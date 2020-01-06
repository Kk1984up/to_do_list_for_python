# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:45:50 2019

@author: libozhang
"""
import torch.onnx
import torchvision

dummy_input = torch.randn(1, 3, 224, 224)
model = torchvision.models.alexnet(pretrained=True)
torch.onnx.export(model, dummy_input, "alexnet.onnx")

import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)