---
title: "On the Energy Cost of Static Analysis Precision: An Empirical Study of SpotBugs Effort Levels"
category: DevOpsSustain'26
category_slug: peer-reviewed
layout: publication
slug: vanderlinden-devopssustain26
type: content
image: assets/img/works/vanderlinden-devopssustain26.png
date: 2026-04-24
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/vanderlinden-devopssustain26.pdf
  # - name: Presentation Slides
  #   url: https://carolin-brandt.de/publications/vanderlinden-devopssustain26-slides.pdf
  # - name: Replication Package
  #   url: https://zenodo.org/doi/...
  # - name: DOI
  #   url: https://doi.org/...
---

Sophie van der Linden · Xutong Liu · Andy Zaidman · Carolin Brandt

### Abstract
Static analysis tools are commonly used in continuous integration
(CI) pipelines to detect potential defects without executing the
program. Such tools offer configuration options that control how
thoroughly the code is analyzed. In SpotBugs, this is done through
an effort level setting (Min, Less, More, Max), where higher levels
enable deeper and more computationally intensive analysis. In this
paper, we study how these effort levels affect energy consumption
and analysis results. Our results show that higher effort levels gen-
erally consume more energy, which fits our intuition. However, the
increase is not uniform: deeper static analysis comes with addi-
tional energy cost, but the marginal benefit of higher effort levels
may be limited in some cases. This suggests that static analysis
tool designers could make energy consumption more transparent
and provide configuration options that explicitly expose trade-offs
between analysis depth and energy cost.
