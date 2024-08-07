#!/usr/bin/bash

python ../manage.py graph_models \
    -a \
    -X '*Session|ContentType|PolymorphicModel|Group|Permission|LogEntry' \
    --color-code-deletions \
    --hide-edge-labels \
    -o ../media/models.png
