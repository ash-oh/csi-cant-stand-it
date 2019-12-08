import os
murderers = ["husband", "Jerrod Cooper", "Jamie Smith", "James Moore", "Kyle Travis", "Winston Barger", "Bobby", "Julia Easton", "Kate Armstrong", "Amy Hendler", "Jesse Overton", "Tina Collins"
    , "Nate Metz","Lou Everett" ,"Marlene Valdez", "Max Valdez",  "Kiera Berhle", "Scott Shelton", "Female Trucker", "Girlfriend", "Kenny Berlin", "Tony"
    ,"Paul Millander","Julia Barret","Stu Evans","Roger Jennings","Cameron Nelson","Officer Spencer","Marty Gilmore","Claudia Gideon","Mickey Rutledge","Paul Millander"
    ,"Roy Logan","Russ Bradley","Bartender" ,"Doctor" ,"Jimmy Tadero","Jack","Luke","Patrick Haynes","Amanda Haynes","Tony Thorpe","Roy McCall","Tammy Felton","Justin Green","Mark Rucker","Brad Kendal","Susan Hillridge","Carla Dantini"
    ,"Fred Applewhite","Brad Walden","Syd Goggle","Bonnie Ritten","Walt Braun","Mrs Buckley", "Leigh Sapien", "Ian Wolf"
    ,"Sean Nolan", "Nigel Crane", "Gordon Daimler", "Nicole Exmoor"]
serial = ["Michelle Baldwin",
"Arthur Blisterman",
"Jared Briscoe",
"Jenny Carroll",
"Shane Casey",
"CASt",
"Tom Cooley",
"Gordon Daimler",
"Henry Darius",
"Natalie Davis",
"Steve Davis",
"Charlie DiMasa",
"Clay Dobson",
"Thomas Donover",
"Hollis Eckhart",
"Esteban Fellipe",
"Tammy Felton",
"Darin Hanson",
"Stuart Gardner",
"Lou Gedda",
"Syd Booth Goggle",
"Kevin Greer",
"Nate Haskell",
"Catherine Hill",
"Susan Hillridge",
"John Himmel",
"Dominik Janos",
"Paul Kimball",
"David Lowry",
"Jason McCann",
"Frank McCarthy",
"Paul Millander",
"Kip Miller",
"Esteban Navarro",
"Stewart Otis",
"Marty Pino",
"Daniel Pritchard",
"Walter Resden",
"Bill Ryan",
"Dimitri Sadesky",
"Alisa Santiago",
"Gina Sinclair",
"Casey Steele",
"Tyler Stirling",
"Suspect X",
"Matthew Tarland",
"Jack Toller",
"Sam Vega",
"Lucas Wade",
"Ellen Whitebridge",
"Terry Lee Wicker",
"David Wilson",
"Paul Winthrop",
"Jake Tarland",
"Ellie Brassh",
"Matthew Tarland"]
files = []
for name in murderers:
    name = name.replace(" ","_")
    name = name.lower()
    name = name + ".txt"
    files.append(name)

#os.mkdir("data/good")
#os.mkdir("data/bad")
sort = []
for filename in os.listdir("data/characters/bad"):
    sort.append(filename)

for name in files:
    if name not in sort:
        print (name)
    
