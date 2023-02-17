str=input("enter a string:")
def swap(st):
    start=str[0]
    end=str[-1]
    sw_str=end+str[1:-1]+start
    print(sw_str)
swap(str)