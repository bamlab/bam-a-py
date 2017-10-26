from django.contrib import admin
from .models import Skill, Competency


class SkillCompetencyInline(admin.TabularInline):
    model = Competency
    can_delete = False
    readonly_fields = ["user", "level"]
    ordering = ["level"]

    def has_add_permission(self, request):
        return False


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    inlines = [SkillCompetencyInline]


class CompetencyAdmin(admin.ModelAdmin):
    list_display = ["skill", "user", "level"]
    date_hierarchy = "created_at"


admin.site.register(Skill, SkillAdmin)
admin.site.register(Competency, CompetencyAdmin)
