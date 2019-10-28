# dicts to manually adjust labels to non-colliding positions

import string

class Label():
  def __init__(self, x, y, relative=False):
    self.x = x
    self.y = y
    self.relative = relative

ANCH_LABEL_DICT = {

22: Label(-0.015, 0, relative=True), 
21: Label(-149.98, 61.18),
24: Label(-149.95, 61.11),
27: Label(-149.73, 61.165),
15: Label(0, -0.03, relative=True),
28: Label(-149.73, 61.09),
14: Label(-149.7, 61.2),
13: Label(-149.72, 61.24),

}

FAIRBANKS_SEN_LABEL_DICT = {

1: Label(-147.77, 64.83),
4: Label(-147.8, 64.91),
5: Label(-147.9, 64.8),
6: Label(-147.3, 64.87),

}


def house_sen_dict():
  dct = dict()
  letters = list(string.ascii_uppercase)
  j = 0
  for i in range(1, 41):
    dct[i] = letters[j]
    if i%2 == 0:
      j += 1
  return dct

def sen_house_dict():
  dct = dict()
  letters = list(string.ascii_uppercase)
  j = 0
  for i in range(1, 41):
    if letters[j] in dct.keys():
      dct[letters[j]].append(i)
    else:
      dct[letters[j]] = [i]
    if i%2 == 0:
      j += 1
  return dct

HOUSE_SEN_DICT = house_sen_dict()

def sen_label(i):
  return str(i) + ' - ' + HOUSE_SEN_DICT[i]

def annotate_label(plot=None, i=None, text=None, centroid=None, label_dict=None):
  x = 0
  y = 0 
  if label_dict is None:
    x = centroid.x
    y = centroid.y
  elif i in label_dict.keys():
    if label_dict[i].relative:
      x = centroid.x + label_dict[i].x
      y = centroid.y + label_dict[i].y 
    else:
      x = label_dict[i].x
      y = label_dict[i].y   
  else:
      x = centroid.x
      y = centroid.y
  if x == 0 or y == 0 or text is None:
    print("problem labeling coordinate for district " + text)
  return plot.annotate(text, xy=(x, y))





