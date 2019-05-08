from typing import List
import numpy as np


class Point:
  row: float
  col: float
  
  def __init__(self, *, row: float, col: float):
    self.row = row
    self.col = col
  
  def __sub__(self, other):
    return Point(row=self.row - other.row, col=self.col - other.col)

  @property
  def x(self):
    return self.col

  @property
  def y(self):
    return self.row

  @classmethod
  def to_numpy(cls, points: List['Point']) -> np.array:
    return np.array([list(p) for p in points])

  @classmethod
  def from_numpy(cls, point_array: np.array) -> List['Point']:
    pass

  def __iter__(self):
    yield self.row
    yield self.col

  def __getitem__(self, idx):
    if idx == 0:
      return self.row
    elif idx == 1:
      return self.col
    else:
      raise KeyError('Key must be an index (0 or 1), got: ' + str(idx))