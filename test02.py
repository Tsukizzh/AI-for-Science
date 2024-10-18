from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image
# 初始化 SummaryWriter
writer = SummaryWriter("logs")
image_path = "data/train/bees_image/2651621464_a2fa8722eb.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
writer.add_image("test",img_array,3,dataformats="HWC")
for i in range(100):
    writer.add_scalar('y=2x', 3*i, i)

# 关闭 SummaryWriter_
writer.close()