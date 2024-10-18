import torch
print("-----------------------------------")
A = torch.arange(20).reshape(5,4)
print(A)
B = torch.arange(4)
print(B)
C = torch.mv(A,B)
print(C)
