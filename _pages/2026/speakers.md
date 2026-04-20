---
title: Speakers
layout: page
permalink: /2026/speakers
---

<style>
.inlinelist ul {
  display: inline;
  list-style: none;
}

.inlinelist li {
  display: inline;
  padding: 3px 5px 3px 5px
}

@media only screen and (max-width: 665px) {
  .inlinelist ul {
    display: block;
    list-style: none;
  }

  .inlinelist li {
    display: block;
    padding: none;
  }
}
</style>
<br>
<center>
<ul class="inlinelist"><li class="inlinelist"><a href="/2026/schedule.html"><button class="button is-primary">Schedule</button></a></li>  <li class="inlinelist"><a href="/2026/speakers.html"><button class="button is-primary">Speakers</button></a></li>  <li class="inlinelist"><a href="/2026/poster.html"><button class="button is-primary">Poster Submission</button></a></li> <li class="inlinelist"><a href="/2026/team.html"><button class="button is-primary">USS Team</button></a></li></ul>
</center>
<br>

<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image">
      <img src="/assets/img/USS2026/USS_poster_EN.png" alt="USS 2026" style="width: 100%;">
    </figure>
  </div>
</section>

# Tuesday, 12th May

{% assign people = site.data.speakers_2026 %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "20260512" %}{% assign sessionright = true %}{% endif %}
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

# Wednesday, 13th May

{% assign people = site.data.speakers_2026 %}
{% for person in people %}
  {% if person.fullname == "TBA" %}{% continue %}{% endif %}
  {% for session in person.sessions %}
    {% assign sessionright = false %}
    {% if session contains "20260513" %}{% assign sessionright = true %}{% endif %}
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
