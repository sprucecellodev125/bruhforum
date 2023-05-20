from django.conf import settings

def global_context(request):
    # Add your context variables here
    context = {
        'DEBUG': settings.DEBUG,
        # Add more variables as needed
    }
    return context
