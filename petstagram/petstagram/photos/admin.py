from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "publication_date", "pets")

    @staticmethod
    def pets(current_photo_obj):
        tagged_pets = current_photo_obj.tagged_pets.all()
        if tagged_pets:
            return ", ".join(pet.name for pet in tagged_pets)

        return "No pets"
