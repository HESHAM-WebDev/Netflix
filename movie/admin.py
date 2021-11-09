from django.contrib import admin
from .models import Movie, Actor, Categories, Review, Idnumber


# Register your models here.
class InlineReview(admin.TabularInline):
    model = Review
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name', 'likes', 'actor__first_name', 'actor__id_name__number')
    list_display = ('name', 'likes', 'watch_count', 'rate', 'my_custom_list_display')
    readonly_fields = ("my_custom_list_display","likes")
    inlines = [InlineReview]

    def my_custom_list_display(self, obj):
        if obj.likes and obj.watch_count:
            total = 100 * (obj.likes / obj.watch_count)
            return '{}'.format(round(total))
        else:
            return 0

    my_custom_list_display.short_description = 'Watch/likes Rating'

    fieldsets = (
        ["section_A", {"fields": ["name", "description"]}],
        [None, {'fields': ['likes', 'watch_count', 'rate',"my_custom_list_display"]}],
        ['section_c', {'fields': ['poster', 'video']}],
        ["section_D ",{"fields":["actor"]}]
    )
    def has_delete_permission(self, request, obj=None):
        if request.user.username == "Ali":
            return True
        return False

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Categories)
admin.site.register(Review)
admin.site.register(Idnumber)
