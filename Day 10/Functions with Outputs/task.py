def capitalizing_names(f_name, l_name):
    sorted_name_f = f_name.title()
    sorted_name_l = l_name.title()
    return f"{sorted_name_f} {sorted_name_l}"

print(capitalizing_names(input("What is your name? "),  input("What is your las name? ")))




