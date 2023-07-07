from django.contrib.auth import get_user_model
from django.test import TestCase

from news.models import Newspaper, Topic


class TopicNewspaperModelTests(TestCase):
    def test_topic_str(self):
        obj_topic = Topic.objects.create(
            name="TestTopic"
        )

        self.assertEquals(str(obj_topic), "TestTopic")

    def test_newspaper_str(self):
        obj_topic = Topic.objects.create(
            name="TestTopic"
        )
        obj_newspaper = Newspaper.objects.create(
            title="TestTitle",
            content="TestContent",
            topic=obj_topic
        )

        self.assertEquals(str(obj_newspaper), "TestTitle")


class RedactorModelTests(TestCase):
    def setUp(self) -> None:
        self.obj_redactor = get_user_model().objects.create_user(
            username="user321",
            first_name="user_first",
            last_name="user_last",
            password="user12345",
            years_of_experience=3
        )

    def test_redactor_str(self):
        obj_redactor = get_user_model().objects.get(id=1)

        self.assertEquals(
            str(obj_redactor), "user321"
        )

    def test_redactor_years_of_experience(self):
        obj_redactor = get_user_model().objects.get(id=1)

        self.assertTrue(obj_redactor.check_password("user12345"))
        self.assertEquals(
            obj_redactor.years_of_experience, 3
        )

    def test_redactor_get_absolute_url(self):
        obj_redactor = get_user_model().objects.get(id=1)

        self.assertEquals(
            obj_redactor.get_absolute_url(), "/redactors/1/"
        )
