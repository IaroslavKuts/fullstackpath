from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Display_Manager(models.Manager):
    def receive_person_relatives(self, username):
        #old_version. not in use
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                            SELECT person_name, person_surname, person_age, person_sex, person_family_status, person_country
                            FROM familytree_parents WHERE belongs_to_user_id = '{username}'
                            UNION SELECT person_name, person_surname, person_age, person_sex, person_family_status, person_country FROM familytree_grand_parents WHERE belongs_to_user_id = '{username}'
                            UNION SELECT person_name, person_surname, person_age, person_sex, person_family_status, person_country FROM familytree_siblings WHERE belongs_to_user_id = '{username}'
                            UNION SELECT person_name, person_surname, person_age, person_sex, person_family_status, person_country FROM familytree_siblings WHERE belongs_to_user_id = '{username}'""".format(username = username))
            relatives_list = []
            for row in cursor.fetchall():
                relatives_list.append(row)
        return relatives_list
    
    def receive_person_relatives2(self, username):
        parents = ('Parents', Parents.objects.filter(belongs_to_user = username).values_list())
        grand_parents = ('Grand_parents', Grand_Parents.objects.filter(belongs_to_user = username).values_list())
        siblings = ('Siblings', Siblings.objects.filter(belongs_to_user = username).values_list())
        spouse = ('Spouse', Spouse.objects.filter(belongs_to_user = username).values_list())
        
        relatives_tuple = (parents, grand_parents, siblings, spouse)

        return relatives_tuple


class Person(models.Model):
       
  
    person_name = models.CharField(max_length=128)
    person_surname = models.CharField(max_length=128)
    person_birthdate = models.DateField(max_length=16, default = None)
    person_sex = models.CharField(max_length=12, choices = settings.SEX_CHOICES)
    person_family_status = models.CharField(max_length=10, choices = settings.REL_CHOICES)
    person_country = models.CharField(max_length=128)
    belongs_to_user = models.ForeignKey(User, on_delete =  models.CASCADE , to_field ='username')
    
    objects = Display_Manager()
    
    class Meta:
            abstract = True



class Parents(Person):
    pass
    
class Siblings(Person):
    pass

class Grand_Parents(Person):
    pass

class Spouse(Person):
    pass

