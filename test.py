from  privatebroker.privatebroker import privateclass, privatemethod



@privateclass
class A(object):
    """
    Базовый класс
    """
    def __init__(self, *args, **kwargs):
        self.some_one = {}
    
    
    @privatemethod
    def a_private2(self):
        pass
    
    
    @privatemethod
    def a_private(self, key, value):
        self.some_one[key] = value
    
    
    def test(self, x, y):
        private = self.broker(A, 'a_private')
        return private(self, x, y)
    
    
    def a_public(self):
        return self.some_one

#a = A()
#print(a.a_private())

@privateclass
class B(A):
    
    @privatemethod
    def b_private(self):
        return 'Я могу быть только у объекта B'
    
    def b_public(self):
        self.test('a', 11)
        return self.some_one


b = B()
print(b.b_public())


@privateclass
class C(A):
    
    @privatemethod
    def c_private(self):
        return 'Я могу быть только у объекта C'

    def c_public(self):
        return 'я метод класса C должен быть у всех наследников\n'


c = C()
#print(c.c_public())

@privateclass
class D(C):
    
    @privatemethod
    def d_private(cls):
        return 'Я могу быть только у объекта D'

    def d_public(self):
        #print(self.c_public())
        return 'я метод класса D должен быть у всех наследников\n'


#d = D()
#print(d.c_public())
#print(d.d_public())

class E(D):
    def e_method(self):
        print(self)
        return 'я метод класса E и просто нследуюсь от D'



e = E()
#print(e.e_method())