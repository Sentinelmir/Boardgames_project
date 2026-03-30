from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from .forms import CollectionCreateForm, CollectionEditForm, CollectionDeleteForm
from .models import Collection


class CollectionListView(ListView):
    model = Collection
    template_name = "collections/collection_list.html"
    context_object_name = "collections"

    def get_queryset(self):
        return Collection.objects.select_related("owner").prefetch_related("games")


class CollectionDetailView(DetailView):
    model = Collection
    template_name = "collections/collection_detail.html"
    context_object_name = "collection"

    def get_queryset(self):
        return Collection.objects.select_related("owner").prefetch_related("games")

class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionCreateForm
    template_name = "collections/collection_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("collections:detail", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create collection"
        context["submit_label"] = "Save collection"
        context["cancel_url"] = reverse("collections:list")
        return context

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionEditForm
    template_name = "collections/collection_form.html"
    context_object_name = "collection"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse("collections:detail", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Edit collection"
        context["submit_label"] = "Save changes"
        context["cancel_url"] = reverse("collections:detail", kwargs={"slug": self.object.slug})
        return context

class CollectionDeleteView(LoginRequiredMixin, FormView):
    template_name = "collections/collection_confirm_delete.html"
    form_class = CollectionDeleteForm
    success_url = reverse_lazy("collections:list")

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(Collection, slug=kwargs["slug"])

        if request.user.is_staff or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if self.object.owner != request.user:
            raise Http404("You do not have permission to delete this collection.")

        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect("collections:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collection"] = self.object
        context["cancel_url"] = reverse("collections:detail", kwargs={"slug": self.object.slug})
        return context