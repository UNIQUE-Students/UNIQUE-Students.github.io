---
title: Speakers
layout: page
permalink: /speakers_2021
---


<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image is-5by2">
      <img src="assets/img/banners/banner-1-v1.png" alt="{{'USS21'}}">
    </figure>
  </div>
</section>


# Speakers of the USS 2021
{% assign people = site.data.speakers %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
    {% assign side = forloop.index0 | modulo: 2 %}
      {% if side == 0 %}
        {% include speaker-card_past.html %}
      {% else %}
        {% include speaker-card_past.html %}
      {% endif %}
{% endfor %}
