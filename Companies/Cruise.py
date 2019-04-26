# The textboxes library should implement the following API:
#
#    box = TextBox("hello", "+")
#    box.show()
#    +++++++++
#    + hello +
#    +++++++++
#
# By default, text is padded with one space on each side.

# Please implement the following TextBox padding API
#
# paddedRight()
# =============
# Add support for a paddedRight() method on the TextBox
# class that works as follows:
#
#    TextBox box = TextBox("hello", "+")
#    TextBox object = box.paddedRight(4)
#    object.show()
#
#    box.show()
#    +++++++++++++
#    + hello     +
#    +++++++++++++
#    +++++++++
#    + hello +
#    +++++++++
#
# paddedBelow()
# =============
# Add support for a paddedBelow() method that works as shown
# below:
#
#    box = TextBox("hello", "+")
#    box.paddedBelow(3).show()
#    +++++++++
#    + hello +
#    +       +
#    +       +
#    +       +
#    +++++++++
#
# Calling paddedRight() or paddedBelow() should not mutate
# the original box object.
class Textbox():
    def __init__(self, str1, str2, right, below):
        self.str1 = str1
        self.str2 = str2
        self.right = right
        self.below = below

    def show(self):
        j = ""
        padfielf = (" " * self.right)
        s = self.str2 + " " + self.str1 + padfielf + " " + self.str2
        nxt = self.str2 + " " + (" " *len(self.str1))+ padfielf + " " + self.str2
        length = len(s)

        print(self.str2 * length)
        print(s)
        for i in range(self.below):
            print(nxt)
        print(self.str2 * length)
        return

    def paddedRight(self, padded):
        right = padded
        return Textbox(self.str1, self.str2, right, self.below)

    def paddedBelow(self, padded):
        below = padded
        return Textbox(self.str1, self.str2, self.right, below)


box = Textbox("hello", "+", 0, 0)
box.paddedRight(4).show()
box.paddedBelow(4).show()
box.show()
box1 = Textbox("hello", "+", 0, 0)
box1.paddedBelow(3).paddedRight(2).show()