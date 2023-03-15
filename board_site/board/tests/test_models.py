from django.test import TestCase
from ..models import *
import mock
from django.core.files import File


class ModelsTestCase(TestCase):
    def setUp(self):
        rubric = Rubric.objects.create(
            name="test_name",
        )
        rubric.save()

        file_mock = mock.Mock(spec=File)
        file_mock.name = "photo.jpg"

        object1 = Bb.objects.create(
            title="a test1 title",
            photo=file_mock.name,
            slug="a slug",
            content="a content",
            price=1.1,
            rubric=rubric
        )
        object1.save()

    def test_models(self):
        bb1 = Bb.objects.get(id=1)
        rubric_1 = Rubric.objects.get(id=1)

        file_mock = mock.Mock(spec=File)
        file_mock.name = "photo.jpg"

        title = f"{bb1.title}"
        photo = f"{bb1.photo}"
        slug = f"{bb1.slug}"
        content = f"{bb1.content}"
        price = f"{bb1.price}"
        rubric = f"{bb1.rubric.name}"

        self.assertEqual(title, "a test1 title")
        self.assertEqual(photo, file_mock.name),
        self.assertEqual(slug, "a slug")
        self.assertEqual(content, "a content")
        self.assertEqual(price, "1.1")
        self.assertEqual(rubric, rubric_1.name)



