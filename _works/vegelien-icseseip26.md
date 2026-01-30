---
title: "Addressing Test Flakiness: Practical Approaches in a Database-Reliant Industrial System"
category: ICSE-SEIP'26
category_slug: peer-reviewed
layout: publication
slug: vegelien-icseseip26
type: content # video, music, photo
image: assets/img/works/vegelien-icseseip26.png
date: 2026-04-23
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/vegelien-icseseip26.pdf
  # - name: DOI
  #   url: https://doi.org/10.1145/3639477.3639721
  # - name: Presentation Slides
  #   url: https://carolin-brandt.de/publications/brandt-icseseip24-slides.pdf
  # - name: Replication Package
  #   url: https://zenodo.org/doi/10.5281/zenodo.10470823
---

George Vegelien · Carolin Brandt · Bas Graaf · Arie van Deursen

This paper is a collaboration with Exact that resulted from George's master thesis. We looked into the test flakiness in one of Exact's systems, highlighting how important meaningful measurement and communication both with the engineers and with management is to address test flakiness.

### Abstract
Flaky tests—tests that pass or fail unpredictably even without code changes—undermine the speed and trustworthiness of modern, database-heavy software systems. This study investigates the underlying causes of flakiness at Exact, a large-scale industrial system in which shared database states and resource contention introduced frequent test instability. By repeatedly rerunning the same commit, we pinpointed recurring problem areas and implemented three targeted solutions: (1) minimizing redundant background database tasks, and two strategies for cleaning up “dirty” tests: (2) explicitly disposing of test data and (3) disabling polluting tests with a database sanity check. Together, these interventions raised Exact’s chance of a passing pipeline run from 27% to 95% and boosted their monthly release rate from 60% to 96%. Our findings confirm that rich, systematic measurement and well-prioritized fixes can significantly reduce flakiness in industrial-scale software.
