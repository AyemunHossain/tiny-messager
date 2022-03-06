from django.shortcuts import render



def chat(request, *args, **kwargs):
    
    return render(request, "chat.html")
