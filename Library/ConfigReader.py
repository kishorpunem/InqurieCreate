import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFile/Config.cfg")
    return config.get(section, key)


def fetchElementlocators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFile/Element.cfg")
    return config.get(section, key)