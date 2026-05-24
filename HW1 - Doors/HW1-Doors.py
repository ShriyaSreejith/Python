#Shriya Sreejith - HW1 - Doors - Spring 2025 
#Converts pounds to Newtons and inches to meters
#Calculates the force on the top and bottom hinges of a door

#input
doorWeight = float(input("What is the weight of the door in pounds: "))
doorHeight = float(input("What is the height of the door in inches: "))
distTophinge = float(input("What is the distance from the top of the door to the top hinge in inches: "))
distBottomhinge = float(input("What is the distance from the bottom of the door to the bottom hinge in inches: "))

#convertions
lb_to_Newtons = 4.44822162
in_to_meters = 0.0254

weightNewtons = doorWeight * lb_to_Newtons
heightMeters = doorHeight * in_to_meters
distTophingeMeters = distTophinge * in_to_meters
distBottomhingeMeters = distBottomhinge * in_to_meters

#calculations
forceTopHinge = (weightNewtons * (heightMeters / 2)) / (heightMeters - distBottomhingeMeters)
forceBottomHinge = (weightNewtons * (heightMeters / 2)) / (heightMeters - distTophingeMeters)

#output
print(f"The force on the top hinge is {forceTopHinge} Newtons.")
print(f"The force on the bottom hinge is {forceBottomHinge} Newtons.")