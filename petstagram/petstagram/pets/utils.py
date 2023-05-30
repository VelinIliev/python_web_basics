from petstagram.pets.models import Pet


def get_by_petname_and_username(pet_slug, username):
    return Pet.objects.filter(slug=pet_slug).get()
