def compare_dict(dict1, dict2):
    if dict1.keys() != dict2.keys():
        return False

    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        if type(value1) == dict and type(value2) == dict:
            if not compare_dict(value1, value2):
                return False
        elif value1 != value2:
            return False
#+liste
    return True


def main():
    dict_a = {'teo': 1, 'barca': {'c': 5, 'd': [4, 4]}}
    dict_b = {'teo': 1, 'barca': {'c': 5, 'd': [4, 4]}}
    dict_c = {'teo': 1, 'b': {'c': 5, 'd': [4, 4]}}

    result1 = compare_dict(dict_a, dict_b) 
    result2 = compare_dict(dict_a, dict_c)  

    print(result1)
    print(result2)


if __name__ == "__main__":
    main()