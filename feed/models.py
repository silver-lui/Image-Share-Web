from django.db import models
from sorl.thumbnail import ImageField
from django.conf import settings

class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()

    @property
    def img_path(self):
        return f"./media/{self.image.name}"

    def __str__(self):
        return self.text
