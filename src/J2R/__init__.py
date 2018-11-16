import json
from collections import namedtuple

import schema


class J2R(object):
    def __init__(self):
        pass

    @staticmethod
    def LoadJson(path):
        with open(path,"rt") as f:
            json_obj=json.load(f, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            rf=J2R()
            rf.name = json_obj.Config.RegFileName
            rf.address_width = json_obj.Config.AddressWidth
            
            pass

