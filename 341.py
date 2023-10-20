class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.my_list = []
        self.position = 0
        self.reduce(nestedList)
    
    def reduce(self, old_list):
        for i in old_list:
            if i.isInteger():
                self.my_list.append(i)
            else:
                self.reduce(i)

    def next(self) -> int:
        return_value = self.my_list[self.position]

        self.position += 1

        return return_value
    
    def hasNext(self) -> bool:
        if len(self.my_list) == self.position:
            return False
        
        return True