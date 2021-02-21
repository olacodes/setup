from django.db import models
<<<<<<< HEAD
import uuid


class User(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  username = models.CharField(max_length=50, null=False, unique=True)
  email = models.EmailField(null=False, unique=True)
  password = models.CharField(max_length=100, null=False)
  is_moderator = models.BooleanField(default=False)
  is_superadmin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.username

  # def get_fullname(self):
  #   return self.first_name + self.last_name


class Thread(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255, null=False)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title


class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
      return self.post

=======

# Create your models here.
>>>>>>> 8f811f21e88cf729b6c7c9ccd17ee4f39534d193
