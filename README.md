# cse210-04
# Overview 
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

# Rules
- Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem they earn a point.
- If the player touches a rock they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

# New Classes 

We will use rfk classes, and create new classes that use inheritance.

##### This class will be the new director class and will control the logic of the game
Contributors: Joseph Perez, Daniel Parra 
```
+ flyingObject => Director
```
Direct the game with a different logic
##### This class will call timer to move objects and hadle score
```
Contributors: Daniel Parra, Joseph Perez
+Player => actor 
	sub()
	sumScore()
	wrap()
```
Limit wrap and add score
##### This class will define the attributes of the rocks and gems
	Conhtributors: Joseph Perez
```
timer => keyboardService
	 move()
```

##### This class has been modified to achieve our needs
	Contributors: Daniel Parra
``` 
+Point
	equals()	
```
Added a range for the robot, so it does't have to be too precise to catch a gem

Cleaning the code contributions:

Jonathan Uribe
Thomas Villalobos