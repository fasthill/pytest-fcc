class Country:
    """Super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')


class Korea(Country):
    """Sub Class"""

    def __init__(self, name1):
        self.name1 = name1

    def __eq__(self, other):
        print("other", other)

    def show_name(self):
        print('국가 이름은 : ', self.name1)

a = Korea('대한민국')
a.show_name()
print(a.name)
print(a.name1)
b = Korea('미국')
print(b.name)
print(b.name1)

print(a, b)