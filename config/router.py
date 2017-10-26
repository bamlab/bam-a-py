from rest_framework import routers
from bam_a_py.users.viewsets import UserViewSet
from bam_a_py.competencies_matrix.viewsets import SkillViewSet, CompetencyViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'common/users', UserViewSet)
router.register(r'competency/skills', SkillViewSet)
router.register(r'competency/competencies', CompetencyViewSet)
