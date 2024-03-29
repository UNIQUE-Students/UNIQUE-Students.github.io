---
title: Speakers
layout: page
permalink: /2024/speakers
---

<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image is-5by2">
      <img src="/assets/img/USS2024/banner.png" alt="USS 2024">
    </figure>
  </div>
</section>


# Wednesday, 8th May

{% assign people = site.data.speakers_2024 %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "20240508" %}{% assign sessionright = true %}{% endif %}
    {% if session contains "activebreak" %}{% assign sessionright = false %}{% endif %}
  {% endfor %}
    {% if sessionright %}
      {% assign side = forloop.index0 | modulo: 2 %}
        {% if side == 0 %}
          {% include speaker-card.html %}
        {% else %}
          {% include speaker-card.html %}
        {% endif %}
    {% endif %}
{% endfor %}

# Thursday, 9th May

{% assign people = site.data.speakers_2024 %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "20240509" %}{% assign sessionright = true %}{% endif %}
    {% if session contains "activebreak" %}{% assign sessionright = false %}{% endif %}
  {% endfor %}
    {% if sessionright %}
      {% assign side = forloop.index0 | modulo: 2 %}
        {% if side == 0 %}
          {% include speaker-card.html %}
        {% else %}
          {% include speaker-card.html %}
        {% endif %}
    {% endif %}
{% endfor %}

# Friday, 10th May

{% assign people = site.data.speakers_2024 %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "20240510" %}{% assign sessionright = true %}{% endif %}
    {% if session contains "activebreak" %}{% assign sessionright = false %}{% endif %}
  {% endfor %}
    {% if sessionright %}
      {% assign side = forloop.index0 | modulo: 2 %}
        {% if side == 0 %}
          {% include speaker-card.html %}
        {% else %}
          {% include speaker-card.html %}
        {% endif %}
    {% endif %}
{% endfor %}
