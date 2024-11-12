
class JSS():
    def __init__(self):
        print("JSS!")

a=JSS()

출력: JSS!

class JSS():
    def __init__(self):
        print("JSS!")
    
    def show(self):
        print("JSS02")

a = JSS()  
a.show()

 출력: JSS02

class JSS():
    def __init__(self):  # self=a
        self.name = input("이름:")
        self.age = input("나이:")
    def show(self):
        print("이름 {},나이{}".format(self.name, self.age))

a = JSS()
a.show()

a.이름: ,a.나이:

class JSS():
    def __init__(self):  # self=a
        self.name = input("이름:")
        self.age = input("나이:")
    def show(self):
        print("이름 {},나이{}".format(self.name, self.age))

class JSS2(JSS):
    def__init__(self):# 기존 무시 새 init 시작
        super().__init__()
        self.gender = input("성별: ")
    def show(self):
        print("이름 {},나이{}, 성별{}".format(self.name, self.age, self.age))
        







### encode_labels

def encode_labels(*args):
    le = LabelEncoder()
    return [le.fit_transform(arg) for arg in args]


### encode_labels + numpy

def encode_labels(*args, to_numpy=False):
    le = LabelEncoder()
    encoded_lists = [le.fit_transform(arg) for arg in args]
    
    if to_numpy:
        return [np.array(encoded) for encoded in encoded_lists]
    
    return encoded_lists