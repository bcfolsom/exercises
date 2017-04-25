class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person, self.name))

    def contact_info(self):
        print('{}\'s contact information: email: {}; phone: {}'.format(self.name, self.email, self.phone))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
sonny.greet('Jordan')
jordan.greet('Sonny')
sonny.contact_info()
jordan.contact_info()
