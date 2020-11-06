# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(input_dictionary):
    result = input_dictionary["name"]
    return result

def get_total_cash(input_dictionary):
    return input_dictionary["admin"]["total_cash"]

def add_or_remove_cash(input_dict, amount_to_add):
    final_amount = input_dict["admin"]["total_cash"] + amount_to_add
    return final_amount
    
