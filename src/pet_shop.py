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
    