greet="hello world,"

extended_greet="hello world," + " this is a long string"

extended2_greet=greet + "this is a long string"

print(extended_greet,extended2_greet) 

name="john"

intrupution= f"Hello {name}" 

greet_format="hello {}"

formatted=greet_format.format(name)

print(intrupution,formatted)
print(formatted.upper())
print(formatted.lower())
print(formatted.replace("john","paul"))