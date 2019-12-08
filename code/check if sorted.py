import os
murderers = ["husband", "Jerrod Cooper", "Jamie", "James Moore", "Kyle Travis", "Winston Barger", "Bobby", "Julia Eastman", "Kate Armstrong", "Amy Hendler", "Jesse Overton", "Tina Collins"
    , "Nate Metz","Lou Everett" ,"Marlene Valdez", "Max Valdez",  "Kiera Berhle", "Scott Sheldon", "Female Trucker", "Girlfriend", "Kenny Berlin", "Tony"
    ,"Paul Millander","Julia Barett","Stu Evans","Roger Jennings","Cameron Nelson","Officer Spencer","Marty Gilmore","Claudia Gideon","Mickey Rutledge","Paul Millander"
    ,"Roy Logan","Russ Bradley","Bartender" ,"Doctor" ,"Jimmy Tadero","Jack","Luke","Patrick Haynes","Amanda Haynes","Tony Thorpe","Roy McCall","Tammy Felton","Justin Green","Mark Rucker","Brad Kendal","Susan Hillridge","Carla Dantini"
    ,"Fred Applewhite","Brad Walden","Syd Goggle","Bonnie Ritten","Walt Braun","Mrs. Buckley", "Dr. Leigh Sapien", "Ian Wolf"
    ,"Sean Nolan", "Nigel Crane", "Gordon Daimler", "Nicole Exmoor", "Jeri Newman", "Eric Branson", "Graham Cooper",
    "Hostess", "Ross Halpo", "Les Dutton", "John Damen", "Peter Arnz","Mr. Jones", "Luke", "Kelly Goodson", 
    "Michael Borland", "Mandy Klinefeld", "Cameron Klinefeld", "Stuart Gardner", "Steve Jansson", "Vicky Winston", "Paul Winston", "Eric Brooks","Faye Minden","Sam Abernathy", "Craig", "Zack Lawrence", "Raina Press",
    "Crystal", "Daniel Halburt","Sybil Perez", "Carlos Perez","Hayden Michaels", "Matthew Hawkins", "Jeff Simon", "Susan", "Host",
    "Walter Gordon","Sandra Walkey", "Leon Sneller", "Gregory Kimble", "Natalie Davis","Robert Hsing", "Gavin McGill", "Cole Tritt", 
    "Tara Miller", "Cha cha Romero","Thomas Simon","Megan Cooper", "Sheila Latham", "Charlie Kellerman", "Diane Kentner","Gus DiFusco", "Chandru 'Dru' Kambhatla",
    "Stanley Vespucci","Terry Lee Wicker","Marlon West","Tommy Halpert", "Tommy","Troy Birkhart","Dustin Lightfoot", "Cash Dooley"]

files = []
for name in murderers:
    name = name.replace(" ","_")
    name = name.lower()
    name = name + ".txt"
    files.append(name)

#os.mkdir("data/good")
#os.mkdir("data/bad")
sort = []
for filename in os.listdir("data/bad"):
    sort.append(filename)

for name in files:
    if name not in sort:
        print (name)

print("done")
    
