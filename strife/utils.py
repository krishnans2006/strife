from django import forms


class StrifeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StrifeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "w-full rounded"
