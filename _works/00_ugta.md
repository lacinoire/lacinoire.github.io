---
title: "When to Let the Developer Guide: Trade-offs Between Open and Guided Test Amplification"
category: SCAM'23
category_slug: peer-reviewed
type: content # video, music, photo
image: assets/img/works/ugta.png
button_url: publications/guided_test_amplification_SCAM_2023.pdf
---

Carolin Brandt · Danyao Wang · Andy Zaidman

In this paper we compare a user-driven guided approach of test amplification to the original open test amplification approach.
While the user guidance makes it easier for the developers to understand the amplified tests, and it fits better into their typical workflow of writing tests in conjunction with production code, there are also trade-offs. For example, that now we create the expectation of being able to generate tests for the selected branch, while it can be computationally expensive to find the right branch conditions and initialize the objects under test accordingly.

### Abstract
Test amplification generates new tests by mutating existing, developer-written tests and keeping those tests that improve the coverage of the test suite. Current amplification tools focus on starting from a specific test and propose coverage improvements all over a software project, requiring considerable effort from the software engineer to understand and evaluate the different tests when deciding whether to include a test in the maintained test suite. In this paper, we propose a novel approach that lets the developer take charge and guide the test amplification process towards a specific branch they would like to test in a control flow graph visualization. We evaluate whether simple modifications to the automatic process that incorporate the guidance make the test amplification more effective at covering targeted branches. In a user study and semi-structured interviews we compare our user-guided test amplification approach to the state-of-the-art open test amplification approach. While our participants prefer the guided approach, we uncover several trade-offs that influence which approach is the better choice, largely depending on the use case of the developer.

### Keywords
Software Testing · Test Amplification · Automated Test Code Modification · User-centric Design · Human-Automation Interaction
