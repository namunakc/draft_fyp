from django.db import models

# Create your models here.
class Package(models.Model):
    package_name = models.CharField(max_length=1000, null=True)
    package_desc = models.TextField(null=True)
    number_of_people = models.PositiveIntegerField(null=True)
    no_days = models.PositiveIntegerField(null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.package_name
        

# class Booking_Details(models.Model):
#     package = models.ForeignKey(Package,null=True, no_delete = models.SET_NULL)
#     # user = models.ForeignKey(User,null=True, no_delete= models.SET_NULL)
#     phone_no = models.CharField(max_length=1000, null=True)

#     def __str__(self):
#         return self.package.package_name

