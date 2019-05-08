
from typing import Union
from django.db import models



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