from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from todos import models

# Create your tests here.
class TodosTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = models.Todo.objects.create(
            title="Todo test",
            body="Todo body test"
        )
        
    def test_model_content(self):
        self.assertEqual(self.todo.title, "Todo test")
        self.assertEqual(self.todo.body, "Todo body test")
        self.assertEqual(str(self.todo), "Todo test")
        
    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
        
    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Todo.objects.count(), 1)
        self.assertContains(response, "Todo test")