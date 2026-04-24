---
title: "The Energy Impact of Batch Testing in Continuous Integration: An Empirical Study of Static and Dynamic Batching Strategies"
category: DevOpsSustain'26
category_slug: peer-reviewed
layout: publication
slug: oszko-devopssustain26
type: content
image: assets/img/works/oszko-devopssustain26.png
date: 2026-04-24
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/oszko-devopssustain26.pdf
  # - name: Presentation Slides
  #   url: https://carolin-brandt.de/publications/oszko-devopssustain26-slides.pdf
  # - name: Replication Package
  #   url: https://zenodo.org/doi/...
  # - name: DOI
  #   url: https://doi.org/...
---

Máté Oszkó · Xutong Liu · Andy Zaidman · Carolin Brandt

### Abstract
Continuous integration pipelines execute automated tests on ev-
ery commit, consuming substantial energy. Batch testing, which
groups multiple commits into a single test run, has been shown to
reduce test executions in simulation studies, but no prior work has
measured whether these reductions translate into actual energy
savings. This study measures CPU package energy consumption
of CI builds under a baseline run-all approach and two batching
strategies (BatchStop4 and linear-4 lwd) across eight open-source
Java projects. BatchStop4 achieves energy savings between 57%
and 88%, while linear-4 lwd achieves savings between 59% and
94%. Energy savings correlate almost perfectly with time savings (r
>0.99), indicating that batching reduces energy primarily by short-
ening total execution time. Baseline failure rate strongly predicts
achievable savings, while CPU utilisation shows no significant re-
lationship. These findings provide empirical evidence that batch
testing effectively reduces the environmental footprint of continu-
ous integration, particularly for projects with low failure rates.
