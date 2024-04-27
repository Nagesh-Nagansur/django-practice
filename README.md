# django-practice

Models:

User: Represents users of the platform with attributes like username, email, password, profile picture, etc.

Post: Represents user posts with attributes like content, timestamp, likes, comments, etc.
Comment: Represents comments on posts with attributes like content, timestamp, commenter, etc.

Like: Represents likes on posts, linking users to posts they liked.
Friendship: Represents friendships between users, indicating which users are friends with each other.

Follow: Represents followership, where users can follow other users to see their posts.
Relationships:

One-to-Many:
Each user can have many posts.
Each post can have many comments.
Each post can have many likes.

Many-to-Many:
Users can be friends with many other users.
Users can follow many other users, and each user can have many followers.

Functionality:
Users can create an account, log in, and log out.
Users can create, edit, and delete posts.
Users can like and comment on posts.
Users can send friend requests to other users, which can be accepted or rejected.
Users can follow/unfollow other users to see their posts in their feed.
Users can view their own profile, as well as profiles of other users.
User authentication and authorization to manage access to the system.