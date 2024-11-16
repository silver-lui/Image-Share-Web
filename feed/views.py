from django.views.generic import FormView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Post
from .form import PostForm

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
class PostDetailView(DetailView):
    template_name="details.html"
    model = Post

class PostView(FormView):
    template_name="add_image.html"
    form_class=PostForm
    success_url='/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )

        messages.add_message(self.request, messages.SUCCESS, "POST WAS ADDED SUCCESSFULLY")

        return super().form_valid(form)