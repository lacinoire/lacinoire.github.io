---
title: "Towards Refined Code Coverage: A New Predictive Problem in Software Testing"
category: ICST'25
category_slug: peer-reviewed
layout: publication
slug: brandt-icst25
type: content # video, music, photo
image: assets/img/works/brandt-icst25.png
date: 2025-01-23
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/brandt-icst25.pdf
  # - name: DOI
  #   url: https://doi.org/10.1145/3639477.3639721
  - name: Presentation Slides
    url: https://carolin-brandt.de/publications/brandt-icst25-slides.pdf
  - name: Replication Package
    url: https://anonymous.4open.science/r/understanding-covered-code-4950
---

Carolin Brandt · Aurora Ramírez

This paper introduces a novel way to look at code coverage in software testing: can we predict it based on the code?
Our idea is to learn from existing code coverage in open source projects what characterizes code that developers find it worth to cover with tests.

### Abstract
To measure and improve the strength of test suites,
software projects and their developers commonly use code
coverage and aim for a threshold of around 80%. But what is the
80% of the source code that should be covered? To prepare for
the development of new, more refined code coverage criteria, we
introduce a novel predictive problem in software testing: whether
a code line is, or should be, covered by the test suite. In this short
paper, we propose the collection of coverage information, source
code metrics, and abstract syntax tree data and explore whether
they are relevant to predict whether a code line is exercised by
the test suite or not. We present a preliminary experiment using
four machine learning (ML) algorithms and an open source Java
project. We observe that ML classifiers can achieve high accuracy
(up to 90%) on this novel predictive problem. We also apply an
explainable method to better understand the characteristics of
code lines that make them more “appealing” to be covered. Our
work opens a research line worth to investigate further, where the
focus of the prediction is the code to be tested. Our innovative
approach contrasts with most predictive problems in software
testing, which aim to predict the test case failure probability.
