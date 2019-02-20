
# name
# avatar (profile picture)
# inventory
# 
class Character():
    # "dunder init"
    def __init__(self, new_name):
        # `self` is the customary way to refer to the instance being built
        # in other languages, they use `this`
        self.name = new_name