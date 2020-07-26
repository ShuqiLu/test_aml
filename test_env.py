import torch
print(torch.__version__)
from apex.contrib.optimizers import FP16_Optimizer, FusedAdam
print('ok..')