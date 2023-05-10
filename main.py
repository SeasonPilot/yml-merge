import ruamel.yaml
import os

yaml = ruamel.yaml.YAML()
folder = ""  # 您要遍历的文件夹
output = "output.yaml"  # 您要保存的输出文件
files = []  # 用来存储所有的 yaml 文件名
# data = {}  # 用来存储所有的 yaml 数据的字典

# 创建一个空的列表对象，用于存储所有的 yaml 数据
data = []

# 遍历文件夹下的所有文件
for root, dirs, filenames in os.walk(folder):
    for filename in filenames:
        # 判断文件名是否以 .yaml 结尾
        if filename.endswith(".yaml"):
            # 将文件名添加到列表中
            files.append(os.path.join(root, filename))

# 遍历所有的 yaml 文件
for file in files:
    # 加载每个 yaml 文件
    with open(file) as f:
        file_data = yaml.load(f)
        # print(file_data)
        # 判断 file_data 是否为 None
        if file_data is not None:
            # # 将每个 yaml 文件的数据更新到字典中
            # data.update(file_data)

            # 将每个 yaml 文件的数据追加到列表对象中
            data.append(file_data)

# 将字典保存到输出文件中
with open(output, "w") as f:
    yaml.dump(data, f)
