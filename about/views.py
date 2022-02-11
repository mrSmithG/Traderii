from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from about import forms
from .models import ProductImage

# Create your views here.
class ContactUsView(FormView):
    template_name = "contact_us.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

class HomePageView(TemplateView):
    template_name = "homepage.html"
    model = Product
    context_object_name = 'product_detail'

class ProductDetailView(DetailView):
    pass 

class PurchaseProductView(DetailView):
    pass    
