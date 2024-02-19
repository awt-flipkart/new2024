my_list = ["theja",1,2,3]
my_list.append(4)
print(my_list)
my_list.remove(3)
print(my_list)
new_list = my_list + [5,6]
print(new_list)
sub_list = my_list[2:4]
print(sub_list)

def get_coordinates():
    return(3,4,"theja")

    x,y,z= get_coordinates()
    print(x)