from django.shortcuts import render
import socket
from page.models import Contact
from django.contrib import messages
from bs4 import BeautifulSoup
import requests

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        contact = Contact(name = name, email = email , massage=massage)
        contact.save()
        messages.success(request, 'Thank you for contacting us. We will replay you very soon as posiable.')

    context = { "ip" : ip_address , "host" : hostname}
    return render(request , 'index.html' , context) 

def scrapping(request):

    return render(request, 'webscrapping.html')



def result(request):
    if request.method == 'POST':
        urls = request.POST.get('url')
        r = requests.get(urls)
        content = r.content
        soup = BeautifulSoup(content, "html.parser") 
        context = {
            "final_html" : content
        }
        return render(request, 'final.html')
