import pytest
from django.test import TestCase
from pet_food_diary.models import PetModel

# Create your tests here.

def test_new_user(django_user_model):
    django_user_model.objects.create(username="someone", password="something")

@pytest.mark.django_db
def test_main_page_view(client):
    response =client.get('')
    assert response.status_code == 200

@pytest.mark.django_db
def test_pet_list_view(client, user, pet):
    """
    Tests if a logged in user can access the page, the length of list of pets for currently logged in user.
    Checks if the pet from the list is the correct pet instance.
    """
    client.force_login(user)
    response = client.get('/pet/list/')
    assert response.status_code == 200
    assert len(response.context['pets']) == 1
    assert response.context['pets'][0] == pet


@pytest.mark.django_db
def test_pet_list_view_unauth_access(client):
    """
    Tests if a not logged in user will get a forbidden response
    """
    response = client.get('pet/list/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_pet_detail(client, pet, user):
    client.force_login(user)
    response = client.get(f'/pet/details/{pet.pk}/')
    assert response.status_code == 200
    assert len(response.context['pet']) == 1

@pytest.mark.django_db
def test_pet_create(client, user):
    client.force_login(user)
    response = client.post('/pet/add/',{
        'name': 'fake_name',
        'owner': user,
        'date_of_birth': '2020-03-01',
        'comments': 'A pet'
    })
    assert response.status_code == 302
    assert PetModel.objects.get(name='fake_name', owner=user, date_of_birth='2020-03-01', comments='A pet')


@pytest.mark.django_db
def test_create_pet_unauth(client):
    response = client.get('/pet/add/')
    assert response.status_code == 302

@pytest.mark.django_db
def test_pet_update(client,pet, user):
    client.force_login(user)
    response = client.patch(f'/pet/edit/{pet.pk}', {
        'name': 'pet_name',
        'owner': user,
        'date_of_birth': '2020-03-01',
        'comments': 'A pet'
    })
    assert response.status_code == 301
    assert PetModel.objects.get(name='pet_name', owner=user, date_of_birth='2020-03-01', comments='A pet')

@pytest.mark.django_db
def test_pet_delete(client, pet, user):
    client.force_login(user)
    response = client.delete(f'pet/delete/{pet.pk}/')
    # Można też zrobić metodą post, bo to jest widok generyczny
    assert response.status_code == 404
    assert len(PetModel.objects.filter(pk=pet.pk)) == 0
    # PetModel.objects.filter(pk=pet.pk).count() == 0
    # PetModel.objects.filter(pk=pet.pk).empty()
