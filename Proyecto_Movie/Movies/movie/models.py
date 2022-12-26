from django.db import models

# Create your models here.

genero_status = [
    (1, 'Hombre'),
    (2, 'Mujer'),
    (3, 'Otro')
]

class Pelicula(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    comment = models.TextField()
    director = models.ForeignKey(
        'Director', 
        on_delete=models.CASCADE
        )
    actores = models.ManyToManyField(
        'Actor'
    )
    genero = models.ManyToManyField(
        'Genero'
    )
    imdb = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

class Actor(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    last_name = models.CharField(max_length=50)
    genero = models.IntegerField(choices=genero_status, null=False, blank=False)
    age = models.IntegerField()
    pais = models.ForeignKey(
        'Paises', on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.name}-{self.last_name}"

class Director(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    last_name = models.CharField(max_length=50)
    genero = models.IntegerField(choices=genero_status, null=False, blank=False)
    age = models.IntegerField()
    pais = models.ForeignKey(
        'Paises', on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

class Paises(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

class Genero(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.name}'

