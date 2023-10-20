---
layout: page
title: Who we are
permalink: /team
---

# UNIQUE Student Affairs Committee

{% assign people = site.data.sac_2024 | sort: "name" %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}
