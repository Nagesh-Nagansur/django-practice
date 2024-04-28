from instagram.app.models import User
from instagram.app.models import Post, Comment, PostLike, CommentLike, Follow




all_users = User.objects.all()
print(all_users)
# ==============================================
user = User.objects.get(username="naruto")
print(user)
# ==============================================
users_with_username = User.objects.filter(username="some_username")
# ==============================================
user_posts = Post.objects.filter(user=user)

# ==============================================
users = User.objects.filter(username__in=["user1", "user2"])
posts = Post.objects.filter(user__in=users)

# ==============================================
from datetime import datetime
start_date = datetime(2022, 1, 1)
posts_after_date = Post.objects.filter(created_at__gte=start_date)

# ==============================================
posts_with_content = Post.objects.filter(content__contains="keyword")

# ==============================================
post_comments = Comment.objects.filter(post=post)

# ==============================================
user_comments = Comment.objects.filter(user=user)

# ==============================================
post_likes = PostLike.objects.filter(post=post)

# ==============================================
user_likes = PostLike.objects.filter(user=user)

# ==============================================
user_followers = Follow.objects.filter(followed=user)

# ==============================================
user_following = Follow.objects.filter(follower=user)

# ==============================================
mutual_followers = Follow.objects.filter(follower=user, followed=user)

# ==============================================
likes_count = PostLike.objects.filter(post=post).count()

# ==============================================
# ==============================================
