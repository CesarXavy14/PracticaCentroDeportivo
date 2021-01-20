class Person:
     
    persons = []

    def __init__(self):
        self.idp = 0
        self.name = ""
        self.lastName = ""
        self.age = 0
        self.contact = 0
        self.email = ""  
    
    def __repr__(self):
        return str(self.__dict__)
     
    def addPerson(self, newPerson):
        self.persons.append(newPerson)
        
    def getPersons(self):
        return self.persons

    def removePerson(self, idp, name):  
        index = 0
        if idp != None:
            for person in self.persons:
                if(person.idp == idp):                   
                    self.persons.pop(index)
                    return self.persons
                index += 1
        elif name != None:
            for person in self.persons:
                if(person.name == name):
                    self.persons.pop(index)
                    return self.persons
                index += 1

    def getPerson(self, idp = None, name = None):
        if idp != None:
            for person in self.persons:
                if(person.idp == idp):
                    return person
        elif name != None:
            for person in self.persons:
                if(person.name == name):
                    return person

    def getId(self, idp = None, name = None):
        if idp != None:
            for person in self.persons:
                if(person.idp == idp):
                    return person.idp
        elif name != None:
            for person in self.persons:
                if(person.name == name):
                    return person.idp

    def getName(self, idp = None, name = None):
        if idp != None:
            for person in self.persons:
                if(person.idp == idp):
                    return person.name
        elif name != None:
            for person in self.persons:
                if(person.name == name):
                    return person.name

    def getContact(self, idp = None, name = None):
        if idp != None:
            for person in self.persons:
                if(person.idp == idp):
                    return person.contact
        elif name != None:
            for person in self.persons:
                if(person.name == name):
                    return person.contact

  

    


