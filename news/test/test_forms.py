from django.test import TestCase

from news.forms import RedactorCreationForm


class RedactorCreationFormTest(TestCase):
    def test_redactor_creat_form(self):
        form_data = {
            "username": "new_user",
            "password1": "user12345",
            "password2": "user12345",
            "first_name": "User first",
            "last_name": "User last",
            "years_of_experience": 3
        }
        form = RedactorCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(form_data, form.cleaned_data)
