from django.views.generic import TemplateView
from employment.models import Employer, Skills


class Home(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employers'] = Employer.objects.all()
        context['skills'] = Skills.objects.all()
        return context

