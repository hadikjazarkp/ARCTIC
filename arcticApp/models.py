from django.db import models


from django.db import models

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption if self.caption else f"Image {self.id}"



# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='countries/')
    description = models.TextField()


    def __str__(self):
        return self.name
    

class ProductCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    url_name = models.CharField(max_length=100)  # Store the name of the URL pattern

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(self.url_name)

class SiteLogo(models.Model):
    image = models.ImageField(upload_to='site_logo/')

    def __str__(self):
        return "Site Logo"


class Founder(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='founders_images/')
    description_1 = models.TextField()
    description_2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name






class Review(models.Model):
    name = models.CharField(max_length=100)  # Name of the reviewer or review title
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)# Image associated with the review
    description = models.TextField()  # Detailed description of the review

    def __str__(self):
        return self.name  # Returns the name as the string representation of the model
 
 


class TravelReview(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)  # Use ImageField to handle image uploads
    description = models.TextField()
    job_title = models.CharField(max_length=100, blank=True, null=True)  # New field for the job title
    location = models.CharField(max_length=100, blank=True, null=True)  # New field for the location

    def __str__(self):
        return self.name
    
    
class DisplayImage(models.Model):
    image = models.ImageField(upload_to='display_images/')
    alt_text = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.alt_text 
 
 
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name




class StudyReview(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)  # Use ImageField to handle image uploads
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)  # New field for the location

    def __str__(self):
        return self.name
 
 

class MediaReview(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)  # Use ImageField to handle image uploads
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)  # New field for the location

    def __str__(self):
        return self.name 
    

class laundryReview(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)  # Use ImageField to handle image uploads
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)  # New field for the location

    def __str__(self):
        return self.name    

class healthReview(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)  # Use ImageField to handle image uploads
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)  # New field for the location

    def __str__(self):
        return self.name    
    
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    contact_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
    

class Education(models.Model):
    EDUCATION_TYPE_CHOICES = [
        ('abroad', 'Abroad Education'),
        ('distance', 'Distance Education'),
        ('domestic', 'Domestic Education'),
    ]

    education_name = models.CharField(max_length=255)
    education_type = models.CharField(max_length=10, choices=EDUCATION_TYPE_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='education_images/')

    def __str__(self):
        return f"{self.education_name} ({self.get_education_type_display()})"
    
    
class ContentBO(models.Model):
    heading = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, help_text="Use emoji or icon code")
    paragraph = models.TextField()
    online_text = models.CharField(max_length=255)

    def __str__(self):
        return self.heading


class ShoeCleaningService(models.Model):
    SERVICE_TYPES = [
        ('polishing', 'Polishing'),
        ('deep_cleaning', 'Deep Cleaning'),
        ('premium_cleaning', 'Premium Cleaning'),
        ('regular_cleaning', 'Regular Cleaning')  # Added Regular Cleaning
    ]
    
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    description1 = models.CharField(max_length=255)
    description2 = models.CharField(max_length=255, blank=True, null=True)
    description3 = models.CharField(max_length=255, blank=True, null=True)  # Corrected max_length
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.get_service_type_display()
    
    


class ShoeService(models.Model):
    SERVICE_CHOICES = [
        ('deep_cleaning', 'Deep Cleaning'),
        ('shoe_polishing', 'Shoe Polishing'),
        ('odor_removal', 'Odor Removal'),
        ('waterproofing', 'Waterproofing'),
    ]

    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.get_service_type_display()    
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/')
    badge = models.CharField(max_length=100)
    misc_info = models.CharField(max_length=100)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])    
    



class MediaContent(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    name = models.CharField(max_length=200)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    media_file = models.FileField(upload_to='media/')
    description = models.TextField()
    item = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='media_contents')

    def __str__(self):
        return self.name    
    
    
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to {self.question}"    
    
    
class AlertImage(models.Model):
    image = models.ImageField(upload_to='alerts/')    
    
    

class HealthHeaderImage(models.Model):
    image = models.ImageField(upload_to='header_images/')
    alt_text = models.CharField(max_length=100, default='header')

    def __str__(self):
        return self.alt_text


class ClassImage(models.Model):
    image = models.ImageField(upload_to='class_images/')
    alt_text = models.CharField(max_length=100, default='class')
    css_class = models.CharField(max_length=50, default='class__img-1')

    def __str__(self):
        return self.alt_text    
    
class HealthImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title    