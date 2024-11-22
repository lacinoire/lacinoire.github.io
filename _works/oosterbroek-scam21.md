---
title: Removing Redundant Statements in Amplified Test Cases
category: SCAM'21
category_slug: peer-reviewed
layout: publication
slug: oosterbroek-scam21
type: content # video, music, photo
image: assets/img/works/rrs.jpeg
date: 2021-09-23
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/RS_paper.pdf
---

Wessel Oosterbroek · Carolin Brandt · Andy Zaidman

This paper proposes minimization approach for amplified test cases based on first drastically then step by step more conservatively removing statements while checking that the improvement in mutation score remains the same.

The paper was accepted at the NIER track of SCAM'21, the IEEE International Working Conference on Source Code Analysis and Manipulation.

### Abstract
Test amplification generates new tests by modifying existing, manually written tests. Up until now, this process preserves statements that were relevant for the original test case but are no longer needed for the behavior of the new test case. These unnecessary statements impact the readability of the tests in question. As a part of the effort to make amplified test cases more readable, we investigate dynamic slicing, taint analysis and static analysis as approaches to remove redundant statements. We design and evaluate a static analysis approach that we implemented as part of the test amplification tool DSpot. Our empirical evaluation on 274 amplified test cases shows that the implemented approach works well: while being rudimentary, it is able to remove a significant portion of the redundant statements in the amplified test cases. While the removal of the statements themselves is fast, verifying that the tests still work as intended through mutation testing is still resource-intensive.
