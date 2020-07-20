from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Acara(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()

    def __str__(self):
        return str(self.judul)

class Bagian(models.Model):
    divisi = models.CharField(max_length=200)
    deskripsi = models.TextField()
    acara = models.ForeignKey(Acara, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.divisi)

class Tugas(models.Model):
    DONE = 'done'
    PENDING = 'pending'

    TASK_STATUS = (
        (DONE, 'Done'),
        (PENDING, 'Pending'),
    )

    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    tgl_dibuat = models.DateTimeField()
    batas_tgl = models.DateTimeField()
    bagian = models.ForeignKey(Bagian, on_delete=models.CASCADE)
    tugas_untuk = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default=PENDING)
    komentar = models.TextField(null=True, blank=True)
    attachment_file = models.FileField(upload_to='attachment_file/', blank=True, null=True)

    def __str__(self):
        return str(self.judul)