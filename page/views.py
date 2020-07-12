from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

# Create your views here.
def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers})

def introduce(request):
    return render(request, 'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})

def new(request) :
    return render(request, 'new.html')

def create(request) :
    if request.method == 'POST' :
        post = Designer()

    if 'image' in request.FILES :
        post.image = request.FILES['image']
    post.name = request.POST['name']
    post.address = request.POST['address']
    post.description = request.POST['description']

    post.save()
    return redirect('detail', post.id)

def update(request, designer_id) : 
    post = get_object_or_404(Designer, pk = designer_id)

    if request.method == "POST" :
        if 'image' in request.FILES :
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()
        return redirect('detail', post.id) #수정 결과를 바로 보여주기 위함 #자동으로 경로 찾아갈 수 있음

    else : #post가 아닌 다른 method를 처리하기 위함
        return render(request, 'update.html', {'designer' : post}) #post를 보내는 이유는 기존에 입력한 정보를 띄워놓은 상태에서 수정하게 하기 위함.

def delete(request, designer_id) :
    post = get_object_or_404(Designer, pk = designer_id) 
    post.delete()

    return redirect('home')