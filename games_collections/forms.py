from django import forms
from .models import Collection


class BaseCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ["title", "description", "banner", "games"]
        labels = {
            "title": "Collection title",
            "description": "Description",
            "banner": "Banner image",
            "games": "Games",
        }
        help_texts = {
            "description": "Write a short description for this collection.",
            "banner": "Upload a wide banner image.",
            "games": "Select one or more games.",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Best two-player games",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Describe the collection...",
            }),
            "banner": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "games": forms.SelectMultiple(attrs={
                "class": "form-select",
                "size": 8,
            }),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 2:
            raise forms.ValidationError("Title must contain at least 2 characters.")
        return title

    def clean_description(self):
        description = self.cleaned_data["description"].strip()
        if len(description) < 10:
            raise forms.ValidationError("Description must contain at least 10 characters.")
        return description


class CollectionCreateForm(BaseCollectionForm):
    pass


class CollectionEditForm(BaseCollectionForm):
    pass


class CollectionDeleteForm(BaseCollectionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance