from django import forms  # import django forms

CHART_CHOICES = (
    ("#1", "Bar chart"),  # when user selects "Bar chart", it is stored as "#1"
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)


class RecipeSearchForm(forms.Form):
    recipe_title = forms.CharField(required=False, label="Recipe Title")
    chart_type = forms.ChoiceField(
        choices=[("#1", "Bar"), ("#2", "Pie"), ("#3", "Line")],
        required=False,
        label="Chart Type",
    )
    show_all = forms.BooleanField(required=False, label="Show All")
