from django.shortcuts import render

from .forms import ContactForm, SignUpForm

from .models import SignUp

#from django.core.mail import send_mail

#from django.conf import settings

# Create your views here.

def home(request):
    title = "Sign up for excessive spam"
    if request.user.is_authenticated():
        title = "101 %s" %(request.user)

    #if request.method == "POST":
        #print(request.POST)

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "new full name"
        instance.full_name = full_name
        #if not instance.full_name:
        #    instance.full_name == "12345"
        instance.save()
        context = {
            "title": "Done",
        }
        #print(instance.email)
        #print(instance.full_name)
        #print(instance.timestamp)

    if request.user.is_authenticated() and request.user.is_staff:
        #print(SignUp.objects.all())
        #i=1
        #for instance in SignUp.objects.all():
        #    print(i)
        #    print(instance.full_name)
        #   i+=1

        queryset = SignUp.objects.all().order_by('-timestamp')#.filter(full_name__icontains="asd")
        #print(SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="asd").count())
        context={
            "queryset": queryset
        }

    return render(request, "home.html", context)

def contact(request):
    title="Contact"
    title_align_center = False
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        #print(email)
        #print(message)
        #print(full_name)
        #print(email, message, full_name)
        #for key in form.cleaned_data:
        #    print(key,form.cleaned_data.get(key))

        #subject = "site contact"
        #from_email = settings.EMAIL_HOST_USER
        #to_email = [from_email]
        #contact_message="%s: %s via %s"%(form_full_name, form_message, form_email)

        #send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }

    return render(request, "forms.html", context)
