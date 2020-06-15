class Person:
    name = "이름이란, 사람이 공통적으로 가지는 속성"
    age = "나이란, 내가 태어나서 죽을때까지의 기간"

    
    def greeting(self):
        return f'{self.name}이 인사합니다. 안녕하세요!'


    def aging(self):
        return f'{self.name}은 {self.age}살 입니다.'

    @classmethod
    def pppp(cls):
        return f'{cls.name}이다. 야발'

p1 = Person()
print(p1.name)
print(p1.greeting())
print(p1.aging())
print(Person.pppp())
print(p1.pppp())