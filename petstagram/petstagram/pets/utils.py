from petstagram.pets.models import Pet


def get_by_petname_and_username(pet_slug, username):
    return Pet.objects.get(slug=pet_slug)
