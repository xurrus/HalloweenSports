class Event():
    
    def __init__(self,name,date,location,province,price,totalEvent):
        self.__name = name
        self.__date = date
        self.__location = location
        self.__province = province
        self.__price = price
        self.__totalEvent = totalEvent
        self.__participants = [] #DNI,Name,Age,Email
        self.__finished = False
        self.__podium = {}
        
    def getName(self):
        return self.__name
    def getDate(self):
        return self.__date
    def getLocation(self):
        return self.__location
    def getProvince(self):
        return self.__province
    def getPrice(self):
        return self.__price 
    def getTotalEvent(self):
        return self.__totalEvent
    def getParticipants(self):
        return self.__participants
    def isFinished(self):
        return self.__finished
    def getPodium(self):
        return self.__podium
    
    def addParticipant(self,dni,pName,age,email):
        self.__participants.append((dni,pName,age,email))

    def finishEvent(self,first,second,third):
        self.__finished = True
        self.__podium["FIRST"] = first
        self.__podium["SECOND"] = second
        self.__podium["THIRD"] = third