from django import forms
class AddMoneyForm(forms.Form):
    isolation_level = forms.ChoiceField(choices=(
            ('A','A'),
            ('B','B'),
            ('C','C'),
        ))
    row_lock = forms.ChoiceField(
        choices=(
            ('A','A'),
            ('B','B'),
        ),
        widget=forms.Select)
    value = forms.IntegerField()
