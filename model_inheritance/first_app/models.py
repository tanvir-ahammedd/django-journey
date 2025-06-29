from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    father_name = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        return f"Name: {self.name}"
    
#abstract base class
class CommonInfoClas(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfoClas):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)

class TeacherInfoModel(CommonInfoClas):
    salary = models.IntegerField()
    
# Multitable inheritance
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=20)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
# Proxy Model inheritance
class Friend(models.Model): # friend is present in class
    school = models.CharField(max_length=30)
    section = models.CharField(max_length=10)
    attendance = models.BooleanField()
    hw = models.CharField(max_length=40)
    class Meta:
        ordering = ['id']

class Me(Friend): # Me is not present in class
    class Meta:
        proxy = True
        ordering = ['id']