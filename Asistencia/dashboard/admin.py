from django.contrib import admin
from .models import User, Alumno, Profesor, Curso , Aula , Nota,Asistencia

admin.site.register(User)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Nota)
admin.site.register(Asistencia)


# Register your models here.
