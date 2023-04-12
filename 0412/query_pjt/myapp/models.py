from django.db import models

class PetSitter(models.Model):
    firts_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return f'집사{self.first_name}'

class Pet(models.Model):
    name = models.CharField(max_length=50)
    pet_sitter = models.ForeignKey(PetSitter, on_delete=models.CASCADE)

    def __str__(self):
        return f'펫{self.name}'


# Create your models here.
