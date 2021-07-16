from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == "POST":
        context={"fname":request.POST["fname"],
        "location":request.POST["location"],
        "fav_lang":request.POST["fav_lang"],
        "txt_comments":request.POST["txt_comments"]
        }
    return render(request,'result.html',context)

