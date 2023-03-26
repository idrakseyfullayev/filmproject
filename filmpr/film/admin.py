from django.contrib import admin

# Register your models here.
from film.models import ActorModel, FilmModel, LikeModel, CommentModel, CategoryModel, ViewNumberModel

# admin.site.register(ActorModel)
admin.site.register(LikeModel)
admin.site.register(CommentModel)
# admin.site.register(CategoryModel)
admin.site.register(ViewNumberModel)

@admin.register(FilmModel)
class FilmAdmin(admin.ModelAdmin):
    # fields = ("name", "rating",)
    list_display = ("name", "rating","pub_date",)
    list_display_links = ("name", "rating","pub_date")
    list_filter = ("pub_date",)
    date_hierarchy = "pub_date"

    fieldsets = (
        ("BASIC INFO", {
            'fields': ('name', 'poster', 'video',)
        }),
        ('OTER INFO', {
            'classes': ('collapse',),
            'fields': ('pub_date', 'rating',),
        }),
        
        ('LAST INFO', {
            'fields': ('about', 'actors'),
        }),
    )
        
# admin.site.register( FilmModel, FilmAdmin)


class ActorAdmin(admin.ModelAdmin):
    list_display = ("name","surname", "poster")
    

admin.site.register(ActorModel, ActorAdmin)


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass
    