import quick_sketches as m
import numpy as np

a = np.array([3, 4, 5])
#assert m.__version__ == '0.0.4'
assert (m.cm_sketch_preds(5, a, 100, 1) >= a).all()