from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SubSubject(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    yr_group = models.CharField(max_length=50)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subsubject_id = models.ForeignKey(SubSubject, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_id.username} on {self.post_id.title}"


class Resource(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.FileField(upload_to='resources/')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title