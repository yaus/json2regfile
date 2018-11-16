import json
from collections import namedtuple
from jsonschema import validate



class J2R(object):

    J2R_schema = ""

    def __init__(self):
        pass


    
    @staticmethod
    def LoadJson(path):
        with open(path,"rt") as f:
            json_obj=json.load(f)
            f.seek(0)
            validate(json_obj,J2R.J2R_schema)
            rf=J2R()
            if "$schema" in json_obj:
                del json_obj["$schema"]
            json_obj=json.load(f,object_hook=lambda d: namedtuple('X', d.keys(),rename=True)(*d.values()))
            rf.name = json_obj.Config.RegFileName
            rf.addressWidth = json_obj.Config.AddressWidth
            rf.dataWidth = json_obj.Config.dataWidth
            
            pass

import os
J2R.J2R_schema=json.load(open(os.path.dirname(__file__)+"/j2r_schema.json"))