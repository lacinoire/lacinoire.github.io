---
title: "Mind the Gap: What Working With Developers on Fuzz Tests Taught Us About Coverage Gaps"
category: ICSE-SEIP'24
category_slug: peer-reviewed
layout: publication
slug: brandt-icseseip24
type: content # video, music, photo
image: assets/img/works/moz-fuzz.png
links:
  - name: Full Publication
    url: https://carolin-brandt.de/publications/brandt-icseseip24.pdf
  - name: Presentation Slides
    url: https://carolin-brandt.de/publications/brandt-icseseip24-slides.pdf
  - name: Replication Package
    url: https://zenodo.org/doi/10.5281/zenodo.10470823
---

Carolin Brandt · Marco Castelluccio · Christian Holler · Jason Kratzer · Andy Zaidman · Alberto Bacchelli

This paper is a collaboration with Mozilla, where we try out whether we can use fuzzers to automatically generate partial input-tests that developers then complete into full functional tests with assertions.
Inspired by the feedback from developers on the initial Bugzilla reports we submitted, we then dive deeper into which kind of coverage gaps are actually relevant for developers to close.

### Abstract
Can fuzzers generate partial tests that developers find useful enough to complete into functional tests (e.g., by adding assertions)? To address this question, we develop a prototype within the Mozilla ecosystem and open 13 bug reports proposing partial generated tests for currently uncovered code. We found that the majority of the reactions focus on whether the targeted coverage gap is actually worth testing. To investigate further which coverage gaps developers find relevant to close, we design an automated filter to exclude irrelevant coverage gaps before generating tests. From conversations with 13 developers about whether the remaining coverage gaps are worth closing when a partially generated test is available, we learn that the filtering indeed removes clearly non- test-worthy gaps. The developers propose a variety of additional strategies to address the coverage gaps and how to make fuzz tests and reports more useful for developers.
