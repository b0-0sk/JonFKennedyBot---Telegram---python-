# -*- coding: utf-8 -*-
from configobj import MISSING
class client():
    def __init__(self,username): # nombre del usuario 
        
        self.historial = username + "_historial.txt"
        self.historial1 = {
            "name" : "",
            "history" : ""        
            }
        
    def charCheck(self):
        missingFields = []
        
        for x,y in self.charDict().item:
            if y != "":
                pass
            elif y == "":
                missingFields.append(x)
        return missingFields
    
    def addField(self,definer, text):
        if definer in self.charDict:
            self.charDict[defined] = text
    
    def removeFields(self,):
        for x,y in self.charDict.items():
            self.charDict[x] = ""
            print(self.charDict[x])