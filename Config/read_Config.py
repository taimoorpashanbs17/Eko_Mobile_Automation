import configparser

class read_Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('D:\GitHub\Eko_Mobile_Automation\Config\data.ini')

    def group_Name(self):
        group_Name = self.config['DEFAULT']['GROUP_NAME']
        return group_Name

    def message(self):
        message = self.config['DEFAULT']['MESSAGE']
        return message

    def topic_Name(self):
        topic_Name = self.config['DEFAULT']['TOPIC_NAME']
        return topic_Name



