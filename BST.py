
# values that are less than node value go to the left
# else > or = will go right

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if value is less than node value
        if value < self.value:

            # go left
            # determine if there is anything to left
            if not self.left:
                # base case
                # create new BST with value
                # make that value the left
                self.left = BST(value)

                # recursive case
            else:
                self.left.insert(value)

        # if value is > than or = to curr node value
        else:
            if not self.right:
                self.right = BST(value)

            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True

        elif value < self.value:
            if not self.left:
                return False

            else:
                self.left.contains(value)

        else:
            if not self.right:
                return False
            else:
                self.right.contains(value)
