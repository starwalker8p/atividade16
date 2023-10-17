idoso,gestante,cadeirante=str(input("você é idoso? sim ou não.")),str(input("você é gestante? sim ou não.")),str(input("você é cadeirante? sim ou não."))
if idoso=="sim" or gestante=="sim" or cadeirante=="sim":
    print("fila preferencial")
else: 
    print("não preferencial")