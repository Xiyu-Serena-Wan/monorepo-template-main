# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
    - I think MObject is an abstract class, because it has a method __init__ that is not instantiated.
2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
    - When called, this method will destroy the instance and release the memory.
3. What class does Texture inherit from?
    - Texture class inherits from Image class.
4. What methods and attributes does the Texture class inherit from 'Image'? 
    - The Texture class inherits all the attributes and methods from 'Image'. The methods include: __init__(self, w, h), getWidth(self), getHeight(self), getPixelColorR(self, x, y), getPixels(self), and setPixelsToRandomValue(self). The attributes include: m_width, m_height, m_colorChannels, and m_Pixels.
5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
    - I think a texture should have a 'is-a' relationship with 'Image'. Having a 'is-a' relationship means that Texture is a type of 'Image' with some properties added or modified. It makes sense because a texture can be a type of images. If the relationship is 'has-a', then it means there will be an attribute in 'Texture' that has the type of 'Image', which could be less intuitive. 
6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
    - Yes. the 'Texture' class inherits the 'Image' class's constructor.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singletons in Python thread safe? Why or why not?
- Singletons in Python are not thread safe. It is always possible that a thread thinks that there is no existing instance then starts to create one. However, if another thread does the same thing before the above-mentioned instance is stored, then there will be two instances and this program does not follow singleton design pattern anymore.
 
  
