room_A = input("Enter Room A status (DIRTY/CLEAN): ")
room_B = input("Enter Room B status (DIRTY/CLEAN): ")
position = input("Enter vacuum position (A/B): ")

if position == "A":
    if room_A == "DIRTY":
        print("SUCK")
        room_A = "CLEAN"

    print("MOVE RIGHT")
    
    if room_B == "DIRTY":
        print("SUCK")
        room_B = "CLEAN"

else:
    if room_B == "DIRTY":
        print("SUCK")
        room_B = "CLEAN"

    print("MOVE LEFT")

    if room_A == "DIRTY":
        print("SUCK")
        room_A = "CLEAN"

print("Final State:")
print("Room A =", room_A)
print("Room B =", room_B)