from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class TemplatePage(generic.TemplateView):
    template_name = "template.html"
