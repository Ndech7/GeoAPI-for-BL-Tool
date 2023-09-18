from django.contrib.gis.db import models
class Sites(models.Model):
    name = models.CharField(max_length=200)
    area_name = models.CharField(max_length=200)
    landuse_class = models.CharField(max_length=100)
    orientation = models.CharField(max_length=10)
    location = models.PointField()
    photo = models.ImageField(upload_to='pics')

    class Meta:
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.name


