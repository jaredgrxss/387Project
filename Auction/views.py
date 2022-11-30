from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class LogoutConfirm(generic.TemplateView):
    template_name = 'signout_confirm.html'


class LoginConfirm(generic.TemplateView):
    template_name = 'signin_confirm.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'