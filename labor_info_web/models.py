from django.db import models

class ContactRequest(models.Model):
    """Contact request data model"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_4_SSN = models.CharField(max_length=4)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return (f"{self.first_name} {self.last_name}")

class BlogPost(models.Model):
    """A blog post."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        """Return the blogs title and text. This might be incorrect"""
        return (f"{self.title} {self.text}")