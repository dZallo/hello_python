# Variables

my_string_variable = "My String Variable"
print("Variable:", type(my_string_variable),"- ",my_string_variable)

my_int_variable = 5
print("Variable:", type(my_int_variable),"- ",my_int_variable)

my_int_to_str_variable= str(my_int_variable)
print("Variable int_to_str:",type(my_int_to_str_variable),"- ",my_int_to_str_variable)

my_bool_variable = False
print("Variable:", type(my_bool_variable),"- ",my_bool_variable)

my_list_variable = ["Texto1","Texto2"]
print("Variable:", type(my_list_variable),"- ",my_list_variable)

my_dict_variable = {"name":"Daniel", "username": "dZallo"}
print("Variable:", type(my_dict_variable),"- ",my_dict_variable)

print(my_string_variable, str(my_int_variable), my_bool_variable) # Print with different arguments(concatenation)

print("len() with list function: ", len(my_list_variable))
print("len() with string function: ", len(my_string_variable))# The len function also counts the spaces in a string

# Variables in a line
name, surname, nickname, age ="Daniel", "Zallo", "DanZ", 27
print("Person:",name,surname,str(age) + ".","NickName: ",nickname)

# Inputs, method to insert something from terminal
name= input('What is your name?: ')
age= input('How old are you?: ')
print(name)
print(age)

#cambiamos los tipos
name=35
age="Dani"
print(name)
print(age)

address: str = "My address"
print(type(address))