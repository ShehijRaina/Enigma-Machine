#Rotor for the Enigma Machine

class Rotor:
    def __init__(self, mappings, notch = None):
        self.alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #String Of Alphabets
        if type(mappings) is str and len(mappings) == 26:                           #To Check If Mapping Entered Is Valid, Else Raise Error
            self.mappings = mappings 
            self.originalmappings = mappings
            self.notch = notch              #Creates 2 Attributes mappings And notch
            
        else:
            print('Invalid Entry: Check Mappings are Entered in String 26 Alphabets')
            raise ValueError()
        
    def rotor_reset(self):
      self.mappings = self.originalmappings
      
    def ring_set(self,ringsetting):          #Changes The Mappings To Correspond With Given Ring Settings
        STRING =''
        for i in range(0, len(self.mappings)):
            alphabet = self.mappings[i]
            alphabetord = ord(alphabet)
            newalphabet = chr((((alphabetord - 65 + (ringsetting-1)) % 26) + 65))
            STRING += newalphabet
        string = STRING[26-(ringsetting-1):] + STRING[0:26-(ringsetting-1)]
        self.mappings = string

               

    def encode_right_to_left(self, character, offset):
        index = self.alphabets.index(chr(((ord(character) - 65 + offset) % 26) + 65))
                                            #Uses Index Of Alphabet From Alphabets To Find Letter The Rotor Encodes It As
                                            #Taking Into Consideration Offset
        letter = chr(((ord(self.mappings[index]) - 65 - offset) % 26) + 65)

        return letter

    def encode_left_to_right(self, character, offset):
        index = self.mappings.index(chr(((ord(character) - 65 + offset) % 26) + 65))
                                            #Uses Index Of Alphabet From Mappings To Find Letter The Rotor Encodes It As
                                            #Taking Into Consideration Offset
        letter = chr(((ord(self.alphabets[index]) - 65 - offset) % 26) + 65)

        return letter

def rotor_from_name(name):                  #Returns Rotor From Its String Name
    if name in ['I', 'II', 'III', 'IV', 'V']:
        #Creating Rotors
        if name == 'I':
            '''Rotor I'''
            return(Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"))
        elif name == 'II':
            '''Rotor II'''
            return(Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"))
        elif name == 'III':
            '''Rotor III'''                                                                                                                
            return(Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","V"))
        elif name == 'IV':
            '''Rotor IV'''
            return(Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"))
        elif name == 'V':
            '''Rotor V'''
            return(Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"))
    

    

    
    
    


