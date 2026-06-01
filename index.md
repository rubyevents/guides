---
layout: home
title: Ruby Community Guides
---

<p class="eyebrow">Living resources for organizers</p>

# Ruby Community Guides

Everything you need to start and run a Ruby community — written by people who've done it.

You don't need a big budget, a large following, or years of event experience. You need a room, a few friendly people, and the willingness to keep showing up.

These guides were built from conversations with organizers around the world — people who booked their first venue not knowing what they were doing, cold-emailed their first speaker, and somehow ended up building lifelong connections.

{% include testimonial.html
  quote="There are rare times that you get a lot of people in a community together. It's a rare time for people to have face-to-face interaction and build health and deeper connection together. You need the technical content, because that's the affinity that draws us together. But that's not how you build relationships."
  name="Jeremy Smith"
  conference="Blue Ridge Ruby"
  avatar="/assets/images/avatars/jeremy.jpg"
  initials="JS"
%}

{% include testimonial.html
  quote="I now know all these people from doing this I didn't know before. My circle has greatly expanded, and these are people I can reach out to and ask when I have a question, or help me with a job search or help them. It's really nice to have a community."
  name="Spike Ilacqua"
  conference="Rocky Mountain Ruby"
  avatar="/assets/images/avatars/spike.jpg"
  initials="SI"
%}

## Start Here

<nav class="start-links" aria-label="Guide paths">
  <a class="start-link" href="{{ '/meetups/' | relative_url }}">
    <span class="start-link__title">Running Ruby Meetups</span>
    <span class="start-link__description">Start small, find a room, get speakers, keep going.</span>
  </a>

  <a class="start-link" href="{{ '/conferences/' | relative_url }}">
    <span class="start-link__title">Running Ruby Conferences</span>
    <span class="start-link__description">From your first venue to a room full of people who came because of you.</span>
  </a>
</nav>

## Voices behind the guides

<ul class="voices">
{% for voice in site.data.voices %}
  <li class="voice">
    {% if voice.image %}
    <img class="voice__avatar" src="{{ voice.image }}" alt="" width="32" height="32" loading="lazy">
    {% else %}
    <span class="voice__avatar voice__avatar--initials" aria-hidden="true">{{ voice.initials }}</span>
    {% endif %}
    <span class="voice__info">
      <span class="voice__name">{{ voice.name }}</span>
      <span class="voice__conference">{{ voice.conference }}</span>
    </span>
  </li>
{% endfor %}
</ul>
