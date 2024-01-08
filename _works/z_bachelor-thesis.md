---
title: "A Description Language for Structural Smells"
category: Bachelor Thesis
category_slug: more
layout: publication
slug: brandt-bachelor-thesis
type: content # video, music, photo
image: assets/img/works/bt.png
links:
  - name: Full Thesis
    url: https://carolin-brandt.de/publications/bachelor_thesis.pdf
---

In my bachelor thesis I designed a domain specific language to express structural smells in natural-language requirements documents.
Main conclusion: split the location definition from defining how that smell should look.

### Abstract
High quality requirements artifacts are an important factor in the engineering process of any product, since quality defects within these artifacts are costly to resolve. Therefore many companies try to standardize their requirements artifacts by providing templates and guidelines on how requirements should be documented. These aim at standardizing the structure of requirements and making them easier to understand for all readers, so they can find the information they are looking for faster.
Conformance to these guidelines is still checked with manual reviews. These reviews are however very costly in terms of time the stakeholders and reviewers have to invest. The reviews’ quality also greatly depends on how skilled the respective stakeholder is to assess requirements quality. Combining manual reviews with automatic ones can speed up this process. At the moment, there is no structured language to define structural guidelines for requirements artifacts so that they can be automatically quality assured.
To address this shortcoming, we collect different kinds of structural rules that are defined in guidelines for writing requirements used in industrial practice. From the collected rules we infer structural requirements smells. These can be used to detect structural defects within requirements artifacts. We develop a domain specific language to configure an automated analysis of requirements artifacts that detects structural defects. With this language, the user can define the structure, to which an artifact has to conform to. In addition, the user can specify how the author has to be warned about potential quality defects in his requirements documentation. To evaluate our domain specific language, we take rules from existing requirements authoring guides and assess to which extent they can be described by our language. Our analysis found that we can already describe 69% of the structural rules describe in selected guidelines used in industrial practice. Further possible extensions to our language are described at the end of the thesis.
