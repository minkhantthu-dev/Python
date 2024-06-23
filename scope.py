# Variable scope

name = "Khant thu hein" # Global variable


def sayMyname() :
    # Local variable
    global name;
    name = "Khant thu"  # overwrite
    print(name);
    
sayMyname();

print(name); 
