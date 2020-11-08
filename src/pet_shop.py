# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(input_dictionary):
    result = input_dictionary["name"]
    return result

def get_total_cash(input_dictionary):
    return input_dictionary["admin"]["total_cash"]


def add_or_remove_cash(input_dict, amount_to_add):
    final_amount = input_dict["admin"]["total_cash"] + amount_to_add 
    add_final_amount_to_dict = input_dict["admin"]["total_cash"] = final_amount
    return add_final_amount_to_dict
    
def add_or_remove_cash(input_dict, amount_to_remove):
    final_amount_sub = input_dict["admin"]["total_cash"] + amount_to_remove
    remove_final_amount_from_dict = input_dict["admin"]["total_cash"] = final_amount_sub
    return remove_final_amount_from_dict

def get_pets_sold(input_dict):
    return input_dict["admin"]["pets_sold"]

def increase_pets_sold(input_dict, num_pets_sold):
    final_amount_pets = input_dict["admin"]["pets_sold"] + num_pets_sold
    add_final_amount_to_dict = input_dict["admin"]["pets_sold"] = final_amount_pets
    return add_final_amount_to_dict

def get_stock_count(input_dict):
    return len(input_dict["pets"])

def get_pets_by_breed(input_dict, breed):
    found_pet_by_breed = []
    for pet in input_dict["pets"]:
        if pet["breed"] == breed:
            found_pet_by_breed.append(pet)
    return pet_by_breed
    
def get_pets_by_breed(input_dict, breed):
    not_found_pet_by_breed = []
    for pet in input_dict["pets"]:
        if pet["breed"] == breed:
            not_found_pet_by_breed.append(pet)
    return not_found_pet_by_breed

def find_pet_by_name(input_dict, name):
    found_pet_by_name = None
    for pet in input_dict["pets"]:
        if pet["name"] == name:
            found_pet_by_name = pet
    return found_pet_by_name

def find_pet_by_name(input_dict, name):
    not_found_pet_by_name = None
    for pet in input_dict["pets"]:
        if pet["name"] == name:
            not_found_pet_by_name = pet
    return not_found_pet_by_name

def remove_pet_by_name(input_dict, name_to_remove):
    for pet in input_dict["pets"]:
        if pet["name"] == name_to_remove:
            input_dict["pets"].remove(pet)

def add_pet_to_stock(input_dict, pet_to_add):
    input_dict["pets"].append(pet_to_add)
    
def get_customer_cash(input_dict):
    return input_dict["cash"]

def remove_customer_cash(input_dict, remove_cash): 
    final_amount = input_dict["cash"] - remove_cash 
    remove_final_amount_from_dict = input_dict["cash"] = final_amount
    return remove_final_amount_from_dict

def get_customer_pet_count(input_dict):
    return len(input_dict["pets"])

def add_pet_to_customer(input_dict, pet_to_add):
    return input_dict["pets"].append(pet_to_add)

def customer_can_afford_pet(customer, pet):
    can_afford = None
    for potential_customer in customer:
        if customer["cash"] >= pet["price"]:
            can_afford = True
        else:
            can_afford = False
    return can_afford
            
            
    



    








    