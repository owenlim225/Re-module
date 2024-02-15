# Re-module

Develop a comprehensive program for regular expression, where users can choose from a variety of options: a) utilize a string scanner, b) eliminate negativity from strings, or c) extract substrings. Each option seamlessly integrates with its corresponding function for efficient execution.

**str_scanner().** 
    Ask the user to input a string and check if the string starts with a small letter and ends with a non=digit and non-letter character using regex. If the string meets these conditions, print "Valid string!" Otherwise, print "Invalid string."
    
    sample outpu1
    
    enter a string: The quick brown fox jumps over the lazy dog.
    invalid string.
    
    Smaple output 2 
    enter a string: this is how we do it. 
    Valid string!


**re_nega().**
    Ask the user to input a paragprah. Using regex, replace the negative words hate, angry, bully, punch, and rant with "-". Print the updated paragraph
    
    Sample output 1
    Enter a pargarph: I hate you
    Updated pargraph: I - you
    
    Sample output 2:
    Enter a apragraph: I hate being in a place full of builly
    UPdated pargarph: I - being - in a place full of -

**sub_string()**
    Ask the user to input two string, a and b. check if b exist in a using regex. If b exist in a, print "{b} found in {a}!" Otherwise print "{b} not found in {a}"
    
    Sample output 1
    Enter a string a: helloworld
    Enter a string b: hello
    hello found in helloworld!
    
    Sample output 2 
    Enter a string a: Happy Birthday
    Enter a string b: valentine
    valentine not found in Happy Birthday
    
    Sample output 3
    Enter a string a: Elevator
    Enter a string b: ele
    ele not found in Elevator

