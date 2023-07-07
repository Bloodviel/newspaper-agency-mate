from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.obj_redactor = get_user_model().objects.create_user(
            username="user321",
            first_name="user_first",
            last_name="user_last",
            password="user12345",
            years_of_experience=3
        )

    def test_redactor_years_of_experience_listed(self):
        url = reverse("admin:news_redactor_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.obj_redactor.years_of_experience)

    def test_redactor_detailed_years_of_experience_listed(self):
        url = reverse("admin:news_redactor_change", args=[self.obj_redactor.id])
        response = self.client.get(url)

        self.assertContains(response, self.obj_redactor.years_of_experience)

    def test_redactor_add_additional_info(self):
        url = reverse("admin:news_redactor_add")
        response = self.client.get(url)

        self.assertContains(response, "First name")
        self.assertContains(response, "Last name")
        self.assertContains(response, "Years of experience")
