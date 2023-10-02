---
title: Incremental Just-In-Time Test Generation in Lock-Step with Code Development
category: SMILESENG Summer School
category_slug: presentations
layout: publication
slug: brandt-smileseng22
type: content # video, music, photo
image: assets/img/works/smileseng22.png
links:
  - name: Full Publication
    url: publications/smileseng_2022_abstract.pdf
---

On the SMILESENG Summer School 2022 in Córdoba, Spain, I presented my future work idea of generating test cases right while the developer is writing their production code. With the participants we discussed the open challenges to realize such a powerful tool.

I received the award for the "best new ideas and work in progress paper" at the summer school 😊

You can find the slides [here](publications/smileseng_2022_slides.pdf).
If you want to discuss any of the mentioned challenges, shoot me an email!

### Abstract
State-of-the-art test generation strategies employ advanced analyses of the code under test and powerful optimization
algorithms to generate automatic test cases for software systems.
As these techniques require a large amount of computational
power, they are often limited to generating tests after the code
under test is already written. However, today’s broad education
about the importance of software testing lets developers strive to
create test cases directly with new code they are contributing.
To support these developers, we want to develop an incremental just-in-time test generation tool that works in close
proximity to the development of the code under test. Whenever
the developer creates a new class or functionality, the tool
automatically proposes a matching test case. When the developer
finishes implementing a new condition, the tool automatically
recommends an additional test case that tests the code which
was just added. The generated test cases are closely based on the
existing test cases in the project with small, incremental changes
to test the new lines of code.
To realize such a just-in-time test generation tool we have to
tackle many challenges: Detecting the completion of a test-worthy
condition, generating a fitting test case in a short time on the
developer’s machine, or effectively communicating the value of
the new test case to the developer. With the participants of the
SMILESENG Summer School we want discuss our new idea,
brainstorm on the challenges that this research opens up and
identify possible approaches to tackle them.


### Keywords
Software Testing · Automatic Test Generation · Test-Guided Development · Developer-Centric Design
