import yaml

with open("./data2.yaml", "r", encoding="utf-8") as f:
    # 使用yaml加载数据
    data = yaml.safe_load(f)
    print("返回字典数据：", data)
# print("返回字典类型：", type(data))
    print("返回字典类型：", type(data.get("value2")))
