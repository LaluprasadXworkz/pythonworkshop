class Aadhar:

    def __init__(self,name,aadhar_number,dob,finger_print,retina):
        self.name=name
        self.aadhar_number=aadhar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina #private

    def display_userData(self):
        print(f"Retena :{self.__retina},Aadhar Number : {self.aadhar_number}")

    def getRetena(self):
        return self.__retina

var=Aadhar("Prasad",2454658,"1-jan-2020","sdfggghgggg","jgghgghhghjghghghg")
var.display_userData()
retena_var=var.getRetena()
print(retena_var)

