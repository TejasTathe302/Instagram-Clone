from django.db import models

# Create your models here.
class UserDetailsModel(models.Model):
    umobile_email=models.CharField(max_length=200)
    ufull_name=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    upassword=models.CharField(max_length=200)
    uphoto=models.ImageField(upload_to='static/uploaded/profile_potos/')
    ubio=models.CharField(max_length=200)
    ugender=models.CharField(max_length=200)
    uwebsite=models.CharField(max_length=200)
    ufollowers=models.IntegerField()
    ufollowings=models.IntegerField()

class postModal(models.Model):
    upost=models.ImageField(upload_to='static/uploaded/posts')

class allPostModal(models.Model):
    post_user_det=models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE)
    post_photo=models.ImageField(upload_to='static/uploaded/posts')
    post_caption=models.CharField(max_length=200)
    post_location=models.CharField(max_length=200)
    post_tag=models.CharField(max_length=200)
    post_time=models.CharField(max_length=200)
    post_comment=models.IntegerField()
    post_likes=models.IntegerField()
    

class UserLikePost(models.Model):
    post_id = models.ForeignKey(allPostModal,on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE)

class UserFollowModal(models.Model):
    follow_user_id = models.IntegerField()
    follow_id = models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE)

class allCommenDetailstModal(models.Model):
    post_det=models.ForeignKey(allPostModal,on_delete=models.CASCADE)
    pComment=models.CharField(max_length=255)
    comment_time=models.CharField(max_length=200)
    comment_likes=models.IntegerField()
    who_comment=models.ForeignKey(UserDetailsModel,on_delete=models.CASCADE)




