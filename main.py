from LabPrinter import LabPrinter

# Create LabPrinter instance with secret string "abc"
printer = LabPrinter("abc")  # Provide the required argument

# Function to call the correct method
def call_method_named(printer, method_name):
    if method_name == "print_2_plus_2":
        printer.print_2_plus_2()
    elif method_name == "print_secret":
        printer.print_secret()
    else:
        print(f"Unknown method: {method_name}")

# Call methods using call_method_named()
call_method_named(printer, "print_2_plus_2")
call_method_named(printer, "print_plus_2")  # Invalid method name
call_method_named(printer, "print_secret")
