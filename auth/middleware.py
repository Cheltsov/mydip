from django.utils.timezone import now
from core.models.user import User


class SetLastVisitMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_response(self, request, response):
        if request.user.is_authenticated():
            User.objects.filter(pk=request.user.pk).update(last_visit=now())
        return response
