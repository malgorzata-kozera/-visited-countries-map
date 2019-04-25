from django import forms
from .select_countries import select_options

'''
CountriesChoice class is using a select_options() function to create a form.
It creates a multiple choice fields with checkbox inside.
As an options it takes a values (names of the countries) from the json file sorted by continent.
'''


class CountriesChoice(forms.Form):

    Europe = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Europe'))
    Asia = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Asia'))
    Africa = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Africa'))
    Antarctica = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Antarctica'))

    Oceania = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Oceania'))

    South_America = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('South America'))

    North_America = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('North America'))
