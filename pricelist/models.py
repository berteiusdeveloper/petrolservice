from django.db import models

class ProductCategory(models.Model):
    item_no = models.IntegerField()
    title = models.CharField(max_length=300, default='Измеритель объема')
    info = models.CharField(max_length=600, default='Измеритель объема. Важная деталь ТРК. Служит для определения выдаваемого количества (дозы, объема) топлива.Большинство объемомеров – поршневого типа.')
    img = models.ImageField(upload_to='product', blank=True)
    def __str__(self):
        return self.title

class ServiceCategory(models.Model):
    item_no = models.IntegerField()
    title = models.CharField(max_length=300, default='Газоотделитель')
    def __str__(self):
        return self.title


class Production(models.Model):
    item_no = models.IntegerField()
    #type_p = models.CharField(max_length=300, default='Измеритель объема')
    type_p = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    cost = models.FloatField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=300)
    type_s = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    cost = models.FloatField()
    cost_weekend = models.FloatField()

    def __str__(self):
        return self.title
