def order_list(lst):
    return sorted(lst, key=lambda x: x[1][2])

def main():
    lst = [('abc', 'bcd'), ('abc', 'zza')]
    ordered_lst = order_list(lst)
    print(ordered_lst) 

if __name__ == "__main__":  
    main()