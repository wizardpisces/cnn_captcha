import os
import shutil

source_dir = "sample/origin"
dest_dir = "sample/train-4"

# 遍历目录下的文件
for filename in os.listdir(source_dir):
    # 检查文件名是否符合要求
    if filename.endswith(".jpeg"):
        captcha = filename.split("_")[0]  # 提取文件名中的验证码部分
        if len(captcha) == 4:
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copyfile(source_path, dest_path)

source_dir = "sample/train-4"

for index,filename in enumerate(os.listdir(source_dir)):
    if filename.endswith(".jpeg"):
        newFileName = str(index) + '_' + filename.split("_")[0] + ".jpeg"
        new_source_path = os.path.join(source_dir, newFileName)
        os.rename(os.path.join(source_dir, filename), new_source_path)
        # print(filename.split('_')[1][:4])
        # if len(filename.split('_')[1]) == 3:
        #     os.remove(os.path.join(source_dir, filename))
