user_profile_dict = {
    'name': 'ab',
    'age': 25,
    'email': 'johndoe@example.com',
    'gender': 'male',
    'address': '123 Main St',
    'phone': '9861601060'
}

validation_rules_array = [
    {
        'field': 'name',
        'rules': [
            {'name': 'min_length', 'value': 3},
            {'name': 'required', 'value': True},
            {'name': 'type', 'value': str},
        ]
    },
    {
        'field': 'age',
        'rules': [
            {'name': 'min_value', 'value': 18},
            {'name': 'type', 'value': int},
            {'name': 'max_value', 'value': 99}
        ]
    },
    {
        'field': 'email',
        'rules': [
            {'name': 'type', 'value': str},
            {'name': 'min_length', 'value': 5},
            {'name': 'max_length', 'value': 50}
        ]
    },
    {
        'field': 'gender',
        'rules': [
            {'name': 'type', 'value': str},
            {'name': 'valid_values', 'value': ['male', 'female']}
        ]
    },
    {
        'field': 'phone',
        'rules': [
            {'name': 'type', 'value': str},
            {'name': 'length', 'value': 10},
        ]
    },
    {
        'field': 'address',
        'rules': [
            {'name': 'required', 'value': False},
            {'name': 'type', 'value': str},
            {'name': 'max_length', 'value': 50}
        ]
    },
]


def validate(dict, rules):
    for field_rules in rules:
        field = field_rules['field']
        value = dict.get(field)
        
        for rules  in field_rules['rules']:
            rule_name = rules['name']
            rule_value = rules['value'] 

            if rule_name == 'type':
                if type(value) != rule_value:
                    print('Type error')
                    return False       
            
            if rule_name == 'min_length':
                if len(str(value)) < rule_value:
                    print(f'length should be minimun {rule_value}')
                    return False
            elif rule_name == 'max_length':
                if len(str(value)) > rule_value:
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
                        print(f'Required field is empty')
                        return False
            elif rule_name == 'length':
                if len(str(value)) != rule_value:
                    print(f'Phone number length should be {rule_value}')
                    return False
    
    return True

                

print(validate(user_profile_dict, validation_rules_array))