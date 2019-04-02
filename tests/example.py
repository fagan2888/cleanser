

from cleanser import Dataset, DataImport, Document



def test():

  dataset = Dataset.objects.get(name='imagenet')


  dataset.images.all()

