from django.db import models
from django.contrib.postgres.fields import JSONField
from model_utils.fields import AutoCreatedField, AutoLastModifiedField

from bam_a_py.users.models import User
from enumfields import Enum, EnumField


class Skill(models.Model):
    created_at = AutoCreatedField()
    created_by = models.ForeignKey(User)
    modified_at = AutoLastModifiedField()
    name = models.CharField(max_length=20)
    description = models.TextField()
    levels_examples = JSONField()

    def __str__(self):
        return self.name


class SkillLevel(Enum):
    LEVEL_0 = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4


class Competency(models.Model):
    user = models.ForeignKey(User)
    skill = models.ForeignKey(Skill)
    created_at = AutoCreatedField()
    level = EnumField(SkillLevel, max_length=3, null=True)

    class Meta:
        verbose_name_plural = "Competencies"

