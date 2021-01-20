from ClassPerson import *
from ClassItem import *
from ClassTrade import *
from datetime import datetime

listItems = Item()
listPersons = Person()
listTrades = Trade()

idPerson = 0
idItem = 0
idTrade = 0
time = datetime.now()
date = time.strftime("%Y-%m-%d+3 %H:%M:%S")

 

option = 1
while option != 0:

    print("\n")
    print("=== Menú ===")
    print("1.- Ingresar nuevo material.")
    print("2.- Crear nuevo usuario.")
    print("3.- Nuevo prestamo.")
    print("4.- Realizar devolución.")
    print("5.- Guardar lista de personas.")
    print("6.- Guardar lista de materiales.")
    print("7.- Guardar lista de prestamos.")
    print("0.- Salir")
    option = int(input(" - Selecciona una opcion: "))
    print("\n")

    if option == 1:

        newItem = Item()
        
        print("------------ Registro de material ------------")
        print("\n")
        newItem.idi = idItem
        newItem.name = input("Nombre del material: ")
        newItem.quantity = int(input("Cantidad a ingresar: "))

        listItems.addItem(newItem)

        idItem += 1

        print("\n")
        print(" - Registro exitoso! - ")
        print("\n")

        print("**** Lista de Material ****")
        items = listItems.getItems()
        for item in items:
            print('° '+item.name+' '+str(item.quantity))


    elif option == 2:

        newPerson = Person()

        print("------------ Registro de Persona ------------")
        newPerson.idp = idPerson
        newPerson.name = input("Nombre de la persona: ")
        newPerson.lastName = input("Apellido de la persona: ")
        newPerson.age = int(input("Edad de la persona: "))
        newPerson.contact = int(input("Numero de telefóno de la persona: "))
        newPerson.email = input("E - mail de la persona: ")

        listPersons.addPerson(newPerson)

        idPerson += 1

        print("\n")
        print(" - Registro exitoso! - ")
        print("\n")

        print("**** Lista de Personas ****")
        persons = listPersons.getPersons()
        for person in persons:
            print('° '+person.name+' '+person.lastName+' '+str(person.age)+' '+str(person.contact)+' '+person.email)

    elif option == 3:

        newTrade = Trade()

        idp = ""
        namePerson = ""
        contact = ""
        idi = ""
        nameItem = ""
        quantity = 0

        time = datetime.now()
        date = time.strftime("%Y-%m-%d+3 %H:%M:%S")

        print("------------ Registro de Prestamo ------------")
        print("\n")
        print("¿A traves de que quieres identificar a la persona?")
        print("1.- Id")
        print("2.- Nombre")
        replyPerson = int(input("Selecciona una opción: "))

        if replyPerson == 1:

            idFind = int(input("Id de la persona a registrar: "))
            idp = listPersons.getId(idFind, None)
            namePerson = listPersons.getName(idFind, None)
            contact = listPersons.getContact(idFind, None)


        elif replyPerson == 2:

            namePersonFind = input("Nombre de la persona a registrar: ")
            idp = listPersons.getId(None, namePersonFind)
            namePerson = listPersons.getName(None, namePersonFind)
            contact = listPersons.getContact(None, namePersonFind)

        print("\n")
        print("¿A traves de que quieres identificar el material?")
        print("1.- Id")
        print("2.- Nombre")
        replyItem = int(input("Selecciona una opción: "))

        if replyItem == 1:

            idiFind = int(input("Id del material a prestar: "))
            idi = listItems.getId(idiFind, None)
            nameItem = listItems.getName(idiFind, None)


        elif replyItem == 2:

            nameItemFind = input("Nombre del material a prestar: ")
            idi = listItems.getId(None, nameItemFind)
            nameItem = listItems.getName(None, nameItemFind)
            
        quantity = int(input("Cantidad de material a prestar: "))
        
        newTrade.idt = idTrade
        newTrade.personId = idp
        newTrade.personName = namePerson
        newTrade.personContact = contact
        newTrade.itemId = idi
        newTrade.itemName = nameItem
        newTrade.itemQuantity = quantity
        newTrade.date = date

        listTrades.addTrade(newTrade)

        itemsSub = listItems.updateItemSubtraction(idi, None, int(quantity))
        print(itemsSub)

        idTrade += 1

        print("\n")
        print(" - Registro exitoso! - ")
        print("\n")
   
        print("**** Lista de Prestamos ****")
        trades = listTrades.getTrades()
        for trade in trades:
            print(trade.personName+' '+str(trade.personContact)+' '+trade.itemName+' '+str(trade.itemQuantity)+' '+trade.date)


    elif option == 4:
        
        print("--------------- Devolver Prestamo ---------------")
        print("\n")
        print("**** Lista de Prestamos ****")
        trades = listTrades.getTrades()
        for trade in trades:
            print(str(trade.idt)+' '+trade.personName+' '+str(trade.personContact)+' '+trade.itemName+' '+str(trade.itemQuantity)+' '+trade.date)
        
        print("\n")
        idt = int(input("Ingrese el id del prestamo para la devolución: "))

        idiSum = 0
        quantitySum = 0
        for trade in trades:
            if trade.idt == idt:
                trade.date_return = date
                idiSum = trade.itemId
                quantitySum = trade.itemQuantity

        itemSum = listItems.updateItemSum(idiSum,None,quantitySum)
        print(itemSum)
        
        print("\n")
        print("**** Lista de Prestamos ****")
        for trade in trades:
            print(str(trade.idt)+' '+trade.personName+' '+str(trade.personContact)+' '+trade.itemName+' '+str(trade.itemQuantity)+' '+trade.date_return)

    elif option == 5:
        print("\n")
        print("**** Archivo Creado ****")
        filePerson = "filePerson.csv"
        csvp = open(filePerson,"w")
        titlesp = "Id,Nombre,Apellido,Edad,Contacto,Email\n"
        csvp.write(titlesp)  
        personList = listPersons.getPersons()        
        for person in personList:
            idP = str(person.idp)
            name = person.name
            lastName = person.lastName
            age = str(person.age)
            contact = str(person.contact)
            email = person.email
            rowsp = idP+","+name+","+lastName+","+age+","+contact+","+email+"\n"
            csvp.write(rowsp)
            print(str(person.idp)+" "+person.name+" "+person.lastName+" "+str(person.age)+" "+str(person.contact)+" "+person.email)
    
    elif option == 6:
        print("\n")
        print("**** Archivo Creado ****")
        fileItem = "fileItem.csv"
        csvi = open(fileItem,"w")
        titlesi = "Id,Nombre,Cantidad\n"
        csvi.write(titlesi)  
        itemsList = listItems.getItems()        
        for item in itemsList:
            idi = str(item.idi)
            name = item.name
            quantity = str(item.quantity)
            rowsi = idi+","+name+","+quantity+"\n"
            csvi.write(rowsi)
            print(str(item.idi)+" "+item.name+" "+str(item.quantity))
    
    elif option == 7:
        print("\n")
        print("**** Archivo Creado ****")
        fileTrade = "fileTrade.csv"
        csvt = open(fileTrade,"w")
        titlest = "Id,Persona_Id,Persona_Nombre,Contacto,Material_Id,Material_Nombre,Cantidad,Fecha,Devolución\n"
        csvt.write(titlest)  
        tradesList = listTrades.getTrades()
        for trade in tradesList:
            idt = str(trade.idt)
            personId = str(trade.personId)
            personName = trade.personName
            personContact = str(trade.personContact)
            itemId = str(trade.itemId)
            itemName = trade.itemName
            itemQuantity = str(trade.itemQuantity)
            date = trade.date
            date_return = trade.date_return
            rowst = idt+","+personId+","+personName+","+personContact+","+itemId+","+itemName+","+itemQuantity+","+date+","+date_return+"\n"
            csvt.write(rowst)
            print(str(trade.idt)+' '+trade.personName+' '+str(trade.personContact)+' '+trade.itemName+' '+str(trade.itemQuantity)+' '+trade.date)
                    
