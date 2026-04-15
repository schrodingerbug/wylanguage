var = None
var_name = None

def variable():
  global var, var_name
  var_name = input("Name your variable:")
  var = input(f"{var_name}-)")

def log():
 output = input(">>")
 if output != f"log<{var_name}>":
  print(output[5:-2])
 elif output == f"log<{var_name}>":
  print(var)

def boolean():
 value = input(">>")
 if value == f"{var_name}?={var}":
     print("True")
 elif value != f"{var_name}?={var}":
     print("False")

def maths():
    global var,var_name
    arithmetic = input(">>")
    print(eval(arithmetic))

while True:
    command = input(">>")
    if command == "variable":
        variable()
    elif command == "log":
        log()
    elif command == "boolean":
        boolean()
    elif command == "maths":
        maths()
    else:
        print("Invalid input.")
        break
