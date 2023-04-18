#Reflector Pair for the Enigma Machine Reflectors

class ReflectorPair:
    def __init__(self, mapping):                                                    #To Check If Mapping Entered Is Valid, Else Raise Error
        if type(mapping) is str and len(mapping) == 2 and mapping[0] != mapping[1]:
            self.reflector1 = mapping[0]    #Creates 2 Attributes reflector1 And reflector2
            self.reflector2 = mapping[1]    #With The Alphabets 

        else:
            print("Invalid Entry: Check Value entered is String of 2 different Alphabets")
            raise ValueError()

    def encode(self, character):
        if type(character) is str and len(character) == 1:                           #To Check If Character Entered Is Valid, Else Raise Error                     
            if character == self.reflector1:
                return self.reflector2
            if character == self.reflector2:
                return self.reflector1      #Returns The Other Alphabet In Pair

        else:
            print('Invalid Entry: Check Value Entered is 1 Alphabet')
            raise ValueError()
       
 