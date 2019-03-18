class Property:
    def __init__(self,square_feet='',beds='',baths='',**kwarg):
        super().__init__(**kwarg)
        self.square_feet=square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.beds))
        print("bathrooms: {}".format(self.baths))

    def promt_init():
        return dict(square_feet=input("Enter the square feet: "),beds=input("Enter number of bedrooms"),baths=input("Enter number of pathrooms: "))
    promt_init = staticmethod(promt_init)


class Apartment(Property):
    valid_laundries = ("coin","ensuite","none")
    valid_balconies = ("yes","no","solarium")

    def __init__(self,balcony='',laundry='',**kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("=================")
        print("Laundry : {}".format(self.laundry))
        print("Balcony: {}".format(self.balcony))




    def promt_init():
        parent_init = Property.promt_init()
        laundry = get_valid_input("What laundry facilities does the property have? ",Apartment.valid_laundries)
        balcony = get_valid_input("Does property have a balcony? ",Apartment.valid_balconies)
        parent_init.update({"laundry" : laundry,"balcony":balcony})
        return parent_init
    promt_init = staticmethod(promt_init)

def get_valid_input(input_string,valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)

    while response not in valid_options:
        response=input(input_string)
    return response


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    def __init__(self, num_stories='',
    garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories
    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def promt_init():
        parent_init = Property.promt_init()

        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    promt_init = staticmethod(promt_init)

class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
    def promt_init():
        return dict(
        price=input("What is the selling price? "),
        taxes=input("What are the estimated taxes? "))
    promt_init = staticmethod(promt_init)

class Rental:
    def __init__(self, furnished='', utilities='',rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def promt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    promt_init = staticmethod(promt_init)

class HouseRental(Rental, House):
    def promt_init():
        init = House.promt_init()
        init.update(Rental.promt_init())
        return init
    promt_init = staticmethod(promt_init)

class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class Agent:
    def __init__(self):
        self.property_list = []
    def display_properties(self):
        for property in self.property_list:
            property.display()