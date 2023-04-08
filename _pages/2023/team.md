---
layout: page
title: Team of USS 2023
permalink: /2023/team
---

# UNIQUE Student Affairs Committee

{% assign people = site.data.sac_2023 | sample: site.data.sac_2023.size %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}

# Organizers of UNIQUE Student Symposium 2023

USS is organized every year by volunteer students from [UNIQUE](https://sites.google.com/view/unique-neuro-ai/home). This is the organizing team of USS 2023, in random order.


{% assign people = site.data.team_2023 | sample: site.data.team_2023.size %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}


<!-- 
To be announced soon!
-->
