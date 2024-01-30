from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import UserDetailsModel, UserFollowModal, UserLikePost, allPostModal, postModal, allCommenDetailstModal
import datetime

# Create your views here.
def registeration_page(req):
    return render(req,'registration_page.html')


def register_user(req):
    new_user=UserDetailsModel(
        umobile_email=req.POST['umobile_email'],
        ufull_name=req.POST['ufull_name'],
        user_name=req.POST['user_name'],
        upassword=req.POST['upassword']
    )
    new_user.save()
    req.session['user_id']=new_user.id
    return redirect('/')


def do_login(req):
    user=UserDetailsModel.objects.filter(
        umobile_email=req.POST['lmobile_username_email'],
        upassword=req.POST['lpassword']
    )
    if(len(user)>0):
        req.session['user_id']=user[0].id
        return redirect('/')
    else:
        return HttpResponse("<script>history.back();</script>")
def login_page(req):
    return render(req,'login_page.html')


def mymodel(req):
    post_det=allPostModal.objects.get(id=req.GET['post_id'])
    comment_detalils=allCommenDetailstModal.objects.filter(post_det=req.GET['post_id'])
    islike = ""
    # isfollow=""
    post_id = req.GET.get('post_id')
    user_id = req.session.get('user_id')
    if post_id is not None and user_id is not None:
        matchrec3 = UserLikePost.objects.filter(post_id=post_id, user_id=user_id)
        matchrec4=UserFollowModal.objects.filter(follow_user_id=req.session['user_id'],follow_id=post_det.post_user_det.id)       
        if matchrec3.exists():
            islike = "Yes"
        if matchrec4.exists():
             isfollow = "Yes"
        else:
            islike = "No"
            isfollow = "No"
    else:
        islike = "No" 
        isfollow = "No"
    
    obj={
        "isfollow":isfollow,
        "islike":islike,
        "post_det":post_det,
        "comment_detalils":comment_detalils
    }
    return render(req,'comment_model.html',obj)


def home_page(req):
    if (req.session.has_key('user_id')):
        ruid=req.session['user_id']
        user_det=UserDetailsModel.objects.filter(id=ruid)
        # all_posts=allPostModal.objects.all().order_by('-id')
        all_posts=allPostModal.objects.all()
        for row in all_posts:
            matchrec = UserLikePost.objects.filter(user_id=req.session['user_id'],post_id=row.id)
            if matchrec:
                row.islike = "Yes"
            else:
                row.islike = "No"
        for row in all_posts:
            matchrec = UserFollowModal.objects.filter(follow_user_id=req.session['user_id'],follow_id=row.post_user_det.id)
            if matchrec:
                row.isfollow = "Yes"
            else:
                row.isfollow = "No"
        post_count=len(all_posts)
        obj={
            'user':user_det,
            "all_posts":all_posts,
            "post_count":post_count,
            }
        return render(req,'home_page.html',obj)
    else:
        return redirect('/login_page')


def log_out(req):
    del req.session['user_id']
    return redirect('/login_page')


def profile_page(req):
    if (req.session.has_key('user_id')):
        ruid=req.session['user_id']
        user_det=UserDetailsModel.objects.filter(id=ruid)
        user_posts=allPostModal.objects.filter(post_user_det=ruid)
        total_post=len(user_posts)
        obj={
            'user':user_det,
            'user_posts':user_posts,
            'total_post':total_post
            }
        return render(req,'profile_page.html',obj)
    else:
        return redirect('/login_page')
    

def edit_profile(req):
    if (req.session.has_key('user_id')):
        ruid=req.session['user_id']
        user_det=UserDetailsModel.objects.filter(id=ruid)
        obj={'user':user_det}
        return render(req,'edit_profile.html',obj)
    else:
        return redirect('/login_page')


def save_edited_user(req):
    post=False
    if 'uphoto' in req.FILES:
        post=True
    bio=False
    if 'ubio' in req.POST:
        bio=True
    postdet=UserDetailsModel.objects.get(id=req.session['user_id'])
    gender=postdet.ugender
    if 'ugender' in req.POST:
        gender=req.POST['ugender']     
    uid=req.session['user_id']
    user_updated=UserDetailsModel.objects.get(id=uid)
    user_updated.ufull_name=req.POST['ufull_name']
    user_updated.user_name=req.POST['user_name']
    if post:
        user_updated.uphoto=req.FILES['uphoto']
    if bio:
        user_updated.ubio=req.POST['ubio']
    user_updated.ugender=gender
    user_updated.save()
    return redirect('/')


def add_post(req):
    newpost=postModal(
        upost=req.FILES['post1']
    )
    newpost.save()
    filedet=newpost.id
    req.session['post_det']=filedet
    return HttpResponse("done") 
  

def add_detail_of_post(req):
    if ((req.session.has_key('user_id')),(req.session.has_key('post_det'))):
        ruid=req.session['user_id']
        user_det=UserDetailsModel.objects.filter(id=ruid)
        pid=req.session['post_det']
        postdet=postModal.objects.filter(id=pid)
        obj={
            'user':user_det,
            'post1':postdet
            }
        return render(req,'add_post.html',obj)
    else:
        return redirect('/') 


def final_post_save(req):
    date=datetime.datetime.now()
    post_date=date.strftime("%d-%m-%y")
    caption=" "
    if(req.POST['post_caption']):
        caption=req.POST['post_caption']
    tag=" "
    if(req.POST['post_tag']):
        tag=req.POST['post_tag']
    location=" "
    if(req.POST['post_location']):
        location=req.POST['post_location']
    pid=req.session['post_det']
    postdet=postModal.objects.get(id=pid)
    uphoto=postdet.upost
    save_post=allPostModal(
        post_user_det=UserDetailsModel.objects.get(id=req.session['user_id']),
        post_caption=caption,
        post_location=location,
        post_tag=tag,
        post_time=post_date,
        post_photo=uphoto,
        post_likes=0,
        post_comment=0
    )
    save_post.save()
    req.session['post_det']=0
    return redirect('/')


def canclePost(req):
    pid=req.session['post_det']
    postModal.objects.get(id=pid).delete()
    del req.session['post_det']
    return redirect('/')


def view_profile_of_frind(req):
    if (req.session.has_key('user_id')):
        ruid=req.GET['id']
        user_det=UserDetailsModel.objects.filter(id=ruid)
        user_posts=allPostModal.objects.filter(post_user_det=ruid)
        total_post=len(user_posts)
        obj={
            'user':user_det,
            'user_posts':user_posts,
            'total_post':total_post
            }
        return render(req,'view_profile_of_frind.html',obj)
    else:
        return redirect('/login_page')


def save_comment(req):
    date=datetime.datetime.now()
    post_date=date.strftime("%d-%m-%y")
    post_commenthb=allPostModal.objects.get(id=req.GET['post_id'])
    post_commenthb.post_comment=post_commenthb.post_comment+1
    post_commenthb.save()
    save_new_comment=allCommenDetailstModal(
        post_det=allPostModal.objects.get(id=req.GET['post_id']),
        pComment=req.GET['comment'],
        comment_time=post_date,
        comment_likes=0,
        who_comment=UserDetailsModel.objects.get(id=req.session['user_id'])
    )
    save_new_comment.save()  


def add_like(req):
    matchrec=UserLikePost.objects.filter(user_id=req.session['user_id'],post_id=req.GET['post_id'])
    if matchrec:
        return HttpResponse("Already Like")
    else:
        add_like=allPostModal.objects.get(id=req.GET['post_id'])
        add_like.post_likes+=1
        add_like.save()
        ins = UserLikePost()
        ins.user_id = UserDetailsModel.objects.get(id=req.session['user_id']) 
        ins.post_id = allPostModal.objects.get(id=req.GET['post_id'])
        ins.save()
        return HttpResponse("Done")


def remove_like(req):
    UserLikePost.objects.filter(user_id=req.session['user_id'],post_id=req.GET['post_id']).delete()
    add_like=allPostModal.objects.get(id=req.GET['post_id'])
    add_like.post_likes-=1
    add_like.save()
    return HttpResponse("Done")


def add_follow(req):
    matchrec=UserFollowModal.objects.filter(follow_user_id=req.session['user_id'],follow_id=req.GET['follow_id'])
    if matchrec:
        print("Already Follow")
        return HttpResponse("Already Follow")
    else:
        add_followw=UserDetailsModel.objects.get(id=req.GET['follow_id'])
        add_followw.ufollowers +=1
        add_followw.save()
        ins = UserFollowModal()
        ins.follow_user_id = req.session['user_id']
        ins.follow_id = UserDetailsModel.objects.get(id=req.GET['follow_id'])
        ins.save()
    print("Follow "+req.GET['follow_id'])
    return HttpResponse("Done")


def remove_follow(req):
    print("Unfollow " +req.GET['follow_id'])
    UserFollowModal.objects.filter(follow_user_id=req.session['user_id'],follow_id=req.GET['follow_id']).delete()
    remove_followw=UserDetailsModel.objects.get(id=req.GET['follow_id'])
    remove_followw.ufollowers -=1
    remove_followw.save()
    return HttpResponse("Done")
