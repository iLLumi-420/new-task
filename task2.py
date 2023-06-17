user_profile_dict = {
    'name': 'John Doe',
    'age': 25,
    'email': 'johndoe@example.com',
    'gender': 'male',
    'address': '123 Main St'
}

validation_rules = {
    'name': {
        'required': True,
        'min_length': 1
    },
    'age': {
        'min_value': 18,
        'max_value': 99
    },
    'email': {
        'min_length': 5,
        'max_length': 50
    },
    'gender': {
        'valid_values': ['male', 'female']
    },
    'address': {
        'required': False,
        'max_length': 50
    }
}

def validate(dict, rules):
    for field, field_rules in rules.items():
        value = dict.get(field)
        
        for rule_name, rule_value  in field_rules.items():
            if rule_name == 'min_length':
                if len(value) < rule_value:
                    print(f'length should be minimun {rule_value}')
                    return False
            elif rule_name == 'max_length':
                if len(value) > rule_value:
                    print(f'length should be maximum {rule_value}')
                    return False
            elif rule_name == 'min_value':
                if value < rule_value:
                    print(f'value should be minimun {rule_value}')
                    return False
            elif rule_name == 'max_value':
                if value > rule_value:
                    print(f'value should be maximum {rule_value}')
                    return False
            elif rule_name == 'valid_values':
                if value not in rule_value:
                    print(f'{value} is not valid')
                    return False
            elif rule_name == 'required':
                if rule_value:
                    if value is None:
                        print(f'Required field')
                        return False
    
    return True

                

print(validate(user_profile_dict, validation_rules))