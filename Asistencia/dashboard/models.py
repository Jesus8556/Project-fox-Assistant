from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.username
class Alumno(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + " " + self.lastname

class Profesor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    email = models.EmailField()
    speciality = models.CharField(max_length=200)
    celular = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.lastname

class Aula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cycle = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name
class Curso(models.Model):
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    def __str__(self) :
        return self.name

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200)
    note = models.IntegerField()
    def __str__(self) :
        return self.activity
    
class Asistencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    state = models.CharField(max_length=1)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.state

    
    