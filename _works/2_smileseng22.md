---
title: Incremental Just-In-Time Test Generation in Lock-Step with Code Development
category: SMILESENG Summer School
category_slug: presentations
type: content # video, music, photo
image: assets/img/works/smileseng22.png
button_url: publications/smileseng_2022_abstract.pdf
---

On the SMILESENG Summer School 2022 in Córdoba, Spain, I presented my future work idea of generating test cases right while the developer is writing their production code. With the participants we discussed the open challenges to realize such a powerful tool.

I received the award for the "best new ideas and work in progress paper" at the summer school 😊

You can find the slides [here](publications/smileseng_2022_slides.pdf).
If you want to discuss any of the mentioned challenges, shoot me an email!

### Abstract
The most common reason for Continuous Integration (CI) builds to break is failing tests. When a build breaks, a developer often has to scroll through hundreds to thousands of log lines to find which test is failing and why. Finding the issue is a tedious process that relies on a developer’s experience and increases the cost of software testing. We investigate how presenting different kinds of contextual information about CI builds in the Integrated Development Environment (IDE) impacts the time developers take to fix a broken build. Our IntelliJ plugin TestAxis surfaces additional information such as a unique view of the code under test that was changed leading up to the build failure. We conduct a user experiment and show that TestAxis helps developers fix failing tests 13.4% to 48.6% faster. The participants found the features of TestAxis useful and would incorporate it in their development workflow to save time. With TestAxis we set an important step towards removing the need to manually inspect build logs and bringing CI build results to the IDE, ultimately saving developers time.


### Keywords
Software Testing · Continuous Integration · Developer Assistance · IDE Plugin · User Experiment
