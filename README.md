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

\nWe will use rfk classes, and create new classes that use inheritance.

This class will move the object (gems and rocks)
\+ flyingObject => cast

This class will define the attributes of the rocks and gems
\+ Mineral => actor 
	<br>Gems int
	<br>Rocks int
	<br>Set_Value()
	
Will set the score on the screen

\+ Player => actor
		<br>score int
		<br>sumScore()

	
	