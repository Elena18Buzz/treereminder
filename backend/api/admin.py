from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    # Display 'user', 'text', 'created_at', 'due_date', and user email
    list_display = ('author', 'get_username', 'get_email', 'content', 'created_at', 'due_date')
    
    # Custom method to show the username in the admin
    def get_username(self, obj):
        return obj.author.username
    get_username.short_description = 'Username'  # This will change the column header to 'Username'

    # Custom method to show the user's email in the admin
    def get_email(self, obj):
        return obj.author.email
    get_email.short_description = 'Email'  # This will change the column header to 'Email'

    # Filter reminders by user
    list_filter = ('author', 'due_date')
    
    # Make 'text' field searchable
    search_fields = ('content',)

    # Ordering reminders by creation date (newest first)
    ordering = ('-created_at',)

# Register the Reminder model with the custom ReminderAdmin
admin.site.register(Note, NoteAdmin)