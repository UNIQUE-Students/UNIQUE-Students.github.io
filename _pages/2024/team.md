---
layout: page
title: Team of USS 2024
permalink: /2024/team
---

# UNIQUE Student Affairs Committee

{% assign people = site.data.sac_2024 | sort: "fullname" %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}

# Organizers of UNIQUE Student Symposium 2024

USS is organized every year by volunteer students from [UNIQUE](https://sites.google.com/view/unique-neuro-ai/home). This is the organizing team of USS 2024.


{% assign people = site.data.team_2024 | sort: "fullname" %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}
