
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

    def greet(self):
        return "Hello I am %s, I am awesome." % (self.name)
