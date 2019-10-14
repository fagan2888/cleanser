import cleanser
from typing import Iterable

from torch.utils.data import DataLoader
from torchvision.models import SqueezeNet
from torchvision import transforms
import torch


def download(url=None):
  return ''


def create():
  root = download()
  cifar = cleanser.ImageDataset.from_folders('cifar10', root)


def evaluate(model: cleanser.Model, dataset: cleanser.ImageDataset, batch_size=32):
  pass


model = SqueezeNet()
transform = transforms.Compose([
  transforms.ToTensor(),
  # transforms.Normalize()
])

cifar10 = cleanser.ImageDataset.objects.get(name='cifar10')

images: Iterable[cleanser.Image]
for images in cifar10.images.split('test').batches(32):
  batch = torch.stack([transform(img.pillow) for img in images])
  preds = model(batch)
