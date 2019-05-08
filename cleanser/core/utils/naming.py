import inspect


def fully_qualified_name(x, **kwargs):
  args = f"({', '.join(str(k) + '=' + str(v) for k, v in kwargs.items())})"
  if inspect.isclass(x):
    return f"{x.__module__}.{x.__name__}{args}"
  elif inspect.isfunction(x):
    return f"{x.__module__}.{x.__name__}{args}"
  return f"{x.__class__.__module__}.{x.__class__.__name__}{args}"
