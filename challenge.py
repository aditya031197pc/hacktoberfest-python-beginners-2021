#  ISSUE ONE 

class Restaurant():

  """" 
  1.Initialize the class with the attributes
  name, type_restaurant, address. This info comes through the paramerters.
  2. add and atribute called number_people_served and 
  initialize it with zero.
  """

  def __init__(self,name,type_restaurant,address):
    self.name=name
    self.type_restaurant=type_restaurant
    self.address=address
    self.number_people_served=0

  def print_restaurant_info(self): 
    """ This method prints the restaurant 
    info.
    Include the atrributes and add
    any other info you like  
    make sure proper capitalization is used 
    """
    print(f"Name : {self.name}\nType : {self.type_restaurant}\nAddress : {self.address}\nNumber of People Served:{self.number_people_served}")

  def set_number_people_served(self,n_served):
    """ this methods recieves the 
    number of people served 
    and adds it to the attribute number_people_served """
    self.number_people_served+=n_served
     

  def print_number_people_served(self):
    print(f"The number of people served by {self.name} are {self.number_people_served}")





# ISSUE TWO    
  
class CoffeeStore(      ):
    """  Make sure this class inherits Restaurant
     """

  def __init__(self,     ): 
    """initialize it  with an attribute called name and using a variable called
    restaurant_type with the default value 'coffe_store'. These are received through parameters. Make sure to call the super() method and pass the right parameters"""

    """
    add an attribute called coffe_types. This will store a list with at least 3 types of coffe of your choice"""
     
     # write your code here 




  def print_coffe_store_info(self):
    """
    This methods prints the coffe store info 
    use a for loop to print the coffy types in a 
    bullet list format
    Add any other info you like 
    """




# ISSUE 3     
""" Write the main part of the program
make an instace of the class Restaurante
and call the methods
Make an instance of the class CoffeeStore
call 
"""

# write your code here  