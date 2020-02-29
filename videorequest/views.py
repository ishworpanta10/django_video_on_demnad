from django.shortcuts import render, redirect

# Create your views here.

from .models import Video

from .forms import VideoRequestForm


def index(request):
    videos = Video.objects.order_by("-date_added")
    context = {"videos": videos}
    return render(request, "videorequest/index.html", context)


def vrform(request):
    if request.method == "POST":
        # form is obj of VideoRequestForm
        form = VideoRequestForm(request.POST)
        if form.is_valid():
            # we make object of Video model as new_req
            new_req = Video(
                videotitle=request.POST["videoname"],
                videodesc=request.POST["videodesc"],
            )
            # Here first videotitle arg is of Video model attribute and
            # last .POST after videoname is of  forms.py VideoRequestForm class attr
            new_req.save()
            return redirect("index")  # index is url name
    else:
        print("Error")
        form = VideoRequestForm()

    context = {"form": form}
    return render(request, "videorequest/vrform.html", context)

