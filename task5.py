"""
===================   TASK 5  ====================
* Create class Vehicle which represents any 
* vehicle and carries general info about the 
* vehicle like: company that built that vehicle, 
* model of the vehicle, year of production, 
* registration number, engine power and color.
* Create method cost_of_registration() that will 
* return how much will registration cost for that 
* instance of vehicle.
*
* Use this formula:

     - Production year fees: 100 EUR  if production year < 1990
                             200 EUR  if production year < 2000
                             300 EUR  if production year < 2010 
                             400 EUR  if production year < 2020
     - On production year fee add engine fee:   (engine power in kw * 2 EUR)
*
* In your main function create single instance of the
* Vehicle class and demonstrate the use of
* cost_of_registration method.
===================================================
"""

# Write your class here

class Vehicle:
    def __init__(self, company, model, yearOfProduction, registrationNumber, enginePower, color):
        self.company = company
        self.model = model
        self.yearOfProduction = yearOfProduction
        self.registrationNumber = registrationNumber
        self.enginePower = enginePower
        self.color = color

    def cost_of_registration(self):
        result = 0
        # production year
        if self.yearOfProduction < 1990:
            result = 100
        if self.yearOfProduction < 2000:
            result = 200
        if self.yearOfProduction < 2010:
            result = 300
        if self.yearOfProduction < 2020:
            result = 400

        result = result + self.enginePower * 2
        return result


def main():
    v1 = Vehicle("Audi", "A3", 2001, "BR AB123", 1.5, "Black")
    print(v1.cost_of_registration())


main()



