---
title: Speakers
layout: page
permalink: /2021/speakers
---


<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image is-5by2">
      <img src="/assets/img/USS2021/banner-1-v1.png" alt="{{'USS21'}}">
    </figure>
  </div>
</section>


# Speakers of the USS 2021

{% assign people = site.data.speakers_2021 %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
    {% assign side = forloop.index0 | modulo: 2 %}
      {% if side == 0 %}
        {% include speaker-card_past.html %}
      {% else %}
        {% include speaker-card_past.html %}
      {% endif %}
{% endfor %}
