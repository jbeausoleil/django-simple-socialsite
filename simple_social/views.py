from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test'


class ThanksPage(TemplateView):
    template_name = 'thanks'


class Homepage(TemplateView):
    template_name = 'index.html'