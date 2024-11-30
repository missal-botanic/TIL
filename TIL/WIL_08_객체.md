객체
```
변수, 속성, 함수, 메서드 를 포함하는 커스텀 자료구조
객체는 구체적인 것의 유일한 인스턴스를 나타낸다.
객체는 명사, 메서드는 동사

새 객체를 만들기 위해서 'class'를 정의

문자열은 내장된 class
```

```py

class Cat: # 빈 class
    pass

class Cat():
    pass

a_cat = Cat()
another_Cat = Cat()

a_cat
>>> <__main__.Cat at 0x2f15c255840> # 변경가능
```

```py
a_cat = Cat() # a_cat이 Cat 클래스의 인스턴스로, type(a_cat)은 Cat 클래스를 출력합니다.
>>> <class '__main__.Cat'>

a_cat = Cat # a_cat이 Cat 클래스 자체로, type(a_cat)은 type을 출력합니다. 이는 모든 클래스가 type의 인스턴스이기 때문입니다.
>>>  <class 'type'>
```

```
속성은 클래스는 객체 내부의 변수이다. 
속성은 보통 객체 속성을 의미한다.
```

```py
a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_Cat

a_cat.age
>>> 3
a_cat.name
>>> 'Mr. Fuzzybuttons'
a_cat.nemesis
>>> <__main__.Cat at 0x2f15c255840>
```

```py
class Cat:
    def __init__(self): # self는 다른 객체를 만들기 위해서 필요함
        pass


class Cat: # 클래스 정의 찾는다, 메모리에 새 객체를 초기화(생성)한다.
    def __init__(self, name): # 메서드(생성자) __init__ 호출, 생성된 객체를 self에 전달, 인수('Grumpy')를 name(속성)에 전달
        self.name = name # 새 객체를 반환

furball = Cat('Grumpy') # 변수(furvall)에 객체를 연결
furball.name
>>> 'Grumpy'
```
```py
class Monster:
    def __init__(self, name):
        self.name = name
    def say(self):
        print(f'나는 {self.name}')

shark = Monster('상어')
wolf = Monster('늑대')

shark.say()
wolf.say()
>>>
'나는 상어'
'나는 늑대'

class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f'나는 {self.name} {self.age}입니다.')

shark = Monster('상어', 18)
wolf = Monster('늑대', 24)

shark.say()
wolf.say()
>>>
'나는 상어 18입니다.'
나는 늑대 24입니다.'


```
```
클래스: 설계도(이름과 속성, 동작 등을 정의해 놓은 템플릿)

객체 : 설계도로 부타 만든 제품

속성(변수) : 클래스안의 변수

메서드 : 클래스안의 함수(class 안의 .~~ 은 메서드가 아님)

생성자 : 객체를 만들 때 가장 먼저 실행되는 함수(__init__)

인스턴스 : 메모리에 살아있는 객체 (객체(인스턴스))

한개의 설계도로 여러 제품 만들 수 있음

(변수(객체)):객체참조
객체 참조는 변수를 가르키는 것

()는 생성자와 관련 되어 있다.
객체 = 클래스이름() # shark = Monster()
객체.의 메서드() # shark.say()
```
상속
```
기존 클래스 : 부모, 슈퍼, 베이스
새 클래스 : 자식, 서브, 파생
```

```py
class Car(): # 부모 클래스
    pass

class Yugo(Car): # 자식 클래스
    pass

issubclass(Yugo, Car)# 다른 클래스에서 파생 되었는지 확인
>>> True
```
메서드 오버라이드
```py
class Car(): # 부모 클래스
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car): # 자식 클래스
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
>>> I'm a Car!

give_me_a_yugo.exclaim() # 상속의 의미가 없다
>>> I'm a Car! 


class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self): # 부모 클래스의 메서드를 덮어 씌운다.
        print("I'm a Yuga! Much like a Car, but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
>>> I'm a Car!

give_me_a_yugo.exclaim() 
>>> I'm a Yuga! Much like a Car, but more Yugo-ish.

```

```py
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name): # 자식 내용으로 덮는다.
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name): # 자식 내용으로 덮는다.
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
>>> 'Fudd'

print(doctor.name)
>>> 'Doctor Fudd'

print(lawyer.name)
>>> 'Fudd, Esquire'
```
메서드 추가
```py
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push() # 새 메서드 존재
>>> 'A little help here?'

give_me_a_car.need_a_push() # 부모는 새 메서드가 없다
>>> '오류'
```

부모에게 도움 받기

```py
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email): 
        super().__init__(name) # 부모 클래스 정의를 얻는다.
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapple.com')

bob.name
>>> 'Bob Frapples'

bob.email
>>> 'bob@frapple.com'
```
다중 상속
```py
class Animal:
    def says(self): # 하위에 says가 없다면 작동
        return 'I speak!'

class Horse(Animal):
    def says(self): # 먼저 호출된 쪽을 출력
        return 'Neigh!'

class Donkey(Animal):
    def says(self): # 먼저 호출된 쪽을 출력
        return 'Hee-haw!'

class Mule(Donkey, Horse): # 엄마, 아빠 중 엄마를 호출 없을시 아빠
    pass

class Hinny(Horse, Donkey): # 엄마, 아빠 중 엄마를 호출 없을시 아빠
    pass

Mule.mro()
>>> '[__main__.Mule, __main__.Donkey, __main__.Horse, __main__.Animal, object]'

Hinny.mro()
>>> '[__main__.Hinny, __main__.Horse, __main__.Donkey, __main__.Animal, object]'

mule = Mule()
hinny = Hinny()

mule.says()
>>> 'Hee-haw!'

hinny.says()
>>> 'Neigh!'
```
