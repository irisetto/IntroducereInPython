def validate_dict(rules, input_dict):
    #ca sa nu existe chei diferite de cele din rules
    for dict_key in input_dict.keys():
        if all(key != dict_key for key, _, _, _ in rules):
            return False
        
    for key, prefix, middle, suffix in rules:  
        #ca sa nu existe chei  care nu apar in dictionar
        if key not in input_dict:
            return False

        value = input_dict[key]
        if not value.startswith(prefix) or not value.endswith(suffix):
            return False

        middle_start = value.find(middle)
        if middle_start == -1 or middle_start == 0 or middle_start == len(value) - len(middle):
            return False

    return True

def main():
    rules = {("key1", "come", "inside", "out"), ("key2", "start", "middle", "winter")}
    data = {"key1": "come inside, it's too cold out", "key3": "startmiddlewinter"}
    result = validate_dict(rules, data)
    print(result)  


if __name__ == "__main__":
    main()