from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Project, Review, Milestone, Skill, Contact, Profile


# Create your views here.
def index_page(request):
    user_review = Review.objects.all()
    recent_projects = Project.objects.order_by('-acquired_date')[:3]
    context = {'projects': recent_projects, 'reviews': user_review}
    return render(request, 'index.html', context)


def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Project.objects.filter(name__icontains=query)

    context = {'results': results, 'query': query}
    return render(request, 'search_results.html', context)


def profile_page(request):
    milestones = Milestone.objects.all()
    skills = Skill.objects.all()
    profiles = Profile.objects.all()
    return render(request, "profile.html", {'milestones': milestones, 'skills': skills, 'profile': profiles})


def blogs_page(request):
    return render(request, 'blogs.html')


def portfolio_page(request):
    projects = Project.objects.order_by('creation_date')[:3]
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects, 'projects': projects}
    return render(request, 'portfolio.html', context)


def review_page(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form, 'reviews': reviews})


def contact_me_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company_name']
        company_address = request.POST['company_address']
        company_position = request.POST['company_position']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            company_address=company_address,
            company_position=company_position,
            email=email,
            phone_number=phone_number,
            subject=subject,
            message=message
        )
        contact.save()

        send_mail(
            f"{subject}",
            f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}",
            # Email content
            settings.DEFAULT_FROM_EMAIL,
            ['johnTowett@outlook.com'],
            fail_silently=False,
        )

        return redirect('success')

    return render(request, 'contact-me.html')


def thankyou_page(request):
    return render(request, 'thankyou.html')


def success_page(request):
    return render(request, 'success.html')