from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

from .forms import UserRegisterForm, UserLoginForm, UserProfileEditForm
from .models import CustomUser


class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "accounts/login.html"


class UserLogoutView(LogoutView):
    pass


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "accounts/profile_detail.html"
    context_object_name = "profile_user"

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["played_games"] = user.played_games.all()
        context["wishlist_games"] = user.wishlist_games.all()
        context["latest_reviews"] = user.reviews.select_related("game")[:5]
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserProfileEditForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return self.request.user