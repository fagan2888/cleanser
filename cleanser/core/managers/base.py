from django.db import models



class PandasQuerySetMixin:
  def pandas(self, *fields):
    import pandas as pd
    return pd.DataFrame(self.values(*fields))


class DataQuerySet(PandasQuerySetMixin, models.QuerySet):
  pass
