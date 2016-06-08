from django.shortcuts import render

def contact(request):
	return render(request, 'contact/contact.html')
	
def licenses(request):
	return render(request, 'home/licenses.html')

