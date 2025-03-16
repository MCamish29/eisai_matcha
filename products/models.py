from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.category 

class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=75)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.country

class Tea(models.Model):

    class Meta:
        verbose_name_plural = 'Tea'

    product_id = models.AutoField(primary_key=True)
    internal_name = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250, null=True, blank=True)    
    description = models.TextField()
    blend = models.TextField()
    weight = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country_of_origin = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.internal_name

class Equipment(models.Model):

    class Meta:
        verbose_name_plural = 'Equipment'

    product_id = models.AutoField(primary_key=True)
    internal_name = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country_of_origin = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.internal_name

class Kit(models.Model):
    product_id = models.AutoField(primary_key=True)
    internal_name = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.internal_name