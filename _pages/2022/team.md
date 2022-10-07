---
layout: page
title: Team of USS 2022
permalink: /2022/team
---

# UNIQUE Student Affairs Committee

{% assign people = site.data.sac_2022 | sample: site.data.sac_2022.size %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}

# Organizers of UNIQUE Student Symposium 2022

USS is organized every year by volunteer students from [UNIQUE](https://sites.google.com/view/unique-neuro-ai/home). This is the organizing team of USS 2022, in random order.

{% assign people = site.data.team_2022 | sample: site.data.team_2022.size %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}
