import requests
from io import BytesIO
import tempfile
from django.core import files
from urllib.parse import urlparse
import os



def download(url, temp_file=False, chunk_size=1024*8, django_file=True):
  if temp_file:
    response = requests.get(url, stream=True)
    if response.status_code != requests.codes.ok:
      raise Exception('Failed to download file')  # FIXME: better error handling

    tf = tempfile.NamedTemporaryFile()
    for block in response.iter_content(chunk_size):
      if not block:
        break
      tf.write(block)

    return files.File(tf) if django_file else tf

  else:
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
      raise Exception('Failed to download file')  # FIXME: better error handling

    f = BytesIO()
    f.write(response.content)

    return files.File(f) if django_file else f


def url_to_filename(url):
  return os.path.basename(urlparse(url).path)

