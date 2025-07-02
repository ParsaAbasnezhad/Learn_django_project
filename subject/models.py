from django.db import models


class OrganicChemistry(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Organic_chemistry/')
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title


class InorganicChemistry(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Inorganic_chemistry/')
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title


class PhysicalChemistry(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Physical_chemistry/')
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title


class Physics(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Physics/')
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title


class Mathematics(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Mathematics/')
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title
