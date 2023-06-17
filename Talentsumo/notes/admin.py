from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    search_fields = ('title',)
    list_filter = ('type',)
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        if not change:
            # Set the user who created the note
            obj.user = request.user
        super().save_model(request, obj, form, change)



