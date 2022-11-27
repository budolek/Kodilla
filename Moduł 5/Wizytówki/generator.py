from operator import concat
from string import capwords
from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    
    def __init__(self, name, surname, privphone, email):
        self.name = name
        self.surname = surname
        self.privphone = privphone
        self.email = email
    
    def __str__(self):
        return f"\n{self.name} {self.surname} \n tel: {self.privphone}\n e-mail: {self.email}"
        
    def contact(self):
        return f"Wybieram numer +48{self.privphone} i dzwonię do {self.name} {self.surname} \n *****"
     
    @property
    def lebel_lenght(self):
        return sum([len(self.name), len(self.surname)])
             
class BusinessContact(BaseContact):
    def __init__(self, job, company, bissphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.bissphone = bissphone
        
    def __str__(self):
        return f"\n{self.name} {self.surname} \n {self.job} \n {self.company} \n tel: {self.bissphone}"
    
    def contact(self):
        return f"Wybieram numer służbowy +48{self.bissphone} i dzwonię do {self.name} {self.surname} \n*****"    
    
    @property
    def lebel_lenght(self):
        return sum([len(self.name), len(self.surname)])
             
    

def create_contacts(kind, how_many):
    cards = []
    for i in range(how_many):
        if kind == "b":
            cards.append(BusinessContact(name = fake.first_name(), surname = fake.last_name(), privphone = fake.phone_number(), email = fake.email(), job = fake.job(), company=fake.company(), bissphone=fake.phone_number())) 
        elif kind == "p":
            cards.append(BaseContact(name = fake.first_name(), surname = fake.last_name(), privphone = fake.phone_number(), email = fake.email()))
        elif kind != ("b" and "p"):
            print("Nobody expects the Spanish Inquisition!")
            break
    return cards
    
if __name__ == '__main__':

    kind = input("Jaki rodzaj wizytówki chcesz wygenerować:\n b - biznesowa;\n p - prywatna \n")
    how_many = int(input("Ile wizytówek chcesz wygenerować: \n"))
    cards = create_contacts(kind, how_many) 

for i in cards:
    print(i, f"\n Długość znaków imienia i nazwiska to: {i.lebel_lenght}\n")
    print(i.contact())    

