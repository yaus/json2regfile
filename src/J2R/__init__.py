import json
class J2R(object):
    def __init__(self):
        pass

    @staticmethod
    def LoadJson(path):
        with open(path,"rt") as f:
            x=json.load(f)

            pass