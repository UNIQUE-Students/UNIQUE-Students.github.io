---
layout: page
title: Team of past editions of USS
hero_height: is-small
permalink: /2021/team
---

<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image is-5by2">
      <img src="/assets/img/USS2021/banner-1-v1.png" alt="{{'USS21'}}">
    </figure>
  </div>
</section>


# Organizers of USS 2021

{% assign people = site.data.team_2021 | sample: site.data.team_2021.size %}
{% for person in people %}
    {% include team-card_past.html %}
{% endfor %}
