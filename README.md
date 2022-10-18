A linked list class which acts almost identically to the built-in list class with the exception of being... linked.
### Summary of implemented actions:
#### Init
`linkedlist(*iterable)`  
    - Create a new linked list optionally from a preexisting iterable such as a list or another linked list  
#### Methods
`.append(value)`  
    - Add a value to the end  
`.push(value)`  
    - Add a value to the start  
`.insert(index, value)`  
    - Add a value to any index  
`.extend(iterable)`  
    - Add an iterable to the end  
`.copy()`  
    - Create a shallow clone  
`.count(value)`  
    - Count the occurences of a value  
`.index(value, *start, *end)`  
    - Find the first index of a value searching from start to end  
`.remove(value)`  
    - Remove the first index of the item  
`.pop(index)`  
    - Remove the item at index  
`.sort(*key)`  
    - Sort the list with optional swap check function  
#### Arithmatic
`+ iterable`  
    - Append the iterable to the end  
`* int`  
    - Copy the list multiple times  
`+= iterable`  
    - Append the iterable to the end then set  
`*= int`  
    - Copy the list multiple times then set  
