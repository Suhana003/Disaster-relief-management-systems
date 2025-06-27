from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Disaster
from .forms import DisasterForm
from .forms import Donation
from .models import Article
from .models import Volunteer
from .models import MissingPerson
from .forms import MissingPersonForm




import stripe
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import feedparser
from django.shortcuts import render


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY 




def report_disaster(request):
    if request.method == 'POST':
        form = DisasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disaster_list')
    else:
        form = DisasterForm()
    return render(request, 'report_disaster.html', {'form': form})
def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disaster_list.html', {'disasters': disasters})

# views.py



def donation(request):
    if request.method == 'POST':
        form = Donation(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            amount = form.cleaned_data.get('amount')

            # Send a thank-you email
            send_mail(
                'Donation Confirmation',
                f'Thank you {name} for your generous donation of ${amount}!',
                'suhanasnr9@gmail.com',
                [email],  # Donator's email
                fail_silently=False,
            )
            return redirect('thank_you')
            return HttpResponse("Thank you for your donation! A confirmation email has been sent.")
    else:
        form = Donation()

    return render(request, 'donation.html', {'form': form})

def first_donation(request):
    return render(request,'first_donation.html')

def thank_you(request):
    return render(request, 'thank_you.html')

def Thanks(request):
    return render(request,'Thanks.html')

@csrf_exempt  # Allow POST requests without CSRF token issues
def process_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON request
            donor_email = data.get('email')

            if donor_email:
                send_mail(
                    'Thank You for Your Donation!',
                    'Dear Donor,\n\nThank you for your generous donation. Your contribution is greatly appreciated!\n\nBest Regards,\nRelief Team',
                    'suhanasnr9@gmail.com',  # Your sender email
                    [donor_email],  # Recipient's email
                    fail_silently=False,
                )
                return JsonResponse({"message": "Payment Successful! A confirmation email has been sent."})
            else:
                return JsonResponse({"message": "Email is required!"}, status=400)
        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method!"}, status=400)


# views.py



def home(request):
    articles = Article.objects.all()  # Get all articles
    return render(request, 'index.html', {'articles': articles})
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})


def news(request):
    return render(request, 'news.html')


def contact(request):
     return render(request, 'contact.html')

def about(request):
     return render(request, 'about.html')

def index(request):
    return render(request,'index.html')






def fetch_news():
    rss_url = "https://news.google.com/rss/search?q=disaster+relief&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    news_items = []

    for entry in feed.entries[:10]:  # Limit to 10 articles
        news_items.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    
    return news_items

def news_view(request):
    news = fetch_news()
    return render(request, "news.html", {"news": news})


def volunteer_signup(request):
    if request.method == "POST":
        Fullname = request.POST.get("Fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        # ✅ Send confirmation email
        subject = "Thank You for Signing Up as a Volunteer!"
        message = f"Dear {Fullname},\n\nThank you for signing up to volunteer! We appreciate your support.\n\n- Disaster Relief Team"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return redirect("Thanks")  # Redirect to the thank-you page

    return render(request, "volunteer_signup.html")


def report_missing_person(request):
    if request.method == 'POST':
        form = MissingPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('missing_persons_list')  # Redirect to the list after submission
    else:
        form = MissingPersonForm()
    return render(request, "report_missing_person.html", {'form': form})

def missing_persons_list(request):
    persons = MissingPerson.objects.filter(status='Missing')
    return render(request, 'missing_persons_list.html', {'persons': persons})
