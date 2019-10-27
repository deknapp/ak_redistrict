# dicts to manually adjust labels to non-colliding positions

class Label():
  def __init__(x, y, relative=False):
    self.x = x
    self.y = y
    relative = relative

ANCH_LABEL_DICT = {

22: Label(-0.015, 0, True), 
21: Label(-149.98, 61.18),
24: Label(-149.95, 61.11),
27: Label(-149.73, 61.165),
15: Label(0, -0.03, True),
28: Label(-149.73, 61.09),
14: Label(-149.7, 61.2),
13: Label(-149.72, 61.24),

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

def annotate_label(plot, i, centroid, label_dict=None):
  x = 0
  y = 0 
  if i in label_dict.keys():
    if label_dict[i]:
      x = centroid.x + label_dict[i].x
      y = centroid.y + label_dict[i].y 
    else:
      x = label_dict[i].x
      y = label_dict[i].y   
  if x == 0 or y == 0:
    print("problem labeling coordinate for district " + text)
  return plot.annotate(text, xy=(x, y))





