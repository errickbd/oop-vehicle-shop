import sys

class CarManager:
    ALL_CARS = []
    TOTAL_CARS = 0
    
    

    def __init__(self, make, model, year, mileage, services = []):
        CarManager.TOTAL_CARS = CarManager.TOTAL_CARS + 1
        self._id = CarManager.TOTAL_CARS
        CarManager.ALL_CARS.append(self)
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = [services]
        
        

    def __str__(self):
        return f'ID {self._id} | Make {self._make} | Model {self._model} | Year {self._year} | Mileage {self._mileage} | Services needed: {self._services}'
    
    def __repr__(self):
        return str(self)
    
    @classmethod
    def add_car(cls):
        make = input("What is the make of your car? ")
        model = input ("What is the model of your car? ")
        year = input("What year was your car made? ")
        mileage = input("How many miles does it have? ")
        services = input("What services does it need? ")
        new_car = cls(make, model, year, mileage, services)
        return new_car
    
    

    @classmethod
    def view_all_cars(cls):
        print(f'List of cars with details: {cls.ALL_CARS}')

    @classmethod
    def view_total_cars(cls):
        print(f'Total amount of cars: {cls.TOTAL_CARS}')

    @classmethod
    def car_detail(cls):
        car_id = int(input("Enter the ID of the car to service: "))
        for car in cls.ALL_CARS:
            if car._id == car_id:
                print(car)

    @classmethod
    def service_car(cls):
        car_id = int(input("Enter the ID of the car to service: "))
        for car in cls.ALL_CARS:
            if car._id == car_id:
                new_service = input("Enter what needs to be done: ")
                car._services.append(new_service)
                print("Service added.")
                
        else:
            print("Car not found.")

    
    @classmethod
    def update_mileage(cls):
        car_id = int(input("Enter the ID of the car with new mileage: "))
        for car in cls.ALL_CARS:
            if car._id == car_id:
                new_mileage = input("What is the new mileage? ")
                car._mileage = new_mileage
                print("Mileage updated.")
                
            else: 
                print("Car not found.")

    @classmethod
    def quit(cls):
        print("Thank you. See you next time.")
        sys.exit()

    @classmethod
    def welcome_menu(cls):
        while True:
            menu_options = print('----Welcome---- \n1. Add a car \n2. View all cars \n3. View total number of cars\n4. See a car\'s details\n5. Service a car\n6. Update mileage\n7. Quit ')
            user_action = int(input("What would you like to do? Input the number to the corresponding action. "))

            match user_action:
                case 1:
                    cls.add_car()
                case 2:
                    cls.view_all_cars()
                case 3:
                    cls.view_total_cars()
                case 4:
                    cls.car_detail()
                case 5:
                    cls.service_car()
                case 6:
                    cls.update_mileage()
                case 7:
                    cls.quit()
                    break
                case _:
                    print("Invalid input")

        return "Thank you. See you next time!"            

            
            




print(CarManager.welcome_menu())






# car1 = CarManager("Toyota", "Supra", 1989, 10000, ['brakes', 'fluids', 'alignment'])
# car2 = CarManager("Honda", "Civic", 1998, 200000, ['tires', 'transmission'])
# car3 = CarManager("Toyota", "Tacoma", 2005, 120000, ['fuel pump'] )



# print(CarManager.add_car)
