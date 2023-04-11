from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    # admin 페이지에서 좀 더 알아보기 쉽게 설정하는 코드
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]