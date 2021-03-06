from django import forms
from django.conf import settings
from django.forms import Textarea
from django_filters.widgets import RangeWidget
from django_prices.widgets import PriceInput

from ..userprofile.widgets import (
    PhonePrefixWidget as StorefrontPhonePrefixWidget)


class DateRangeWidget(RangeWidget):
    def __init__(self, attrs=None):
        widgets = (forms.DateInput, forms.DateInput)
        super(RangeWidget, self).__init__(widgets, attrs)


class PriceRangeWidget(RangeWidget):
    def __init__(self, attrs=None):
        self.currency = getattr(settings, 'DEFAULT_CURRENCY')
        widgets = (PriceInput(self.currency), PriceInput(self.currency))
        super(RangeWidget, self).__init__(widgets, attrs)


class PhonePrefixWidget(StorefrontPhonePrefixWidget):
    template_name = 'dashboard/order/widget/phone_prefix_widget.html'


class RichTextEditorWidget(Textarea):
    """
    This widget is used to initialize medium-editor out-of-the-box
    """
    def __init__(self, attrs=None):
        default_attrs = {'class': 'rich-text-editor'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
