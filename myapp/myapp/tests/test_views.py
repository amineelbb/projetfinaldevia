# from django.urls import reverse
# from django.test import TestCase
# import pytest
import django
# from django.contrib.auth.models import User
django.setup()


# @pytest.fixture
# def setUp(self):
#         # Crée un utilisateur pour les tests
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

# @pytest.mark.django_db
# def test_index_view(self):
#         url = reverse('index')  # Assurez-vous que 'index' est le nom de votre vue
#         response = self.client.get(url)
#         assert url == ''
#         self.assertEqual(response.status_code, 200)
#         assert 'index.html' in [t.name for t in response.templates]



# @pytest.mark.django_db
# def test_signup_view(self):
        

#         url = reverse('signup')  # Assurez-vous que 'signup' est le nom de votre vue
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#         # Test du formulaire de création d'utilisateur
#         response = self.client.post(url, {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
#         self.assertEqual(response.status_code, 302)  # Redirection après inscription

# @pytest.mark.django_db
# def test_login_view(self):
#         url = reverse('login')  # Assurez-vous que 'login' est le nom de votre vue
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#         # Test de connexion avec un utilisateur valide
#         response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword'})
#         self.assertEqual(response.status_code, 302)  # Redirection après connexion

# @pytest.mark.django_db
# def test_logout_view(self):
#         url = reverse('logout')  # Assurez-vous que 'logout' est le nom de votre vue
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 302)  # Redirection après déconnexion

#     # Ajoutez des tests pour d'autres vues ici...
from django.test import Client
from django.urls import reverse
import pytest
from django.contrib.auth.models import User
import pytest
from django.contrib.auth.models import User




@pytest.fixture
def client():
   return Client()




# def test_index_view(client):
#    url = reverse('index')
#    response = client.get(url)  # Replace with your actual URL path
#    assert response.status_code == 200
#    assert 'index.html' in [t.name for t in response.templates]




@pytest.mark.django_db
def index_view(client, django_user_model):  # Assuming you have a User model
   # Manually create a user instance
   user = django_user_model.objects.create_user(
       username='testuser', password='password')


   # Simulate a logged-in user
   client.force_login(user)


   # Make a request to the 'hello' view
   url = reverse('index')
   response = client.get(url)


   # Assert the response status code is 200
   assert response.status_code == 200


   # Assert that the correct template is used
   assert 'index.html' in [t.name for t in response.templates]


   # Assert that the 'username' variable is passed to the template
   assert 'username' in response.context
   assert response.context['username'] == user.username


@pytest.mark.django_db
def test_connexion():
   all_object = User.objects.all()
   assert all_object is not None


