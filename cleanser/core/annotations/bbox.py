from .point import Point


class BBox:
  top_left: Point
  bottom_right: Point

  @property
  def bottom_left(self):
    return Point(row=self.bottom_right.row, col=self.top_left.col)

  @property
  def top_right(self):
    return

  @classmethod
  def iou(cls, b1, b2):
    raise NotImplementedError()

  def area(self):
    raise NotImplementedError()


def iou(b1: BBox, b2: BBox) -> float:
  raise NotImplementedError()

def intersection(b1: BBox, b2: BBox) -> BBox:
  raise NotImplementedError()