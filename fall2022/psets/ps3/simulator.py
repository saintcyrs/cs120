# Simulator file for question 1.
# Fill in the implementation of the different commands of the simulator.
# You can use `tests.py` to run your simulator on some prewritten RAM programs.

from collections import defaultdict

variableList = []
# Note: defaultdict works exactly the same as a normal Python dictionary except it returns a default 
#       value (in this case, 0) when accessing a key that is not defined rather than raising KeyError.
#       We are using a dictionary rather than a list/array to manage the memory so that we don't need to 
#       initialize and store memory cells that are never accessed by the RAM program.
memory = defaultdict(int)

# Creates the variable list and the memory dictionary.
# Initializes the 0th variable, input_len, to be the first element of the program array.
def setupEnv(programArr, inputArr):
    variableList.clear()
    memory.clear()

    # Initialize the list of variables to be a list of zeroes.
    for i in range(programArr[0]):
        variableList.append(0)
    
    # Make input_len the 0th variable in the variable list.
    variableList[0] = len(inputArr)
    # Put in memory each item of input array. 
    for i in range(len(inputArr)):
        memory[i] = inputArr[i]
        
# Runs the given RAM program on the input.
def executeProgram(programArr, inputArr):
    # Sets up the environment. 
    setupEnv(programArr, inputArr)
    # Create a new dimension of programArr to be just the lines of code (ignoring variables). 
    programArr = programArr[1:]

    programCounter = 0
    while programCounter < len(programArr):
        # Store the command and the list of operands.
        cmd = programArr[programCounter][0]
        ops = programArr[programCounter][1:]
        
        # Assignment commands
        if cmd == "read":       
            # ['read', i, j]: lookup the var_j location in memory and assign that value to var_i                    
            variableList[ops[0]] = memory[variableList[ops[1]]]
        if cmd == "write":
            # ['write', i, j]: store the value of var_j in memory at the location var_i 
            memory[variableList[ops[0]]] = variableList[ops[1]]
        if cmd == "assign":
            # ['assign', i, j]: assign var_i to the value j
            variableList[ops[0]] = ops[1]
            
        # Arithmetic commands
        if cmd == "+":
            # ['+', i, j, k]: compute (var_j + var_k) and store in var_i
            variableList[ops[0]] = variableList[ops[1]] + variableList[ops[2]]
        if cmd == "-":
            # ['-', i, j, k]: compute max((var_j - var_k), 0) and store in var_i.
            variableList[ops[0]] = max((variableList[ops[1]]-variableList[ops[2]]), 0)

        if cmd == "*":
            # ['*', i, j, k]: compute (var_j * var_k) and store in var_i.
            variableList[ops[0]] = variableList[ops[1]] * variableList[ops[2]]

        if cmd == "/":
            #  ['/', i, j, k]: compute (var_j // var_k) and store in var_i.
            # Note that this is integer division. You should return an integer, not a float.
            # Remember division by 0 results in 0.
            if variableList[ops[2]] == 0:
                variableList[ops[0]] = 0
                break
            variableList[ops[0]] = variableList[ops[1]] // variableList[ops[2]]
            
        # Control commands
        if cmd == "goto":
            # ['goto', i, j]: if var_i is equal to 0, go to line j
            if variableList[ops[0]] == 0:
                programCounter = ops[1] - 1
        
        programCounter += 1
    
    # Return the memory starting at output_ptr with length of output_len
    return [memory[i] for i in range(variableList[1], variableList[1]+variableList[2])]
