from django.shortcuts import render,redirect
from.models import slide,aboutus,why_choose_us,services,portfolio,contact,OurTeam,points
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def home(request):
    about=aboutus.objects.all()
    slides=slide.objects.all()
    why_choose_uss=why_choose_us.objects.all()
    servicess=services.objects.all()
    portfolios=portfolio.objects.all()
    contacts=contact.objects.all()
    ourteams=OurTeam.objects.all()
    point=points.objects.all()
    return render(request, 'index.html',{'aboutus':about,'slide':slides,'why':why_choose_uss,'services':servicess,'portfolio':portfolios,'contact':contacts,'ourteam':ourteams,'points':point})


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_message = "Name: {}\n\n{}".format(name, message)

        try:
            send_mail( subject, full_message, email, ['acharyaprajjwol152@gmail.com'])
            messages.success(request, 'Your message has been sent. Thank you!')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect(reverse('home'))
        else:
            return redirect(reverse('home') + '?success=email sent successfully')
    return redirect('home')