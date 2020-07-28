from django.shortcuts import render, redirect
from .models import Post
import uuid

# Create your views here.
def index(request):
    context = {
        "all_posts": Post.objects.all()
    }
    return render(request, "index.html", context)


def create_image(request):
    file_name = request.FILES["image"].name
    request.FILES["image"].name = "{}.{}".format(uuid.uuid4().hex, file_name.split(".")[-1])
    print(request.FILES["image"].name)

    Post.objects.create(
        subject = request.POST['subject'],
        file_name = file_name,
        image = request.FILES["image"]
    )
    return redirect("/")