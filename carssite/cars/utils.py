from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

menu = [{'title': "About", 'url_name': 'cars:about'},
        {'title': "Add Post", 'url_name': 'cars:addpost'},
        {'title': "Feedback", 'url_name': 'cars:contact'},
        ]


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
