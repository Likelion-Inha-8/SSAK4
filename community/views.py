from django.shortcuts import render, redirect, get_object_or_404
from .models import Feed, FeedComment, Photo

lat = "37.449403"
lng = "126.65346"
# Create your views here.
def home(request):
    global lat
    global lng
    lat = "37.449403"
    lng = "126.65346"
    feeds = Feed.objects
    return render(request, 'home.html', {'feeds' : feeds})

def profile(request):
    global lat
    global lng
    lat = "37.449403"
    lng = "126.65346"
    feeds = Feed.objects
    return render(request, 'profile.html',{'feeds':feeds})

def new(request):
    global lat
    global lng
    lat = "37.449403"
    lng = "126.65346"
    return render(request, 'new.html')

def map(request):
    feeds = Feed.objects
    global lat
    global lng
    return render(request, 'map.html',{'feeds':feeds, 'lat':lat ,'lng':lng})

def loc(request):
    if(request.method=='POST'):
        global lat 
        lat = request.POST['lat']
        global lng 
        lng = request.POST['lng']
    return redirect('map')

def createfeed(request):
    if(request.method=='POST'): 
        newfeed=Feed()
        newfeed.title=request.POST['title']
        newfeed.content=request.POST['content']
        newfeed.location=request.POST['search-bar']
        newfeed.lat=request.POST['lat']
        newfeed.lng=request.POST['lng']

        newfeed.writer = request.user
        newfeed.save()
        

        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.feed = newfeed
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
    return redirect('home')

def detail(request, feed_id):
    global lat
    global lng
    lat = "37.449403"
    lng = "126.65346"
    onepost=get_object_or_404(Feed,pk=feed_id)
    comments = onepost.feedcomment_set.all()
    return render(request,'detail.html',{'onepost':onepost, 'comments':comments})

def edit(request,feed_id):
    onepost=get_object_or_404(Feed,pk=feed_id)
    return render(request,'edit.html',{'onepost':onepost})

def feedupdate(request,feed_id):
    editfeed=get_object_or_404(Feed,pk=feed_id)
    editfeed.content=request.POST['content']
    editfeed.title=request.POST['title']
    editfeed.location=request.POST['location']
    editfeed.save()
    return redirect('/detail/'+str(feed_id))

def feeddelete(request,feed_id):
    deletefeed=get_object_or_404(Feed,pk=feed_id)
    deletefeed.delete()
    return redirect('home')

	
def commentcreate(req, feed_id):
    if (req.method == 'POST'):
        post = get_object_or_404(Feed, id=feed_id)
        post.feedcomment_set.create(content=req.POST['comment_content'])
    return redirect('/detail/'+str(feed_id))

    	
def commentdelete(req, feed_id, comment_id):  
    comment = get_object_or_404(FeedComment,id=comment_id,feed_id=feed_id)
    comment.delete()
    return redirect('/detail/'+str(feed_id))

