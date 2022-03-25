---
layout: page
title: Who we are
permalink: /team
---

# UNIQUE Student affairs Committee
{% assign people = site.data.teamSAC22 | sample: site.data.teamSAC22.size %}
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

{% assign people = site.data.team22 | sample: site.data.team22.size %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}
