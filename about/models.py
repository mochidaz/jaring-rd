from django.db import models


class Circle(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    master = models.CharField(max_length=100)
    est_year = models.CharField(max_length=10)
    description = models.TextField()
    key_members = models.TextField(help_text="Pisahkan dengan koma")
    theme_color = models.CharField(max_length=20, default="#8a1c1c", help_text="Kode Hex warna border")

    def __str__(self):
        return self.name
