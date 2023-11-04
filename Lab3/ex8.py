def loop(mapping):
    visited = set()
    result = []

    current_key = mapping.get('start') #returneaza valoarea asociata cheii 'start'

    while current_key is not None and current_key not in visited:
        result.append(current_key)
        visited.add(current_key)
        current_key = mapping.get(current_key)

    return result

def main():
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    result = loop(mapping)
    print(result)  


if __name__ == "__main__":
    main()