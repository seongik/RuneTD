from game import classes

class RedTriangle (classes.Enemy):
    max_hp = 3
    reward = 1
    armour = 0
    
    move_speed = 0.1
    
    image_name = "Red triangle"
    
    def __init__(self, game):
        super(RedTriangle, self).__init__(game)

class BlueCircle (classes.Enemy):
    max_hp = 5
    reward = 1
    armour = 1
    
    move_speed = 0.15
    
    image_name = "Blue circle"
    
    def __init__(self, game):
        super(BlueCircle, self).__init__(game)

class PinkSquare (classes.Enemy):
    max_hp = 8
    reward = 1
    armour = 2
    
    move_speed = 0.2
    
    image_name = "Pink square"
    
    def __init__(self, game):
        super(PinkSquare, self).__init__(game)

class OrangeOctagon (classes.Enemy):
    max_hp = 10
    reward = 1
    armour = 4
    
    move_speed = 0.25
    
    image_name = "Orange octagon"
    
    def __init__(self, game):
        super(OrangeOctagon, self).__init__(game)