class Egg():
    sex = "u" # "m" for male, maybe u for uncertainties
    def __init__(self, sex):
        self.sex = sex
    
    def isMale(self):
        return self.sex=="m"
    
    def updateSex(self, new_sex):
        self.sex = new_sex

    # perhaps make a dummy_egg in place of a null if we want to make computation faster