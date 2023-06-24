from django.conf import settings
from .models import Core

def global_context(request):
    context = {
        'DEBUG': settings.DEBUG,
        'core': Core.objects.all()
    }
    return context
