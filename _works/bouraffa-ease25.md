---
title: "Not One to Rule Them All: Mining Meaningful Code Review Orders From GitHub"
category: EASE'25
category_slug: peer-reviewed
layout: publication
slug: bouraffa-ease25
type: content # video, music, photo
image: assets/img/works/bouraffa-ease25.png
date: 2025-10-23
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/bouraffa-ease25.pdf
  # - name: DOI
  #   url: https://doi.org/10.1145/3639477.3639721
  # - name: Presentation Slides
  #   url: https://carolin-brandt.de/publications/brandt-icseseip24-slides.pdf
  # - name: Replication Package
  #   url: https://zenodo.org/doi/10.5281/zenodo.10470823
---

Abir Bouraffa · Carolin Brandt · Andy Zaidman · Walid Maalej

In this paper we mine the first code review round in pull requests to understand whether we can identify developers that follow meaningful patterns.

### Abstract
Developers use tools such as GitHub pull requests to review code, discuss proposed changes, and request modifications. While changed files are commonly presented in alphabetical order, this does not necessarily coincide with the reviewer's preferred navigation sequence. This study investigates the different navigation orders developers follow while commenting on changes submitted in pull requests. We mined code review comments from 23,241 pull requests in 100 popular Java and Python repositories on GitHub to analyze the order in which the reviewers commented on the submitted changes. Our analysis shows that for 44.6% of pull requests, the reviewers comment in a non-alphabetical order. Among these pull requests, we identified traces of alternative meaningful orders: 20.6% (2,134) followed a largest-diff first order, 17.6% (1,827) were commented in the order of the files' similarity to the pull request’s title and description, and 29% (1,188) of pull requests containing changes to both production and test files adhered to a test-first order. We also observed that the proportion of reviewed files to total submitted files was significantly higher in non-alphabetically ordered reviews, which also received slightly fewer approvals from reviewers, on average. Our findings highlight the need for additional support during code reviews, particularly for larger pull requests, where reviewers are more likely to adopt complex strategies rather than following a single predefined order.
