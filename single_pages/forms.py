from django import forms
from django.forms.widgets import DateInput, TimeInput


class DateInputWidget(DateInput):
    input_type = 'date'


class TimeInputWidget(TimeInput):
    input_type = 'time'


class ContactForm(forms.Form):
    ENQUIRY_TYPE = (
        ('Booking the Course', 'Booking the Course'),
        ('Get Information', 'Get Information'),
        ('Payment question', 'Payment question')
    )
    enquiry_type = forms.ChoiceField(
        label='Select Enquiry Type',
        required=True,
        widget=forms.Select(attrs={
            'class': 'field-select__select',
        }),
        choices=ENQUIRY_TYPE
    )
    name = forms.CharField(
        label='Name',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'field-text__input'
        })
    )
    email = forms.CharField(
        label='Email',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'field-text__input'
        })
    )
    phone = forms.CharField(
        label='Phone Number',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'field-text__input'
        })
    )
    message = forms.CharField(
        label='Message / Question',
        widget=forms.Textarea(attrs={
            'class': 'field-text__input',
            'cols': '',
            'rows': ''
        }),
        required=True
    )


class BookingForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'field-text__input'
        })
    )
    email = forms.CharField(
        label='Email',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'field-text__input'
        })
    )
    phone = forms.CharField(
        label='Phone Number',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'field-text__input'
        })
    )
    program = forms.CharField (
        label='Desired program',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'field-text__input'
        })
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'field-text__input',
            'cols': '',
            'rows': ''
        }),
        required=True
    )
