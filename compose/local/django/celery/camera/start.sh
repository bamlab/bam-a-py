#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A bam_a_py.taskapp events -l info -b redis://redis:6379/0 --camera django_celery_monitor.camera.Camera --frequency=2.0
