---
title: Posters and Lightning Talks
layout: page
permalink: /2022/posters-talks
---

<section class="hero is-primary">
  <div class="hero-body">
    <figure class="image is-5by2">
      <img src="/assets/img/USS2022/banner.png" alt="USS 2022">
    </figure>
  </div>
</section>

# Accepted Posters and Lightning Talks

{% assign submissions = site.data.submissions_2022 | sort: "title" %}
{% for submission in submissions %}
  {% include submission-card.html %}
{% endfor %}
