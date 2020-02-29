from django import forms


class VideoRequestForm(forms.Form):
    videoname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Title here", "id": "title"}
        ),
    )

    videodesc = forms.CharField(
        max_length=400,
        widget=forms.Textarea(
            {
                "class": "form-control",
                "placeholder": "Description here",
                "rows": "8",
                "id": "desc",
            }
        ),
    )
