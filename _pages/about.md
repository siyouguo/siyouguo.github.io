---
permalink: /
title: "Siyou Guo | About Me"
excerpt: "Ph.D. student at Hunan University, focusing on deepfake and fake news detection."
author_profile: true
redirect_from:
  - /about/
  - /about.html
--- 

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
I am a Ph.D. student at the [College of Cyber Science and Technology](http://cst.hnu.edu.cn/), [Hunan University](https://www.hnu.edu.cn/), advised by [Prof. Xin Liao](https://grzy.hnu.edu.cn/site/index/liaoxin). I received my M.S. degree from [Shandong University of Technology (SDUT)](https://www.sdut.edu.cn/) in 2026, advised by [Prof. Mingliang Gao](https://scholar.google.com/citations?user=IFEIrUgAAAAJ&hl=en), and my B.Eng. in Automation from SDUT in 2023. My research focuses on computer vision and deepfake video detection.
To date, I have completed more than 10 journal and conference papers, including 6 papers published as the first author.

<a href='https://scholar.google.com/citations?user=ZKXXk4IAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>  

<!-- My resume in Chinese is [here](assets/pdf/CV_Siyou_Guo_ZH.pdf). -->

<span class='anchor' id='-news'></span>
# 🔥 News
{% include news.md %}

<span class='anchor' id='-publications'></span>
# 📝 Publications
{% include publications.md %}

<!-- Web page click count -->
<p align="center">
  <a href="https://mapmyvisitors.com/web/1byij"  title="Visit tracker">
    <img src="https://mapmyvisitors.com/map.png?d=3jXnIbzPiVi2cKTkkTzb8VgedbRgYKa5dV7t_hn0dew&cl=ffffff" />
  </a>
</p>
