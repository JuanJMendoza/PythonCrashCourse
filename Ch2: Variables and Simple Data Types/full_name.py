first_name = "ada"
last_name = "lovelace"
# To insert a variable's value into a string, place the letter f immediately before the
# opening quotation mark. Put braces around the name or names of any variable you want
# to use inside your string. Python will replace each variable with its value when the
# is displayed. These strings are called f-strings. The f is for Format, because python
# formats the string by replacing the name of any variable in braces with its value. 
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
# Much simpler than printing out the literal value of the variable "message"
message = f"Hello, {full_name.title()}!"
print(message)
full_name2 = "Herro, {} {}!!".format(first_name, last_name)
print(full_name2.title())
"""
Adding Whitespace to Strings with Tabs or Newlines
"""
print("python")
print("\tPython!")
print("\nPython3!")