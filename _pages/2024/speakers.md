---
title: Speakers
layout: page
permalink: /2024/speakers
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
<ul class="inlinelist"><li class="inlinelist"><a href="/2024/schedule.html"><button class="button is-primary">Schedule</button></a></li>  <li class="inlinelist"><a href="/2024/speakers.html"><button class="button is-primary">Speakers</button></a></li>  <li class="inlinelist"><a href="https://www.eventbrite.ca/e/unique-student-symposium-2024-tickets-865573121507"><button class="button is-primary">Registration</button></a></li>  <li class="inlinelist"><a href="/2024/poster.html"><button class="button is-primary">Poster Submission</button></a></li> <li class="inlinelist"><a href="/2024/team.html"><button class="button is-primary">USS Team</button></a></li></ul>
</center>
<br>

<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image is-5by2">
      <img src="/assets/img/USS2024/banner.png" alt="USS 2024">
    </figure>
  </div>
</section>

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
