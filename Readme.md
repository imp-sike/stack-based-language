# Stack Based Language
Currently supported operations. Does not support floating points. 
(NOTE TO MYSELF: check SIMD instructions)

1. Direct Numbers
Inserts the number to the top of the stack.
    ```
        1 2 3 ## This puts the number 1, 2 and 3 in the stack
    ```

2. Arithmetic operations
Currently supports ADD operation (+) and SUBTRACT operation (-) only.
    ```
       1 3    ## Inserts 1 and 3  to stack
       +      ## Sums the inserted number and push the result to stack 
    ```

3. Logical operations
Supports >, <, ==, !=, >=, <=.
    ```
        1 1 
        ==   ## Checks whether two number are equal and puts the bool response to the stack
    ```

4. dup
Copies the top of stack and adds it to top of stack.

5. The print 
```
.                   ## pops the tos and prints it 
"Hello World" outs  ## prints the string  
```

6. The input
```
in             # Takes in user number input and push to tos
```

7. the if else statement
```
1 1 == if 
    "1 equals 1" outs
else
    "1 does not equals 1" outs
fi
```

8. The dup operation
```
32 dup . .
```
Output: 32 32

9. goto
```
    label@labelname
        ## code
        goto@labelname
```

10. functions
```
## Function can operate on stack data only
func@helloworld 
    "Hello World." outs
cnuf@helloworld

call@helloworld
```

11. store@ and read@ operation
```
    store@x  ## pop and stores in x variable
    push@x   ## pushes the value of x to stack
```

12. The almighty include/import/require 
```
    {path/to/filename.expr}
```