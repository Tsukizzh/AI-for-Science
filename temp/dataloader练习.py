import torchvision
from torch.utils.data import DataLoader  # 添加这一行
#准备的测试数据集
test_data=torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor())
test_loader =DataLoader(dataset=test_data,batch_size=4,shuffle=True,num_workers=0,drop_last=False)
img,target=test_data[0]
print(img.shape)
print(target)
