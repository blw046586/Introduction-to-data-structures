# Introduction-to-data-structures
Step 1: Produce correct output
Three commented-out lines of code exist in main.py. Uncomment the lines and click the Run button. Verify that the program's output is:

2 + 2 = 4
Unknown method: print_plus_2
Secret string: "abc"


Click the "Submit for grading" button to submit your code to the auto-grader. The auto-grader will run two tests against the submitted code: a "Compare output" test and a "Unit test".

The submission will pass the "Compare output" test because the program's output matches the expected output. Passing the test achieves 1 of the 10 possible points.

The "Unit test" fails because the LabPrinter object created in the main program code was not used. Steps that follow outline how to use the LabPrinter object to satisfy this lab's requirements and achieve 10/10 points.


Step 2: Inspect the LabPrinter class
Inspect the LabPrinter class implemented in the LabPrinter.py file. Methods print_2_plus_2() and print_secret() print strings using Python's print() function.


Step 3: Implement call_method_named()
Remove the three uncommented lines from the main program code. Then implement the call_method_named() function in main.py to handle three cases:

If method_name is "print_2_plus_2", call printer's print_2_plus_2() method.
If method_name is "print_secret", call printer's print_secret() method.
If method_name is anything other than the two strings mentioned above, print "Unknown method: xyz", where xyz is method_name's value.
After implementing call_method_named(), click the Run button. Verify that the program's output is, once again:

2 + 2 = 4
Unknown method: print_plus_2
Secret string: "abc"

Step 4: Submit code for 10/10 points
Once call_method_named() is properly implemented, submitting the code should receive 10 out of 10 points. The program's output is exactly the same as the implementation from step 1. But step 3's implementation uses the LabPrinter object and step 1 does not.


Step 5: Understand the difference
The unit test uses a different implementation of LabPrinter than what's shown in LabPrinter.py. Calls to each method are tracked, so the unit test determines whether or not call_method_named() was actually implemented according to lab requirements.

Most labs in this book are similar. Program output matters, but how the output is achieved matters more. Functions to implement will commonly require use of an object passed as an argument.


