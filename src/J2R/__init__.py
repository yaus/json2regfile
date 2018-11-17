import json
import re
from collections import namedtuple
from jsonschema import validate



class J2R(object):

    J2R_schema = ""

    def __init__(self):
        pass


    @staticmethod
    def ReadInteger(string):
        if isinstance(string,int):
            return string
        m_Int = ReadInteger.reInt.match()
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
            rf.dataWidth = json_obj.Config.DataWidth
            rf.pipeline = getattr(json_obj.Config,"Pipeline",False)
            rf.busType = getattr(json_obj.Config,"BusType","")
            rf.startAddress = J2R.ReadInteger(json_obj.RegFile.StartAddress)
            
            rf.endAddress = 
            pass

import os
J2R.J2R_schema=json.load(open(os.path.dirname(__file__)+"/j2r_schema.json"))
J2R.ReadInteger.reInt = re.compile(r'(\+|-)?\d+')
J2R.ReadInteger.reVHex = re.compile(r'(?P<WIDTH>\d?)\'(?P<IS_SIGN>s?)h(?P<SIGN>(\+|-)?)(?P<DIGIT>[0-9A-Za_z_]+)')
J2R.ReadInteger.reVBin = re.compile(r'(?P<WIDTH>\d?)\'(?P<IS_SIGN>s?)b(?P<SIGN>(\+|-)?)(?P<DIGIT>[01_]+)')
J2R.ReadInteger.reVDec = re.compile(r'(?P<WIDTH>\d?)\'(?P<IS_SIGN>s?)d(?P<SIGN>(\+|-)?)(?P<DIGIT>[0-9_]+)')
