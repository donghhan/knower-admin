from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from django.conf import settings

EXEMPTED_URL_PATHNAMES = ["login", "forgot-password"]


class AllPagesLoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            current_pathname = resolve(request.path_info).url_name

            if not current_pathname in EXEMPTED_URL_PATHNAMES:
                return HttpResponseRedirect(reverse("common:login"))
