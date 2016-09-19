from django.shortcuts import render, redirect
from . models import Secrets

# Create your views here.
def index(request):
	context = {
	"secrets": Secrets.objects.all()
	}
	return render(request, 'secret/index.html', context)

def secret(request):
	Secrets.objects.create(secret=request.POST['secret'])
	return redirect('/')