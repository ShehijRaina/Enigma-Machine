from PlugLead import PlugLead

#PlugBoard for the Enigma Machine

class Plugboard:
    def __init__(self):
        self.plug_leads = []                 #Creates List For plugleads

    def add(self, pluglead):
        if isinstance(pluglead, PlugLead):                                          #To Check If Object Entered Is Of Class PlugLead, Else Raise Error
            self.plug_leads.append(pluglead) #Adds plugleads To List    

        else:
            print("Invalid Entry: Check Value Entered is of class PlugLead")
            raise ValueError()
        

    def encode(self, character):
        if type(character) is str and len(character) == 1:                          #To Check If Character Entered Is Valid, Else Raise Error   
            letter = character                                                            
            for pluglead in self.plug_leads:  #Goes Through List PlugLeads To Return Encoded Character                                                                                     
                letter = pluglead.encode(character)   
                if letter != character:
                    break
            return letter

        
        else:
            print('Invalid Entry: Check Value entered is 1 Alphabet')
            raise ValueError()

