from django.db import models



class PandasQuerySetMixin:
  def pandas(self, *fields):
    import pandas as pd
    return pd.DataFrame(self.values(*fields))


class NumpyQuerySetMixin:
  def numpy(self, field):
    import numpy as np

    return np.array(self.values_list(field))


class DataQuerySet(PandasQuerySetMixin, models.QuerySet):
  pass




class AnnotationQuerySet(models.QuerySet):
  def labeled(self):
    pass

  def unlabeled(self):
    pass

  def weakly_labeled(self):
    pass

  def verified(self):
    pass

  def unverified(self):
    pass
