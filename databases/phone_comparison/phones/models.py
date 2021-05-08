from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    os = models.TextField()
    processor = models.TextField()
    memory = models.TextField()
    ram = models.TextField()
    ppi = models.TextField()

    def __str__(self):
        return self.name


class iPhone(models.Model):
    five_g_tech = models.TextField()
    double_cam = models.TextField()
    wireless_charge = models.TextField()

    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)


class Samsung(models.Model):
    memory_card = models.TextField()
    fingerprint_scan = models.TextField()
    geomagnetic_sensor = models.TextField()
    wireless_charge = models.TextField()

    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)


class Xiaomi(models.Model):
    memory_card = models.TextField()
    dictaphone = models.TextField()
    fingerprint_scan = models.TextField()
    flashlight = models.TextField()

    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)