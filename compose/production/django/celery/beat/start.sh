#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A bam_a_py.taskapp beat -l INFO
