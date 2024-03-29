---
layout: page
title: Team of USS 2024
permalink: /2024/team
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
<ul class="inlinelist"><li class="inlinelist"><a href="/2024/schedule.html"><button class="button is-primary">Schedule</button></a></li>  <li class="inlinelist"><a href="/2024/speakers.html"><button class="button is-primary">Speakers</button></a></li>  <li class="inlinelist"><a href="https://www.eventbrite.ca/e/unique-student-symposium-2024-tickets-865573121507"><button class="button is-primary">Registration</button></a></li>  <li class="inlinelist"><a href="https://docs.google.com/forms/d/e/1FAIpQLSe1McQQJl94KUQD5rnH5T2992mQDraWf7zh68DnjP9t7JmWtA/viewform"><button class="button is-primary">Poster Submission</button></a></li> <li class="inlinelist"><a href="/2024/team.html"><button class="button is-primary">USS Team</button></a></li></ul>
</center>
<br>

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
