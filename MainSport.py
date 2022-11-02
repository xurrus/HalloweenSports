from controllerSports import ControllerSports
from event import Event

controller = ControllerSports()

newEvent = Event("GREFG","09/09/1999","Alcantera","Valencia",10,"nose")
controller.addEvent(name="GREFG",event=newEvent)
controller.addParticipant(name="GREFG",dni="20931483B",pName="David Gozalvez",age=19,email="email.com")
controller.addParticipant(name="GREFG",dni="11111111A",pName="Joan Segundo",age=20,email="joanemail.com")
controller.addParticipant(name="GREFG",dni="12345678A",pName="Peisen Tercero",age=23,email="peisenemail.com")
controller.addParticipant(name="GREFG",dni="12345678B",pName="Jorge Profe",age=46,email="jorgeemail.com")


newEvent = Event("ALBERTO","01/01/2001","Enguera","Valencia",15,"nose")
controller.addEvent(name="ALBERTO",event=newEvent)
controller.addParticipant(name="ALBERTO",dni="78945612A",pName="Dani Ruso",age=20,email="email.com")
controller.addParticipant(name="ALBERTO",dni="78945612B",pName="Pablo",age=19,email="pabloemail.com")
controller.addParticipant(name="ALBERTO",dni="78945612C",pName="Carlos Tercero",age=25,email="carlos.com")
controller.addParticipant(name="ALBERTO",dni="78945612D",pName="Ana Java",age=43,email="anaemail.com")

while True:
    print("")
    print("We have ",controller.countEvents()," events")
    print("1.- Add Event")
    print("2.- Add participant to an event*")
    print("3.- List pending events with participants")
    print("4.- List events finished with podium")
    print("5.- Finish an event")
    option = int(input("Select an option:"))
    
    if option == 1:
        name = input("Enter the name of the event: ")
        date = input("Enter the date of the event (dd/mm/yyyy): ")
        location = input("Enter the location of the event: ")
        province = input("Enter the province of the event: ")
        price = int(input("Enter the price of the event: "))
        totalEvent = input("Enter the total Event of the event: ")
        newEvent = Event(name,date,location,province,price,totalEvent)
        if (controller.addEvent(name,newEvent)):
            print("Event added!")
        else:
            print("Error. Event already exists")
    elif option == 2:
        name = input("Enter the name of the event: ")
        dni = input("Enter the DNI of the participant: ")
        pName = input("Enter the name of the participant: ")
        age = input("Enter the age of the participant: ")
        email = input("Enter the email of the participant (API): ")
        if (controller.addParticipant(name,dni,pName,age,email)):
            print("Participant ",pName," added!")
        else:
            print("Error adding the participant")
    elif option == 3:
        if (controller.countPending() > 0):
            events = controller.getEvents()
            print("Pending events:")
            for name,event in events.items():
                if (event.isFinished() == False):
                    participants = event.getParticipants()
                    print(name)
                    for i in range(len(participants)):
                        print("\t",participants[i][1])
        else:
            print("There aren't any pending event")
    elif option == 4:
        if (controller.countFinished() > 0):
            events = controller.getEvents()
            print("Finished events...")
            for name,event in events.items():
                if (event.isFinished()):
                    print(name)
                    podium = event.getPodium()
                    print("\tFIRST: ",podium["FIRST"][1])
                    print("\tSECOND: ",podium["SECOND"][1])
                    print("\tTHIRD: ",podium["THIRD"][1])
        else:
            print("There aren't any finished event")
    elif option == 5:
        name = input("Enter the name of the event to finish it: ")
        if (controller.finishEvent(name)):
            print("Event finished!")
        else:
            print("Error finishing event")