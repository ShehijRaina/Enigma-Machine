from PlugBoard import Plugboard
from PlugLead import PlugLead
from Reflector import reflector_from_name
from Rotor import rotor_from_name

#Enigma Machine

class EnigmaMachine:
    def __init__(self, rotors, reflector,ring_settings, initial_positions, plugboard_pairs=[]):
        self.alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #String Of Alphabets

        space1 = rotors.find(' ')           #Extracting Rotors From 
        space2 = rotors.rfind(' ')          #String With Their Name
        self.rotorleft = rotor_from_name(rotors[0:space1])
        self.rotormid = rotor_from_name(rotors[space1+1:space2])
        self.rotorright = rotor_from_name(rotors[space2 + 1:])

        self.reflector = reflector_from_name(reflector)
                                            #Extracting Reflector From String With Its Name

        space3 = ring_settings.find(' ')    #Extracting Ring Settings From String
        space4 = ring_settings.rfind(' ')
        self.ringsetleft = int(ring_settings[0:space3])
        self.ringsetmid = int(ring_settings[space3+1:space4])
        self.ringsetright = int(ring_settings[space4+1:])

        space5 = initial_positions.find(' ')#Extracting Initial Positions From String
        space6 = initial_positions.rfind(' ')
        self.posleft = initial_positions[0:space5]
        self.posmid = initial_positions[space5+1:space6]
        self.posright = initial_positions[space6+1:]

        self.plugboard = Plugboard()        #Extracting Plugboard Pairs From List

        if len(plugboard_pairs) <= 10:       #Ensuring No More Than 10 Pairs Can Be Added
            for i in plugboard_pairs:
                self.plugboard.add(PlugLead(i))
        else:
            print("too many plugleads")
            raise ValueError()
        
        #Modifying The Rotors With The Ring Settings
        self.rotorleft.ring_set(self.ringsetleft)
        self.rotormid.ring_set(self.ringsetmid)
        self.rotorright.ring_set(self.ringsetright)

    def encode(self,text):
        ciphertext = ""

        if type(text) is str :
            text = text.upper()             #Converts Text To Uppercase
            length = len(text)              
            
            for i in range(0,length):
                if text[i].isalpha():
                    letter = text[i]

                    #For Rotation Of Rotors Before Encoding
                    rotortrigger = False
                    if self.rotorright.notch:   #Checks If Rightmost Rotor Has A Notch
                        if self.posright == self.rotorright.notch:
                            rotortrigger = True
                    self.posright = self.alphabets[(self.alphabets.index(self.posright) + 1) % 26]#Rotates Rightmost Rotor 1 step
                    if rotortrigger:
                        rotortrigger = False    
                        if self.rotormid.notch: #Checks If Middle Rotor Has A Notch
                            if self.posmid == self.rotormid.notch:
                                rotortrigger = True
                        self.posmid = self.alphabets[(self.alphabets.index(self.posmid) + 1) % 26]#Rotates Middle Rotor 1 step
                        if rotortrigger:
                            rotortrigger = False
                            self.posleft = self.alphabets[(self.alphabets.index(self.posmid) + 1) % 26]#Rotates Leftmost Rotor 1 step
                    #Double Step
                    else:
                        if self.rotormid.notch:
                            if self.posmid == self.rotormid.notch:
                                self.posmid = self.alphabets[(self.alphabets.index(self.posmid) + 1) % 26]#Rotates Middle Rotor 1 step
                                self.posleft = self.alphabets[(self.alphabets.index(self.posleft) + 1) % 26]#Rotates Leftmost Rotor 1 step
                    
                    offsetleft = self.alphabets.index(self.posleft)  #Finds Offset For All Rotors
                    offsetmid = self.alphabets.index(self.posmid)    #After Rotation
                    offsetright = self.alphabets.index(self.posright)

                    '''Letter Goes Through Plugboard'''
                    STEP1 = self.plugboard.encode(letter)
                    
                    '''Letter Goes Through Rotors From Right To Left'''
                    STEP2 = self.rotorright.encode_right_to_left(STEP1, offsetright)
                    STEP3 = self.rotormid.encode_right_to_left(STEP2, offsetmid)
                    STEP4 = self.rotorleft.encode_right_to_left(STEP3, offsetleft)
                    
                    '''Letter Goes Through Reflector'''
                    STEP5 = self.reflector.encode(STEP4)
                    
                    '''Letter Goes Through Rotors From Left To Right'''
                    STEP6 = self.rotorleft.encode_left_to_right(STEP5, offsetleft)
                    STEP7 = self.rotormid.encode_left_to_right(STEP6, offsetmid)
                    STEP8 = self.rotorright.encode_left_to_right(STEP7, offsetright)
                    
                    '''Letter Goes Through Plugboard'''
                    STEP9 = self.plugboard.encode(STEP8)
                else:
                    STEP9 = text[i]
                ciphertext += STEP9 #Encoded Letter Is Added To Rest Of Encoded Text
            
                
            self.rotorleft.rotor_reset()
            self.rotormid.rotor_reset()
            self.rotorright.rotor_reset()
            return ciphertext #Final Encoded Text

        else:
            print('Invalid Entry: Check Value Entered is a string of alphabets')
            raise ValueError()
        
# method with returns an fully set up enigma machine object
# @param - rotors - string of the rotors used in this enigma machine e.g. "I II III"
# @param - reflector - string of the reflector used in this enigma machine e.g. "B"
# @param - ring_settings - string of the ring settings for the rotors, numbered from 01-26 e.g. "01 02 03"
# @param - initial_positions - string of the starting positions of the rotors, from A-Z e.g. "A A Z"
# @param - plugboard_pairs - list of the plugboard pairs to be used, default is an empty list

def create_enigma_machine(rotors, reflector, ring_settings, initial_positions, plugboard_pairs=[]):
    A = EnigmaMachine(rotors,reflector,ring_settings,initial_positions,plugboard_pairs)
    return A