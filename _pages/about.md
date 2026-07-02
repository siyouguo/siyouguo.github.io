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

{% include about-me.md %}

{% include news.md %}

{% include publications.md %}
