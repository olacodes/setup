from django.test import TestCase

# Create your tests here.

class TestCI(TestCase):
  def test_github_action_ci(self):
    self.assertEqual(2 + 2, 4)
