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
    
    def __str__(self):
        return f"Name: {self.name}"
    class Meta:
        ordering = ['id']

class Me(Friend): # Me is not present in class
    class Meta:
        proxy = True
        ordering = ['id'] 
        
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email = models.CharField(max_length=20)

# one to one relationship
class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete=models.CASCADE)
    pass_number = models.IntegerField()
    pages = models.IntegerField()
    validity = models.IntegerField()

# many to one relationship
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=50)
    
#many to many relationship
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=20)
    def __str__(self):
        return f"Name: {self.name}"
    class Meta:
        ordering = ['id']

class Teacher(models.Model):
    student = models.ManyToManyField(Student)
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ", ".join([str(i) for i in self.student.all()])