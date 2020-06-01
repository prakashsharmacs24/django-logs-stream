from django.views.generic import TemplateView


class StreamView(TemplateView):
    template_name = "stream.html"
