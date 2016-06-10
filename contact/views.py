from django.shortcuts import render, redirect
from contact.forms import ContactForm
# new imports that go at the top of the file
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.template import Context

# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['lthai423@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            # email.send()
            send_mail('Subject here', 'Here is the message.', 'from@example.com', ['lthai423@gmail.com'], fail_silently=False)

            print "\n\nwtf  \n\n"
            return redirect('/contact')

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })
	
def licenses(request):
	return render(request, 'home/licenses.html')

