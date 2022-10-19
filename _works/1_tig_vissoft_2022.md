---
title: How Does This New Developer Test Fit In? A Visualization to Understand Amplified Test Cases
category: VISSOFT'22
category_slug: peer-reviewed
type: content # video, music, photo
image: assets/img/works/tig.png
button_url: publications/TIG_paper_VISSOFT_2022.pdf
---

Carolin Brandt · Andy Zaidman

In this paper we took a look at how we should build visualizations that let developers compare one test case to the rest of a test suite.

The paper was accepted at VISSOFT'22, the 10th IEEE Working Conference on Software Visualization.

**Short video introducing our visualization:** https://youtu.be/R5KDR_viFRA  
**Artifact with our implementation, replication documentation and the full codes elicited during the study:**
https://zenodo.org/record/7022610

### Abstract
Developer testing, the practice of software engineers programmatically checking that their own components behave as they expect, has become the norm in today’s software projects. With the constantly growing size and complexity of software projects and with the rise of automated test generation tools, understanding a test case is becoming more and more important compared to writing test cases from scratch.
This holds especially in the area of developer-centric test amplification, where a tool automatically generates new test cases to improve a developer-maintained test suite. To investigate how visualization can help developers understand and judge test cases, we present the TestImpactGraph, a visualization of the call tree and coverage impact of a JUnit test case proposed for amplification. It empowers the developer to drill down into the behavior of a test case, as well as providing them a clear view on how the proposed test case contributes to the coverage of the overall test suite. In a think-aloud study we investigate which information developers seek from the TestImpactGraph, how its features can support them in accessing this information, and observations regarding the coverage impact of test cases. We infer ten actionable recommendations on how developer tests can be visualized to help developers understand their behavior and impact.


### Keywords
Software Testing · Test Amplification · Test Review · Test Visualization · Test Understanding
