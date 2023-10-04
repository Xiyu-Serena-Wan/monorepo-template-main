**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Draw Smoothness

**Primary Actor**: User

**Goal in Context**: To test if a pixel color will change wherever the mouse is located when the mouse is pressed and a user left-clicks.

**Preconditions**: The program must be running and in a responsive state.

**Trigger**: Left-clicking the mouse.
  
**Scenario**: A user will left-click the mouse when they want to draw something.

**Exceptions**: The program may become potentially unresponsive. In this case, the program can be terminated from the operating system.

**Priority**: High-priority.

**When available**: First release

**Channel to actor**: The primary actor communicates through the mouse. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: We may need to implement 'intelligent drawing' functionality in the future, and revise this use case.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
