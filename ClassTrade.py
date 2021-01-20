class Trade:

     trades = []

     def __init__(self):
          self.idt = 0
          self.personId = ""
          self.personName = ""
          self.personContact = ""
          self.itemId = 0
          self.itemName = ""
          self.itemQuantity = 0
          self.date = ""
          self.date_return = ""
     
     def __repr__(self):
          return str(self.__dict__)
     
     def addTrade(self, newTrade):
          self.trades.append(newTrade)

     def getTrades(self):
          return self.trades
     
     def dropTrade(self, idt):
          index = 0
          if idt != None:
               for trade in self.trades:
                    if(trade.idt == idt):                   
                         self.trades.pop(index)
                         return self.trades
                    index += 1

        
    
    
