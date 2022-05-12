import os
from utils.YamlUtil import YamReader

#获取项目基本目录
#获取当前目录绝对路径
current = os.path.abspath(__file__)
print(current)
#获取至项目层AutoStudy
BASE_DIR  = os.path.dirname(os.path.dirname(current))
print(BASE_DIR)
_config_path = BASE_DIR + os.sep + "config"
print(_config_path)
_config_file = _config_path + os.sep + "conf.yml"
print(_config_file)

def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

#读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config = YamReader(get_config_file()).data()

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    print(conf_read.get_conf_url())

# config = YamReader(get_config_file()).data()
# print(config)