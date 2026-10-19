# IN THIS CHEAPTER WE WILL LEARN ABOUT EXCEPTION HANDLING:-
# EXCEPTION HANDLING:-
# ERRRORS:-
#         there are three types of errors
# 1. syntax error:-       ----> wrong syntax
# 2. indentation error:-  ----> bad spacing
# 3. tab error:-          ----> mixing tabs / spacing

# EXCEPTIONS:-
# 1.zeroErrorDivision
# 2.TypeError
# 3.valueError
# 4.FileNotFoundError

# KEYWORD:-
# TRY     --------> wrap the risky code
# EXCEPT  --------> handles the exceptions
# ELSE    --------> runs only if no exception occured
# FINALLY --------> always run - good for cleanup
# RAISE   --------> manually through your own exception

# FOR EXAMPLE:-
try:
    result = 10/0
except ZeroDivisionError:
    print("can't divide  by zero")
else:
    print("success", result)
finally:
    print("this always runs or prints")
