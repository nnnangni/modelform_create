from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def create(request):
    if request.method == "POST":
        # 저장을하려면 post방식으로 넘겨야됨.
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        # GET-> 사용자가 데이터를 입력하지 않았고 그 상태에서 폼을 보여주는 방식
        form = PostForm() # 인스턴스화
        print(form) # 프린트문에 html코드 찍힘
        return render(request, 'create.html', {'form':form})