import random
class ControllerSports():
    def __init__(self):
        self.__events = {}
        
    def addEvent(self,name,event):
        if name in self.__events:
            return False
        self.__events[name] = event
        return True
    
    def addParticipant(self,name,dni,pName,age,email):
        if name not in self.__events:
            return False
        self.__events[name].addParticipant(dni,pName,age,email)
        return True

    def countEvents(self):
        return len(self.__events)
    
    def getEvents(self):
        return self.__events

    def finishEvent(self,name):
        if name not in self.__events:
            return False
        event = self.__events[name]
        if (event.isFinished()):
            return False
        participants = event.getParticipants()
        if (len(participants) < 3):
            return False
        first,second,third = 0,0,0
        #ASIGNAMOS LA POSICION 1
        first = random.randrange(len(participants))
        #ASIGNAMOS LA 2
        while True:
            aleatorio = random.randrange(len(participants))
            if aleatorio !=first:
                second = aleatorio
                break
        #ASIGNAMOS LA 3
        while True:
            aleatorio = random.randrange(len(participants))
            if aleatorio !=first and aleatorio!=second:
                third = aleatorio
                break
        event.finishEvent(participants[first],participants[second],participants[third])
        return True
    
    def countFinished(self):
        cont = 0
        for name, event in self.__events.items():
            if (event.isFinished()):
                cont += 1
        return cont
    
    def countPending(self):
        cont = 0
        for name, event in self.__events.items():
            if (event.isFinished() == False):
                cont += 1
        return cont