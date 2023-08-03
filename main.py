def mini(number):
    min_number = min(number)
    return min_number
def add_number(addition , mini_number):
    addition.append(mini_number)
    return addition
    
def remove_number(number, mini_number):
    number.remove(mini_number)
    return number
    
    
def main():
    number = [4,6,5,1,3,2]
    sorted_number = []
    while True:
        if(len(number) > 0):
            print(add_number(sorted_number , mini(number)))
            remove_number(number , mini(number))
        elif(len(number) == -1):
            break
main()