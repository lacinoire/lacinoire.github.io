---
title: "LogChunks: A Data Set for Build Log Analysis"
category: MSR'20
category_slug: peer-reviewed
layout: publication
slug: brandt-msr20
type: content # video, music, photo
image: assets/img/works/lc.png
date: 2020-09-23
links:
  - name: Full Publication / DOI
    url: https://doi.org/10.1145/3379597.3387485
  - name: Dataset
    url: https://zenodo.org/record/3632351
---

Carolin Brandt · Annibale Panichella · Andy Zaidman · Moritz Beller

A dataset of continuous integration log files from a variety of 80 GitHub repositories and the chunk of the file that states why the build failed.

The paper was accepted at the dataset track of MSR'20, the 17th IEEE/ACM International Conference on Mining Software Repositories.

### Abstract
Build logs are textual by-products that a software build process creates, often as part of its Continuous Integration (CI) pipeline. Build logs are a paramount source of information for developers when debugging into and understanding a build failure. Recently, attempts to partly automate this time-consuming, purely manual activity have come up, such as rule- or information-retrieval-based techniques.

We believe that having a common data set to compare different build log analysis techniques will advance the research area. It will ultimately increase our understanding of CI build failures. In this paper, we present LogChunks, a collection of 797 annotated Travis CI build logs from 80 GitHub repositories in 29 programming languages. For each build log, LogChunks contains a manually labeled log part (chunk) describing why the build failed. We externally validated the data set with the developers who caused the original build failure.

The width and depth of the LogChunks data set are intended to make it the default benchmark for automated build log analysis techniques.

### Keywords
Continuous Integration · Build Log Analysis · Build Failure · Chunk Retrieval
