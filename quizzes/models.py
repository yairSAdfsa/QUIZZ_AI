from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)  # Título del quiz
    description = models.TextField(blank=True, null=True)  # Descripción opcional
    created_at = models.DateTimeField(auto_now_add=True)  # Se guarda la fecha de creación

    def __str__(self):
        return self.title 