class BaseClass():
    num_base_calls = 0
    def call_me(self):
        print("Calling the base class")
        self.num_base_calls+=1

class LeftSubClass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling the left sub class")
        self.num_left_calls+=1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling right sub class")
        self.num_right_calls+=1

class SubClass(LeftSubClass,RightSubClass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling Sub class")
        self.num_sub_calls+=1
obj = SubClass()
obj.call_me()