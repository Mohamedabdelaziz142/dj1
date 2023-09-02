from django.db import models
from django.utils import timezone

category_choices =(
 ('WB','Web Developments'),
 ('DB','Desktop Developments'),
  ('DS','Data Science')
)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    create_at = models.DateTimeField(default = timezone.now)
    published = models.BooleanField(default=True)
    email = models.EmailField(default="test@gmail.com",max_length=250)
    views = models.IntegerField(default=0)
    category = models.CharField(choices=category_choices, max_length=30,default='WB')



    def __str__(self):
        return self.title
