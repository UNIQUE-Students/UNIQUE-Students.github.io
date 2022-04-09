---
title: Speakers
layout: page
permalink: /speakers
---

<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image is-5by2">
      <img src="assets/img/USS2021/banner-1-v1.png" alt="{{'USS21'}}">
    </figure>
  </div>
</section>


# Monday June 7th
{% assign people = site.data.speakers %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "20210607" %}{% assign sessionright = true %}{% endif %}
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

# Tuesday June 8th
{% assign people = site.data.speakers | sample: site.data.speakers.size %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "20210608" %}{% assign sessionright = true %}{% endif %}
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

# Active breaks leader
{% assign people = site.data.speakers | sample: site.data.speakers.size %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "activebreak" %}
        {% assign sessionright = true %}
    {% endif %}
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
