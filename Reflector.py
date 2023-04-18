from ReflectorPair import ReflectorPair

#Reflector for the Enigma Machine

class Reflector:
    def __init__(self):
        self.reflector = []                 #Cretes List For Connected Alphabets in Reflector

    def add(self, reflectorpair):
        if isinstance(reflectorpair, ReflectorPair):                                #To Check If Object Entered Is Of Class ReflectorPair, Else Raise E
            self.reflector.append(reflectorpair)
                                            #Adds Pairs To List
        else:
            print("Invalid Entry: Check Value entered is of class ReflectorPair")
            raise ValueError()
        

    def encode(self, character):
        if type(character) is str and len(character) == 1:                          #To Check If Character Entered Is Valid, Else Raise Error 
            for i in self.reflector:
                if character == i.reflector1 or character == i.reflector2:
                    return i.encode(character)
                                            #Returns The Other Alphabet From Pair

        else:
            print('Invalid Entry: Check Value Entered is 1 Alphabet')
            raise ValueError()

#Creating Reflectors

'''Reflector B'''
B = Reflector()
B.add(ReflectorPair("AY")); B.add(ReflectorPair("BR")); B.add(ReflectorPair("CU")); B.add(ReflectorPair("DH"))
B.add(ReflectorPair("EQ")); B.add(ReflectorPair("FS")); B.add(ReflectorPair("GL")); B.add(ReflectorPair("IP"))
B.add(ReflectorPair("JX")); B.add(ReflectorPair("KN")); B.add(ReflectorPair("MO"))
B.add(ReflectorPair("TZ")); B.add(ReflectorPair("VW"))


'''Reflector C'''
C = Reflector()
C.add(ReflectorPair("AF")); C.add(ReflectorPair("BV")); C.add(ReflectorPair("CP")); C.add(ReflectorPair("DJ"))
C.add(ReflectorPair("EI")); C.add(ReflectorPair("GO")); C.add(ReflectorPair("HY")); C.add(ReflectorPair("KR"))
C.add(ReflectorPair("LZ")); C.add(ReflectorPair("MX")); C.add(ReflectorPair("NW"))
C.add(ReflectorPair("QT")); C.add(ReflectorPair("SU"))



def reflector_from_name(name):              #Returns Reflector From Its String Name
    NAMES = { "B": B, "C": C}
    if name in NAMES:
        return NAMES[name]
