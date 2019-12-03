import os
murderers = ["husband", "Jerrod Cooper", "Jamie Smith", "James Moore", "Kyle Travis", "Winston Barger", "Bobby", "Julia Easton", "Kit Armstrong", "Amy Hendler", "Jesse Overton", "Tina Collins"
    , "Nate Metz","Lou Everett" ,"Marlene Valdez", "Max Valdez",  "Dr. Kiera Berhle", "Scott Shelton", "Female Trucker", "Girlfriend", "Kenny Berlin", "Teller 12"
    ,"Paul Millander","Julia Barret","Stu Evans","Roger Jennings","Cameron Nelson","Officer Spencer","Marty Gilmore","Claudia Gideon","Mickey Rutledge","Paul Millander"
    ,"Roy Logan","Russ Bradley","Bartender" ,"Doctor" ,"Jimmy Tadero","Jack","Luke","Patrick Haynes","Amanda Haynes","Tony Thorpe","Roy McCall","Tammy Felton","Justin Green","Mark Rucker","Brad Kendal","Susan Hillridge","Carla Dantini"
    ,"Fred Applewhite","Brad Walden","Syd Goggle","Bonnie Ritten","Walt Braun","Mrs Buckley", "Leigh Spaien", "Ian Wolf"]
files = []
for name in murderers:
    name = name.replace(" ","_")
    name = name.lower()
    name = name + ".txt"
    files.append(name)

os.mkdir("data/good")
os.mkdir("data/bad")
for filename in os.listdir("data/character"):
    path = "data/character/"+filename
    print (path)
    if filename in files:
        os.rename("data/character/"+filename, "data/bad/"+ filename)
    else:
        os.rename("data/character/"+filename, "data/good/"+ filename)
    
