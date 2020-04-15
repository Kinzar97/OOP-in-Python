class Person:
    def __init__(self, n, s, qual=1):
        self.name = n
        self.surname = s
        self.qualification = qual

    def return_info(self):
        info = self.name + ' ' + self.surname + ' ' + str(self.qualification)
        return info

    def __del__(self):
        print('Good bye, mr. ' + str(self.name) + ' ' + str(self.surname))


n1 = Person('Igor', 'Zaripov', 7)
n2 = Person('Fedor', 'Smolov', 5)
n3 = Person('Igor', 'Akinfeev')

print('1: ' + n1.return_info())
print('2: ' + n2.return_info())
print('3: ' + n3.return_info(), end='\n\n')

select = input('Choose number of a weak link: ')

if select == 1:
    del n1
elif select == 2:
    del n2
elif select == 3:
    del n3

input('Enter anything for exit...')
