
# name
# avatar (profile picture)
# inventory
# 
class Character():
    # "dunder init"
    def __init__(self, new_name, new_avatar):
        # `self` is the customary way to refer to the instance being built
        # in other languages, they use `this`
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
# Someone=None is a default argument where `None`
# is equivalent to `null` in other languages 
    def greet(self, someone=None):
        if someone:
            return "Hello, %s I am %s, I am awesome." % (someone.name, self.name)
        else:
            return "Hello I am %s, I am awesome." % (self.name)

class Monster(Character):
    def greet_hero(self, someone):
        return "mruahh. I want to eat you. I mean...hello %s, I am %s. I am terrible" % (someone.name, self.name)
        

class Hero(Character):
        pass
