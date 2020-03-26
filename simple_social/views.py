from django.views.generic import TemplateView


class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class Homepage(TemplateView):
    template_name = 'index.html'
