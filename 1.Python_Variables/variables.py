# Assigning Varibales

name = "Timothy Wangwe"     # String
name
male = True                 # Boolean
male
age = 20                    # Integer
age
birth_year = 2020 - age     # Operations
birth_year
height = 1.78               # Float
height
interests = [               # List
            'Data Science', 
            'Basketball', 
            'Sci-fi Movies'
            ] 
interests
summary = {                 # Dictionary
    "Name":       name,
    "Age":        age,
    "Birth year": birth_year,
    "Height":     height,
    "Interests":  interests,
}
summary

# Scope
# =======

# Local Scope
def scope():
    campus = "TRC"
              # Returns
print(campus) # NameError: name 'campus' is not defined


# Global Scope
campus = "TRC"

def scope():
    global campus   # Keyword 'global'
    campus = "TOWN"

scope()
print(campus)       # Returns "TOWN"

# Without key word
campus = "TRC"

def scope():
    campus = "TOWN"

scope()
print(campus)       # Returns "TRC"