from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})
	
def contact(request):
	if request.method == "POST" :
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(
			message_name, #subject
			message, #message
			message_email, #from_email
			['faridehburs@gmail.com'], #to_email
			fail_silently = False,
			)

		return render(request, 'contact.html', {})

	else:
		return render(request, 'contact.html', {})