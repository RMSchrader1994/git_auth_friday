from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import Compose_Message


# Create your views here.
def inbox(request):
    return render(request, 'messanger/indox.html')

def sent(request):
    return render(request, 'messanger/sent.html')
    
def view_message(request, id):
    mail = get_object_or_404(Message, pk=id)
    message.read=True
    message.save()
    return render(request, "messanger/mail.html", {'mail': mail})
    
def compose(request): 
    if request.method == "POST":
        form = Compose_Message(request.POST)
        message = form.save(commit=False)
        message.sender = request.user
        message.save()
        return redirect("inbox")
    else:
        print("It's the GET")
        
    form = Compose_Message()
    return render(request, "messanger/compose.html", {'form': form})
    
    
  