
from typing import Union
from django.db import models

from .. import settings


def run_sql(command: str):
  """
  https://docs.djangoproject.com/en/dev/topics/db/sql/

  :param command:
  :return:
  """
  from django.db import connection
  with connection.cursor() as c:
    c.execute(command)


def vacuum(table: Union[str, models.Model]):
  pass


def cluster_on_index(table, index):
  pass


async def get_async_connection(db='default', settings=settings):
  import asyncpg
  db_info = settings.DATABASES[db]
  connection = await asyncpg.connect(
    user=db_info['USER'],
    host=db_info['HOST'],
    database=db_info['NAME'],
    password=db_info['PASSWORD'],
    port=db_info['PORT']
  )
  return connection


def _translate_sql_template(sql):
  """
  asyncpg uses placeholders of form $1, ${n}
  django uses %s
  need to replace %s with ${n}
  :return:
  """
  x = sql
  for n in range(1, sql.count('%s') + 1):
    x = x.replace('%s', f'${n}', 1)
  return x


def get_asyncpg_query(queryset: models.QuerySet):
  sql_template, params = queryset.query.get_compiler(using=queryset.db).as_sql()
  return _translate_sql_template(sql_template), params


async def run_async(query: Union[str, models.QuerySet], connection=None, settings=settings):
  open_connection = connection is None
  if open_connection:
    connection = await get_async_connection(settings=settings)

  if isinstance(query, str):
    results = await connection.fetch(query)
  else:
    sql_template, params = get_asyncpg_query(queryset=query)
    results = await connection.fetch(sql_template, *params)


  if open_connection:
    await connection.close()

  return results