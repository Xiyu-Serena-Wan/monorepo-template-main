# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

In the SL, the names of the dictionary and list member functions correlate to what they actually do. A good name of a function makes the function more self-explaining. No extra comments is needed. Users can understand what the function does without dig into the actual code.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A list is an ordered data structure. Lists are mostly implemented by arrays. Each element in a list has an index. Users can access to a random element quickly via the index. Whereas a dictionary is an unordered data structure of key-value pairs. Dictionaries are implemented by hash tables. The element in a dictionary does not have an corresponding index. Instead, a value has a key. 

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, a list allows for random access, but the index has to be in bound. In Java, it means that the index has to be bigger than or equal to 0 and smaller than or equal to the length of the list minus 1.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Pros: Codes can be reused for multiple data types. It is very adaptable.

Cons: Users needs to be more cautious because there might be data type related errors.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

The functions are well named in the Request module. The functions all have very clear intentions of what they need to do, and one function only does one thing, which makes naming and using them easier. For example, for get(), the function simply gets the result of a given url.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

I did find some functions that have a lot of parameters. Like this one: resp = s.send(prepped, stream=stream, verify=verify, proxies=proxies, cert=cert, timeout=timeout).

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

**kwargs is a syntax in a function's argument part. It means that the number of keyword arguments is optional. Putting this in a function makes the function more flexible and extensible. However, the function then needs to parse the keyword arguments, and they might not fit the rule. The user also needs to find out what those arguments do in a function, which means the functions with **kwargs are less readable and straightforward. 

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Arguments that have the default value of None means that they are optional arguments. They can be customized by the user. Arguments can be set to values other than None. It depends on the purpose of the arguments. Setting the arguments to values give users a clear guideline of what the arguments' jobs are. 
