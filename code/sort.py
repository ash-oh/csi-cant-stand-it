import os
murderers = ["husband", "Jerrod Cooper", "Jamie Smith", "James Moore", "Kyle Travis", "Winston Barger", "Bobby", "Julia Easton", "Kit Armstrong", "Amy Hendler", "Jesse Overton", "Tina Collins"
    , "Nate Metz","Lou Everett" ,"Marlene Valdez", "Max Valdez",  "Dr. Kiera Berhle", "Scott Shelton", "Female Trucker", "Girlfriend", "Kenny Berlin", "Teller 12"
    ,"Paul Millander","Julia Barret","Stu Evans","Roger Jennings","Cameron Nelson","Officer Spencer","Marty Gilmore","Claudia Gideon","Mickey Rutledge","Paul Millander"
    ,"Roy Logan","Russ Bradley","Bartender" ,"Doctor" ,"Jimmy Tadero"]
files = []
for name in murderers:
    name = name.replace(" ","_")
    name = name.lower()
    name = name + ".txt"
    files.append(name)


for filename in os.listdir("data/character"):
    path = "data/character/"+filename
    if filename in files:
        os.rename("data/character/"+filename, "data/character/bad/"+ filename)
    else:
        os.rename("data/character/"+filename, "data/character/good/"+ filename)
    
