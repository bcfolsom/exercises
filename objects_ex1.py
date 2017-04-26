class Person:
    greeting_count = 0
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.num_unique_people_greeted = 0
        self.unique = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person, self.name))
        self.greeting_count += 1

        if other_person not in self.unique:
            self.unique.append(other_person)
            self.num_unique_people_greeted += 1

    def print_contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone))

    def add_friend(self, other):
        self.friends.append(other)

    def num_friends(self):
        print(len(self.friends))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', [])
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])
sonny.greet('Jordan')
# jordan.greet('Sonny')
sonny.greet('Jordan')
# jordan.greet('Sonny')
sonny.greet('Jordan')
sonny.greet('Brad')
sonny.greet('Josh')
# jordan.greet('Sonny')
# sonny.print_contact_info()
# jordan.print_contact_info()
# print(sonny.email, sonny.phone)
# print(jordan.email, jordan.phone)
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# jordan.add_friend(sonny)
# print(len(jordan.friends))
# jordan.num_friends()
print(sonny.greeting_count)
print(jordan.greeting_count)
print(sonny.num_unique_people_greeted)
