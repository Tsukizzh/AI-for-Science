import torch
import torchvision
from torch.utils.tensorboard import SummaryWriter
import matplotlib.pyplot as plt

# 设置数据转换
dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

# 加载CIFAR10数据集
test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=dataset_transform, download=True)

# 创建SummaryWriter
writer = SummaryWriter("tensorboard_logs")

# 添加单张图片
img, _ = test_set[0]
writer.add_image("单张图片示例", img, 0)

# 添加多张图片
images = []
for i in range(10):
    img, _ = test_set[i]
    images.append(img)
    # 添加单张图片，每张都有不同的步骤
    writer.add_image(f"图片序列/图片_{i}", img, global_step=i)

# 将图片堆叠成一个批次
image_batch = torch.stack(images)

# 添加图片批次
writer.add_images("图片网格", image_batch, 0)

# 添加一个标量值来显示步骤
for i in range(10):
    writer.add_scalar("步骤", i, global_step=i)

# 确保所有数据都被写入
writer.close()

print("数据已写入TensorBoard。请运行 'tensorboard --logdir=tensorboard_logs' 来查看结果。")

# 使用matplotlib显示几张图片作为参考
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(images[i].permute(1, 2, 0))
    ax.axis('off')
    ax.set_title(f'图片 {i}')
plt.tight_layout()
plt.show()
