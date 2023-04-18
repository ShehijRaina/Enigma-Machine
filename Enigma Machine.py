from EnigmaMachine import create_enigma_machine

#ENIGMA MACHINE EMULATOR

while True:
    print("WELCOME\n")
    print("Choose your Enigma Settings\n")
    print("""ROTORS
            1. I
            2. II
            3. III
            4. IV
            5. V
            """)
    print("Choose any three")
    rotor1 = int(input("Rotor 1 (enter integer from 1 - 5) " ))
    rotor2 = int(input("Rotor 2 (enter integer from 1 - 5) "))
    rotor3 = int(input("Rotor 3 (enter integer from 1 - 5) "))
    l = ["I", "II", "III", "IV", "V"]
    rotors = l[rotor1 - 1] + " " + l[rotor2 - 1] + " " + l[rotor3 - 1]
    
    print("""\nREFLECTORS
            - B
            - C
            """)
    print("Choose any one")
    reflector = input("Reflector (enter B or C) ")
    reflector = reflector.upper()
    
    print("""\nRING SETTINGS
          1-26, 1-26, 1-26""")
    set1 = int(input("Initial Settings for leftmost rotor (enter integer from 1 - 26) " ))
    set2 = int(input("Initial Settings for middle rotor (enter integer from 1 - 26) " ))
    set3 = int(input("Initial Settings for rightmost rotor (enter integer from 1 - 26) " ))
    d = {1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06", 7: "07", 8: "08", 9: "09", 10: "10", 11: "11", 12: "12", 13: "13", 14: "14", 15: "15", 16: "16", 17: "17", 18: "18", 19: "19", 20: "20", 21: "21", 22: "22", 23: "23", 24: "24", 25: "25", 26: "26"}
    ring_settings = d[set1] + " " + d[set2] + " " + d[set3]
    
    print("""\nINITIAL POSITIONS
          A-Z, A-Z, A-Z""")
    pos1 = input("Initial Position for leftmost rotor (enter alphabet from A - Z) " )
    pos2 = input("Initial Position for middle rotor (enter alphabet from A - Z) " )
    pos3 = input("Initial Position for rightmost rotor (enter alphabet from A - Z) " )
    initial_positions = pos1.upper() + " " + pos2.upper() + " " + pos3.upper()
    
    print("\nPLUGBOARD PAIRS")
    num = int(input("how many pairs do you want to enter (must be <= 10): "))
    plugboard_pairs = []
    for i in range(num):
        pair = input("Enter pair (any 2 aplhabets of the form AB, CL, EK.... ")
        plugboard_pairs.append(pair.upper())
    
        if i == 9:
            break
             
    
    
    
    enigma = create_enigma_machine(rotors, reflector, ring_settings, initial_positions, plugboard_pairs)
    print("Enter text to encode/decode")
    t1 = input(">>>")
    text = ''
    for i in t1:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "abcdefghijklmnopqrstuvwxyz":
            text += i
    
    print(enigma.encode(text))
