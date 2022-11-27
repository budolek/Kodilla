from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, name, surname, privphone, e_mail):
        self.name = name
        self.surname = surname
        self.privphone = privphone
        self.e_mail = e_mail
    
    def __str__(self):
        return f"\n{self.name} {self.surname} {self.company} {self.job} {self.e_mail}"
        
    def privcontact(self):
        return f"\nWybieram numer +48{self.privphone} i dzwonię do {self.name} {self.surname}"
    
    def workcontakt(self):
        return f"\nWybieram numer +48{self.bissphone} i dzwonię do {self.name} {self.surname}"      
    
    @property
    def lebel_lenght(self):
        return sum([len(self.name), len(self.surname)])
             
class BusinessContact(BaseContact):
    def __init__(self, job, company, bissphone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.bissphone = bissphone
        
   
ludz = BusinessContact(name = fake.first_name(), surname = fake.last_name(), privphone = fake.phone_number(), e_mail = fake.free_email(), job = fake.job(), company = fake.company(), bissphone = fake.phone_number())     

print(ludz)   
print(ludz.privcontact())
print(ludz.workcontakt())
print(ludz.lebel_lenght)
