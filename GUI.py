import customtkinter

from EnigmaMachine import create_enigma_machine

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def enigma_machine():
    rotors = rotor1.get() + " " + rotor2.get() + " " + rotor3.get()
    reflect = reflector.get()
    ring_settings = ringsetting1.get() + " " + ringsetting2.get() + " " + ringsetting3.get()
    initial_positions = initialposition1.get() + " " + initialposition2.get() + " " + initialposition3.get()
    plugboard = []
    
    if (pairs.get()):
        plugboard = pairs.get().strip().split(" ")
    enigma = create_enigma_machine(rotors, reflect, ring_settings, initial_positions, plugboard)

    text = textbox.get("0.0", "end")[0:-1]
    cipher = enigma.encode(text)
    textbox2.delete("0.0", "end")
    textbox2.insert("0.0", cipher)
    

"ENIGMA MACHINE WINDOW"
root = customtkinter.CTk()
root.geometry("740x650")
root.title("ENIGMA MACHINE EMULATOR")

#Text Frame
frame = customtkinter.CTkFrame(master=root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=3)

label = customtkinter.CTkLabel(master=frame, text="ENIGMA MACHINE")
label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

textbox = customtkinter.CTkTextbox(master=frame, width=700, height=100)
textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
textbox.insert("0.0", "Text to Encode/Decode")

#Rotor Frame
rotor_frame = customtkinter.CTkFrame(master=root)
rotor_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

label1 = customtkinter.CTkLabel(master=rotor_frame, text="ROTORS")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

rotor1 = customtkinter.CTkComboBox(master=rotor_frame, values=["I", "II", "III", "IV", "V"])
rotor1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
rotor2 = customtkinter.CTkComboBox(master=rotor_frame, values=["I", "II", "III", "IV", "V"])
rotor2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
rotor3 = customtkinter.CTkComboBox(master=rotor_frame, values=["I", "II", "III", "IV", "V"])
rotor3.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

#Ring Setting Frame
ring_setting_frame = customtkinter.CTkFrame(master=root)
ring_setting_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

label2 = customtkinter.CTkLabel(master=ring_setting_frame, text="RING SETTINGS")
label2.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ringsetting1 = customtkinter.CTkComboBox(master=ring_setting_frame, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'])
ringsetting1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
ringsetting2 = customtkinter.CTkComboBox(master=ring_setting_frame, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'])
ringsetting2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
ringsetting3 = customtkinter.CTkComboBox(master=ring_setting_frame, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'])
ringsetting3.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

#Initial Position Frame
initial_position_frame = customtkinter.CTkFrame(master=root)
initial_position_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

label3 = customtkinter.CTkLabel(master=initial_position_frame, text="INITIAL POSITIONS")
label3.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

initialposition1 = customtkinter.CTkComboBox(master=initial_position_frame, values=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
initialposition1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
initialposition2 = customtkinter.CTkComboBox(master=initial_position_frame, values=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
initialposition2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
initialposition3 = customtkinter.CTkComboBox(master=initial_position_frame, values=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
initialposition3.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

#Reflector and Plugboard Frames
reflectorplugboard_frame = customtkinter.CTkFrame(master=root)
reflectorplugboard_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

reflector_frame = customtkinter.CTkFrame(master=reflectorplugboard_frame)
reflector_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
label4 = customtkinter.CTkLabel(master=reflector_frame, text="REFLECTOR")
label4.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
reflector = customtkinter.CTkComboBox(master=reflector_frame, values=["B", "C"])
reflector.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

plugboard_frame = customtkinter.CTkFrame(master=reflectorplugboard_frame)
plugboard_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
label5 = customtkinter.CTkLabel(master=plugboard_frame, text="PLUGBOARD")
label5.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
pairs = customtkinter.CTkEntry(master=plugboard_frame, placeholder_text="Enter Plugboard Pairs")
pairs.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

#Cipher Frame
cipher_frame = customtkinter.CTkFrame(master=root)
cipher_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew", columnspan=2)

textbox2 = customtkinter.CTkTextbox(master=cipher_frame, width=500, height=150)
textbox2.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
textbox2.insert("0.0", "Enocoded/Decoded Text")

button = customtkinter.CTkButton(master=cipher_frame, text="ENCODE", command=enigma_machine)
button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


root.mainloop()