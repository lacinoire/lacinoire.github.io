---
title: Fixing Continuous Integration Tests From Within the IDE With Contextual Information
category: ICPC'22
category_slug: peer-reviewed
layout: publication
slug: boone-icpc22
type: content # video, music, photo
image: assets/img/works/testaxis_cut.png
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/TestAxis_icpc22.pdf
  - name: Presentation Recording
    url: https://youtu.be/m-h5k7tGNsw?si=lBrCISjIY-RB7dN7
  - name: Code on GitHub
    url: https://github.com/testaxis
  - name: Replication Package
    url: https://zenodo.org/record/5526015
  - name: Casper's Master Thesis
    url: https://repository.tudelft.nl/islandora/object/uuid:f8375d5f-3bbd-4559-863b-6951e9d6bab0?collection=education
  - name: Paper DOI
    url: https://doi.org/10.1145/3524610.3527908
---

Casper Boone · Carolin Brandt · Andy Zaidman

This paper discusses a plugin that brings information from the CI to the developer's IDE to help them fix failing tests faster.
It is based on Casper Boone's excellent Master Thesis, who I had the pleasure to supervise in 2020/21.

The paper was accepted at ICPC'22, the 30th IEEE/ACM International Conference on Program Comprehension [(DOI)](https://doi.org/10.1145/3524610.3527908).

### Abstract
The most common reason for Continuous Integration (CI) builds to break is failing tests. When a build breaks, a developer often has to scroll through hundreds to thousands of log lines to find which test is failing and why. Finding the issue is a tedious process that relies on a developer’s experience and increases the cost of software testing. We investigate how presenting different kinds of contextual information about CI builds in the Integrated Development Environment (IDE) impacts the time developers take to fix a broken build. Our IntelliJ plugin TestAxis surfaces additional information such as a unique view of the code under test that was changed leading up to the build failure. We conduct a user experiment and show that TestAxis helps developers fix failing tests 13.4% to 48.6% faster. The participants found the features of TestAxis useful and would incorporate it in their development workflow to save time. With TestAxis we set an important step towards removing the need to manually inspect build logs and bringing CI build results to the IDE, ultimately saving developers time.


### Keywords
Software Testing · Continuous Integration · Developer Assistance · IDE Plugin · User Experiment
