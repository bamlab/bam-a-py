from django.apps import AppConfig


class CompetenciesMatrixConfig(AppConfig):
    name = 'bam_a_py.competencies_matrix'
    verbose_name = "Competencies matrix"

    def ready(self):
        pass
