#PlugLead for the Enigma Machine Plugboard

class PlugLead:
    def __init__(self, mapping):
        if type(mapping) is str and len(mapping) == 2 and mapping[0] != mapping[1]: #To Check If Mapping Entered Is Valid, Else Raise Error
            self.plug1 = mapping[0].upper() #Creates 2 Attributes plug1 And plug2       
            self.plug2 = mapping[1].upper() #With The Alphabets                                            

        else:
            print("Invalid Entry: Check PlugLead value entered is String of 2 Different Alphabets")
            raise ValueError()

    def encode(self, character):
        if type(character) is str and len(character) == 1:                          #To Check If Character Entered Is Valid, Else Raise Error
            if character == self.plug1:            
                return self.plug2                                                  
            if character == self.plug2:
                return self.plug1           #Returns The Other Alphabet In Pair
            else:
                return character            #Or Character Itself If No Pair Exists 

        else:
            print('Invalid Entry: Check Value Entered is 1 Alphabet')
            raise ValueError()


