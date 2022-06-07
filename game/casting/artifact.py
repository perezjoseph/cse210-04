from game.casting.actor import Mineral

class Artifact(Mineral):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = self_message
class Player(Artifact):
    def __init__(self):
        super().__init__()
        self.points = 0
    def do_math(self):
        if self.gem.get('item') == '*':
            self.points += self.gem.get('value')
        else:
            self.points -= self.rock.get('value')
            print(self.rock.get('value'))