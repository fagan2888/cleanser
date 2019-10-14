

def batches(qs, size=32):
  offset = 0

  while True:
    results = list(qs[offset:offset+size])
    if len(results) < size:
      if len(results) == 0:
        return
      yield results
      return
    else:
      yield results