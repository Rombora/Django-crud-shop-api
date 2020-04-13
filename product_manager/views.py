""" This file controls the views for Products and Categories inside product_manager. """

# Django imports
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView

# Project imports
from .models import Product, Category
from .forms import ProductForm, CategoryForm

from django.conf import settings
from django.shortcuts import redirect


###########################

from django.contrib.auth.decorators import login_required
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

from django.contrib.auth.mixins import LoginRequiredMixin




#------------------------------------------------------
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

class SignUpView(FormView):
    form_class = UserCreationForm
    template_name = 'product_manager/signup.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('/')

#------------------------------------------------------


class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    # success_url = '/auth/home/'
    success_url = '/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'product_manager/login.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        # redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        redirect_to = self.request.GET.get(self.redirect_field_name)
        # redirect_to = self.request.GET.get(self.template_name)


        if not is_safe_url(url=redirect_to, allowed_hosts=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)



################################
# def my_view(request):
#     if not request.user.is_authenticated:
#         return redirect("login.html")


#####
# from django.shortcuts import render, render_to_response
# from django.contrib.auth import authenticate

# user=authenticate(username="admin3", password="admin3")
# if user is not None:
#     print("valid user ==========================================")
# else:
#     print("invalid user ========================================")
#     render_to_response('login.html')



# def my_view(request):
#     if not request.user.is_authenticated:
#         print("--------------------------------------------------")
#     else:
#         print("++++++++++++++++++++++++++++++++++++++++++++++++++")
#     return render_to_response('login.html')





# global myreq
# myreq = 0


# def my_view(request):
#     myreq = request
#     if 1==1:
#         print("--------------------------------------------------")
#     else:
#         print("++++++++++++++++++++++++++++++++++++++++++++++++++")
#     return render(request, 'login.html')










# class LoginRequiredMixin(object):
#     def as_view(cls):
#         return login_required(super(LoginRequiredMixin, cls).as_view())





class IndexView(LoginRequiredMixin, ListView):
# class IndexView(ListView):
    """ This index view displays the last ten products created. """
    template_name = 'product_manager/index.html'
    
    def get_queryset(self):
            """ Return the last ten products. """
            return Product.objects.order_by('-id')[:10]





class ProductListView(LoginRequiredMixin, ListView):
    """ Allows you to list all products. """
    model = Product

    # render(myreq, 'login.html')

    # render_template('login.html')
    # def two(request):
        # my_view(request)
    # print("================================================")

class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Allows you to create a product (linked to forms). """
    model = Product
    form_class = ProductForm


class ProductDetailView(LoginRequiredMixin, DetailView):
    """ Allows you to view detailed information about an object in Product. """
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """ Allows you to delete a product. """
    model = Product
    success_url = reverse_lazy('product_manager_product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Allows you to update a product's details. """
    model = Product
    form_class = ProductForm









class CategoryListView(LoginRequiredMixin, ListView):
    """ Allows you to view all categories. """
    model = Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm


class CategoryDetailView(LoginRequiredMixin, DetailView):
    """ Allows you to view details of a category (will be used for inline product display). """
    model = Category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of the current category taken from above context.
        context['products_in_category'] = Product.objects.filter(category=context['object'])
        return context


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('product_manager_category_list')

    

class CategoryUpdateView(LoginRequiredMixin, UpdateView):

    model = Category
    form_class = CategoryForm
