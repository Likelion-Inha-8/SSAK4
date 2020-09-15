from django.db import models

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    Like_Num = models.IntegerField(default=0) #좋아요 개수
    Like = models.BooleanField(default=0) #해당 피드 좋아요 눌렀는지 O/X

    def __str__(self):
       	return self.content

class FeedComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    feed_id = models.ForeignKey(Feed, on_delete=models.CASCADE)

class Photo(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)