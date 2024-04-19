---
title: "Shaken, Not Stirred. How Developers Like Their Amplified Tests"
category: IEEE Transactions on Software Engineering
category_slug: peer-reviewed
layout: publication
slug: brandt-tse24
type: content # video, music, photo
image: assets/img/works/brandt-tse24.png
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/brandt-tse24.pdf
  - name: DOI / Publication in IEEE Xplore
    url: https://doi.ieeecomputersociety.org/10.1109/TSE.2024.3381015
  # - name: Presentation Slides
  #   url: https://carolin-brandt.de/publications/guided_test_amplification_SCAM_2023_slides.pdf
  - name: Replication Package
    url: https://zenodo.org/doi/10.5281/zenodo.7034924
  - name: Poster
    url: https://carolin-brandt.de/works/brandt-aliceandeve22-ictopen23
---

Carolin Brandt · Ali Khatami · Mairieli Wessel · Andy Zaidman

In this paper we conduct a large-scale open source contribution study, submitting pull requests with amplified tests to Java projects on GitHub. We analyze the feedback from the maintainers, as well as the preparations we needed to do to prepare the amplified tests for the pull requests. Based on this we collect guidelines on what developers can expect to change in amplified tests before including them in their test suite. Part of this are very helpful changes that are based on the developer's understanding of the code base and their software project, leading us to call for more support for developers to understanding amplified tests instead of focusing on further automation.

### Abstract
Test amplification makes systematic changes to existing, manually written tests to provide tests complementary to an automated test suite. We consider developer-centric test amplification, where the developer explores, judges and edits the amplified tests before adding them to their maintained test suite. However, it is as yet unclear which kind of selection and editing steps developers take before including an amplified test into the test suite. In this paper we conduct an open source contribution study, amplifying tests of open source Java projects from GitHub. We report which deficiencies we observe in the amplified tests while manually filtering and editing them to open 39 pull requests with amplified tests. We present a detailed analysis of the maintainer’s feedback regarding proposed changes, requested information, and expressed judgment. Our observations provide a basis for practitioners to take an informed decision on whether to adopt developer-centric test amplification. As several of the edits we observe are based on the developer’s understanding of the amplified test, we conjecture that developer-centric test amplification should invest in supporting the developer to understand the amplified tests.

### Keywords
Software Testing · Automatic Test Generation · Developer-Centric Test Amplification
