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
    pet_by_breed = []
    for pet in input_dict["pets"]:
        if pet["breed"] == breed:
            pet_by_breed.append(pet)
    return pet_by_breed
    
   
    
    