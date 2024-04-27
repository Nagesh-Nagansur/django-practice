from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    
    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username
   
class Post(models.Model):
    __tablename__ = "post"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"
    
    def __str__(self):
        return f"Post by {self.user.username} at {self.timestamp}"

class Comment(models.Model):
    __tablename__ = "comment"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"

class Like(models.Model):
    __tablename__ = "like"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "like"
    
    def __str__(self):
        return f"Like by {self.user.username} on {self.post}"

class Follow(models.Model):
    __tablename__ = "follow"
    follower = models.ForeignKey(User, related_name='follower_relationships', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed_relationships', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "follow"
    
    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username} since {self.timestamp}"
