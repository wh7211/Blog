from django.db import models

# Create your models here.

class BlogPost(models.Model):
    """用户学习的主题"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title

