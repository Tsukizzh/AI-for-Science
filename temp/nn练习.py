import torch
import torch.nn as nn


# 定义一个简单的神经网络
class Zeheng(nn.Module):
    def __init__(self):
        super(Zeheng, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.fc2 = nn.Linear(20, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x