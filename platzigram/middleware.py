""" Platzigram middleware catalog """

#Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """ Profile completion middleware.
        Ensure every user that is interacting with the platform
        have their profile picture and biography
    """
    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                # Podemos hacer eso porque antes le dijimos que es una relación oneToOne entre profile y user
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    # Condiciono en que pagina va a redireccionar.
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response