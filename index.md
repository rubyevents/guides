---
layout: home
title: Ruby Community Guides
---

<div class="index-intro" markdown="1">

Living resources for organizers
{: .eyebrow }

# Ruby Community Guides

Everything you need to start and run a Ruby community — written by people who've done it.

You don't need a big budget, a large following, or years of event experience. You need a room, a few friendly people, and the willingness to keep showing up.

These guides were built from conversations with organizers around the world — people who booked their first venue not knowing what they were doing, cold-emailed their first speaker, and somehow ended up building lifelong connections.

</div>

<aside class="index-rail" aria-label="Guides">
  <div class="index-rail__guides">
    <p class="toc__heading">The guides</p>
    <ul class="toc__list">
      <li class="toc__item"><a class="toc__link index-rail__link" href="{{ '/meetups/' | relative_url }}">Running Ruby Meetups</a></li>
      <li class="toc__item"><a class="toc__link index-rail__link" href="{{ '/conferences/' | relative_url }}">Running Ruby Conferences</a></li>
    </ul>

    <p class="toc__heading index-rail__heading">Resources</p>
    <ul class="toc__list">
      <li class="toc__item"><a class="toc__link index-rail__link" href="{{ '/interviews/' | relative_url }}">The Interviews</a></li>
    </ul>

  </div>

  <div class="index-note">
    <p class="toc__heading">Work in progress</p>
    <p class="index-note__text">Still being written and refined. If you have organizing experience to share — or a question you wish they answered — help shape what comes next.</p>
    <a class="index-note__cta" href="https://github.com/{{ site.github_repo }}">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 0C5.373 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.562 21.8 24 17.302 24 12 24 5.373 18.627 0 12 0z"/></svg>
      Contribute on GitHub
    </a>
  </div>
</aside>

<div class="index-body" markdown="1">

{% include testimonial.html
  class="testimonial--plain"
  quote="There are rare times that you get a lot of people in a community together. It's a rare time for people to have face-to-face interaction and build health and deeper connection together. You need the technical content, because that's the affinity that draws us together. But that's not how you build relationships."
  name="Jeremy Smith"
  conference="Blue Ridge Ruby"
  avatar="/assets/images/avatars/jeremy.jpg"
  initials="JS"
%}

<nav class="start-links index-mobile-guides" aria-label="Guide paths">
  <a class="start-link" href="{{ '/meetups/' | relative_url }}">
    <span class="start-link__title">Running Ruby Meetups</span>
    <span class="start-link__description">Start small, find a room, get speakers, keep going.</span>
  </a>
  <a class="start-link" href="{{ '/conferences/' | relative_url }}">
    <span class="start-link__title">Running Ruby Conferences</span>
    <span class="start-link__description">From your first venue to a room full of people who came because of you.</span>
  </a>
  <a class="start-link start-link--resource" href="{{ '/interviews/' | relative_url }}">
    <span class="start-link__title">The Interviews</span>
    <span class="start-link__description">Read the organizer conversations behind the guides.</span>
  </a>
</nav>

## Voices behind the guides

<p class="voices-intro">These guides are built from full conversations with organizers who have started, sustained, revived, and scaled Ruby communities around the world.</p>

<p class="voices-cta"><a href="{{ '/interviews/' | relative_url }}">Read the full interviews</a></p>

<ul class="voices">
{% for voice in site.data.voices %}
  <li class="voice">
    {% if voice.image %}
    <img class="voice__avatar" src="{{ voice.image | relative_url }}" alt="" width="32" height="32" loading="lazy">
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

</div>
