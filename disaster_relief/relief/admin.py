from django.contrib import admin
from .models import Disaster, Donation, Volunteer,Article,MissingPerson

admin.site.register(Disaster)
admin.site.register(Donation)
admin.site.register(Volunteer)
admin.site.register(Article)
admin.site.register(MissingPerson)  # Register the model
