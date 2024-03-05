from django.contrib import admin
'''from toolapp.models import person'''
from toolapp.models import *
from toolapp.models import review
from toolapp.models import contact
from toolapp.models import user_register
from toolapp.models import helpus

# Register your models here.
'''admin.site.register(person)'''
admin.site.register(ContentCreator)
admin.site.register(Blog)
admin.site.register(review)
admin.site.register(contact)
admin.site.register(user_register)
admin.site.register(helpus)