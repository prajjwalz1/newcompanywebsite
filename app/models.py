from django.db import models
from django.db import models
import datetime
from PIL import Image
import io
from django.core.mail import send_mail
from django import forms
class slide(models.Model):
    title = 'slideinfo'
    shortinfo=models.CharField(max_length=300)
    slogan=models.CharField(max_length=300)
    youtubewatch = models.URLField()
    logo=models.ImageField(upload_to='projects/')
    
    def __str__(self):
        return self.title
class aboutus(models.Model):
    title='about us'
    summary = models.CharField(max_length=300)
    Points=models.CharField(max_length=200)
    Learnmore=models.CharField(max_length=1000)
    

    def __str__(self):
        return self.title


class why_choose_us (models.Model):
    title="Why to choose us"
    summary = models.CharField(max_length=500)
    tagline=models.CharField(max_length=100)
    
        
    def __str__(self):
        return self.title

class points(models.Model):
        
        point=models.CharField(max_length=100)
        pointdescribe = models.CharField(max_length=300)
        def __str__(self):
            return self.point

class services (models.Model):
    title='Our service'
    summary=models.CharField(max_length=200)
    service_name=models.CharField(max_length=100)
    icon_name=models.CharField(max_length=20, null=True)
    service_summary = models.CharField(max_length=200)
    def __str__ (self):
     return self.title;




class portfolio(models.Model):
    title='portfolio'
    summary=models.CharField(max_length=200)
    image=models.ImageField(upload_to='projects/')
    link=models.URLField(null=True)

    def save(self, *args, **kwargs):
        # Open the image using Pillow
        image = Image.open(self.image)

        # resize the image to the desired dimensions
        image = image.resize(( 200, 200))

        # Save the cropped image to a buffer
        buffer = io.BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)

        # Save the buffer to the ImageField
        self.image.save(self.image.name, buffer, save=False)

        # Save the rest of the model
        super().save(*args, **kwargs)
    def __str__ (self):
     return self.title;


class OurTeam(models.Model):
    title='Team'
    summary=models.CharField(max_length=400)
    Full_name = models.CharField(max_length=50,null=True)

    position=models.CharField(max_length=30)
    image=models.ImageField(upload_to='projects/',null=True)
    comments=models.CharField(max_length=200)
    def save(self, *args, **kwargs):
        # Open the image using Pillow
        image = Image.open(self.image)

        # resize the image to the desired dimensions
        image = image.resize(( 200, 200))

        # Save the cropped image to a buffer
        buffer = io.BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)

        # Save the buffer to the ImageField
        self.image.save(self.image.name, buffer, save=False)

        # Save the rest of the model
        super().save(*args, **kwargs)
    def __str__ (self):
     return self.title;

class OurTeam2(models.Model):
    title='Team'
    summary=models.CharField(max_length=400)
    Full_name = models.CharField(max_length=50,null=True)

    position=models.CharField(max_length=30)
    image=models.ImageField(upload_to='projects/',null=True)
    comments=models.CharField(max_length=200)
    def save(self, *args, **kwargs):
        # Open the image using Pillow
        image = Image.open(self.image)

        # resize the image to the desired dimensions
        image = image.resize(( 200, 200))

        # Save the cropped image to a buffer
        buffer = io.BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)

        # Save the buffer to the ImageField
        self.image.save(self.image.name, buffer, save=False)

        # Save the rest of the model
        super().save(*args, **kwargs)
    def __str__ (self):
     return self.title;

class contact(models.Model):
    name = models.CharField(max_length=255,null=True)
    summary=models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=255,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    map_url = models.URLField(null=True)

    def __str__(self):
        return self.name

