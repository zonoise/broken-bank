from django import forms
class AddMoneyForm(forms.Form):
    isolation_level = forms.ChoiceField(choices=(
            ('READ_COMMITED','READ_COMMITED'),
            ('READ_UNCOMMITTED','READ_UNCOMMITTED'),
            ('SERIALIZABLE','SERIALIZABLE'),
            ('REPEATABLE_READ','REPEATABLE_READ'),
        ))
    row_lock = forms.ChoiceField(
        choices=(
            ('None','None'),
            ('FOR_UPDATE','FOR_UPDATE'),
            ('LOCK_IN_SHARE_MODE','LOCK_IN_SHARE_MODE'),
        ),
        widget=forms.Select)
    value = forms.IntegerField()
