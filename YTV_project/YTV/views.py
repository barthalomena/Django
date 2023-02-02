from django.shortcuts import render

# Create your views here.
from pytube import YouTube #youtube module

def index(request): #defines the index function, which takes a single argument request which represents an HTTP request.
    try:# starts a try-except block to handle any exceptions that might occur.
        if request.method=="POST":#checks if the request method is a "POST" request. If it is, the code inside the block is executed.
            try:
                link=request.POST["link"]#extracts the link from the POST data of the request.
                video=YouTube(link)#creates a YouTube object from the extracted link.
                import pdb; pdb.set_trace() # Debugger

                stream=video.streams.get_by_resolution()# gets the lowest resolution video stream from the YouTube object.
                stream.download() #downloads the video stream.
                return render(request,"index.html",{"map":"downloded"})#"Video downloaded".
            except:
                return render(request,"index.html",{"msg":"not downloaded"})
        return render(request, 'index.html', {'msg':''})
    except:            
        return render(request,"index.html",{"msg":"sorry, something went wrong"})
