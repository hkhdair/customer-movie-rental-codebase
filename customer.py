import sys
from rental import Rental
import datetime

class Customer:
    def __init__(self,name):
        # Our constructor method which instantiates various customer objects. 
        self.name = name
        self.movie = ""
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
        self.shop = Rental()

    def show_currently_rented(self):
        # Show movies currently rented by customer
        if self.movie and self.rentalTime and self.rentalBasis:
            print(f"{self.name} rented {self.movie} on {self.rentalTime}")
            return self.movie
        else:
            print(f"{self.name} has no movies currently rented")
            return None

    def rent_movie(self, movie, rentCondition):
        # Set the request from the customer for the movie they want to rent 
        movie = movie.lower()
        self.movie = movie
        
        while True:
            if rentCondition == "hourly":
                self.rentalBasis = 1
                self.rentalTime = datetime.datetime.now().replace(microsecond=0)
                break
            elif rentCondition == "daily":
                self.rentalBasis = 2
                self.rentalTime = datetime.datetime.now().replace(microsecond=0)
                break
            elif rentCondition == "weekly":
                self.rentalBasis = 3
                self.rentalTime = datetime.datetime.now().replace(microsecond=0)
                break
            elif rentCondition == "exit":
                sys.exit(1)
            else:
                print("Please enter either hourly, daily or weekly or enter exit to exit")
                continue
        return self.movie, self.rentalTime, self.rentalBasis

    def return_movie(self):
        # Allows customers to return their movies to the rental shop 
        if self.movie and self.rentalTime and self.rentalBasis:
            return self.movie, self.rentalTime, self.rentalBasis
        else:
            return 0, 0, 0
