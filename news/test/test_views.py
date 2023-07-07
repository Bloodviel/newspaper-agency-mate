from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from news.models import Newspaper, Topic

TOPIC_URL = reverse("news:topic-list")
NEWSPAPER_URL = reverse("news:newspaper-list")
REDACTOR_URL = reverse("news:redactor-list")
USERNAME = "user12"
PASSWORD = "user12345"
TOPICS = ["Art", "Weather", "Politics"]
NEWSPAPERS = [
    ("TestTitle35", "TestContent1"),
    ("TestTitle66", "TestContent2"),
    ("TestTitle09", "TestContent3"),
]
REDACTORS = [
    {
        "username": "redactor_1",
        "first_name": "first_1",
        "last_name": "last_1",
        "years_of_experience": 1
    },
    {
        "username": "redactor_2",
        "first_name": "first_2",
        "last_name": "last_2",
        "years_of_experience": 2
    },
    {
        "username": "redactor_3",
        "first_name": "first_3",
        "last_name": "last_3",
        "years_of_experience": 3
    }
]


class PublicViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_topic_login_required(self):
        response_1 = self.client.get("news:topic-update")
        response_2 = self.client.get("news:topic-delete")

        self.assertNotEquals(response_1.status_code, 200)
        self.assertNotEquals(response_2.status_code, 200)

    def test_newspaper_login_required(self):
        response_1 = self.client.get("news:newspaper-update")
        response_2 = self.client.get("news:newspaper-delete")

        self.assertNotEquals(response_1.status_code, 200)
        self.assertNotEquals(response_2.status_code, 200)


class PrivateTopicViewTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USERNAME,
            password=PASSWORD
        )

        self.client.force_login(self.user)

    @classmethod
    def setUpTestData(cls):
        for topic in TOPICS:
            Topic.objects.create(
                name=topic[0],

            )

    def test_retrieve_topic(self):
        response = self.client.get(TOPIC_URL)
        topic_list = Topic.objects.all()

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            list(response.context["topic_list"]),
            list(topic_list)
        )
        self.assertTemplateUsed(response, "news/topic_list.html")

    def test_topic_search_form(self):
        search_value = "Ar"
        url = reverse("news:topic-list") + f"?name={search_value}"
        response = self.client.get(url)
        topic_query = Topic.objects.filter(
            name__icontains=search_value
        )

        self.assertEquals(
            list(response.context["topic_list"]),
            list(topic_query)
        )


class PrivateNewspaperViewTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USERNAME,
            password=PASSWORD
        )
        self.client.force_login(self.user)

    @classmethod
    def setUpTestData(cls):
        for topic in TOPICS:
            Topic.objects.create(
                name=topic,
            )

        for newspaper in range(len(NEWSPAPERS)):
            Newspaper.objects.create(
                title=NEWSPAPERS[newspaper][0],
                content=NEWSPAPERS[newspaper][1],
                topic=Topic.objects.get(id=newspaper + 1)
            )

    def test_retrieve_newspaper(self):
        response = self.client.get(NEWSPAPER_URL)
        newspaper_list = Newspaper.objects.all()

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            list(response.context["newspaper_list"]),
            list(newspaper_list)
        )
        self.assertTemplateUsed(response, "news/newspaper_list.html")

    def test_newspaper_search_form(self):
        search_value = "35"
        url = reverse("news:newspaper-list") + f"?title={search_value}"
        response = self.client.get(url)
        newspaper_query = Newspaper.objects.filter(
            title__icontains=search_value
        )

        self.assertEquals(
            list(response.context["newspaper_list"]),
            list(newspaper_query)
        )


class PrivateRedactorViewTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=USERNAME,
            password=PASSWORD
        )
        self.client.force_login(self.user)

    @classmethod
    def setUpTestData(cls):
        for redactor in REDACTORS:
            get_user_model().objects.create(
                username=redactor["username"],
                first_name=redactor["first_name"],
                last_name=redactor["last_name"],
                years_of_experience=redactor["years_of_experience"]
            )

    def test_retrieve_redactor(self):
        response = self.client.get(REDACTOR_URL)
        redactor_list = get_user_model().objects.all()

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            list(response.context["redactor_list"]),
            list(redactor_list)
        )
        self.assertTemplateUsed(response, "news/redactor_list.html")

    def test_redactor_search_form(self):
        search_value = "_2"
        url = reverse("news:redactor-list") + f"?username={search_value}"
        response = self.client.get(url)
        redactor_query = get_user_model().objects.filter(
            username__icontains=search_value
        )

        self.assertEquals(
            list(response.context["redactor_list"]),
            list(redactor_query)
        )
