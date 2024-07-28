from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    color = models.CharField(max_length=6)  # hex

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Role: {self.name}>"
