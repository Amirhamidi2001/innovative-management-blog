from django.views.generic.edit import FormView
from django.shortcuts import render
from article.forms import ContactForm


class HomePageView(FormView):
    """
    View for displaying the home page and handling contact form submissions.
    """

    template_name = "index.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        """
        Save the form data when it is valid.
        """

        form.save()
        return super().form_valid(form)
