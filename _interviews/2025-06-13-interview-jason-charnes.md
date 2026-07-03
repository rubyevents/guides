---
title: Jason Charnes and Southeast Ruby
voice: jason-charnes
host: travis-dockter
date: 2025-06-13
source_url: https://rubyconferenceproject.com/2025-06-13-interview-jason-charnes/
teaser: >-
  Jason Charnes talks through the early decisions behind Southeast Ruby, from starting small and finding sponsors to making a regional Ruby event feel real.
links:
  - label: "Jason's Blog"
    url: https://www.jasoncharnes.com/
  - label: "Jason's X"
    url: https://www.x.com/jmcharnes
  - label: "Jason's Blog Post after the first year of Southeast Ruby"
    url: https://jasoncharnes.com/organizing-southeast-ruby/
  - label: "Jason's conversation with Jason about conferences"
    url: https://www.codewithjason.com/podcast/10094963-134-behind-the-scenes-of-conference-organizing-with-jason-charnes/
highlights:
  - title: "Workshops as a separate day"
    anchor: workshops-separate-day
  - title: "Reaching keynote speakers cold"
    anchor: cold-keynote-outreach
  - title: "Losing money the first year"
    anchor: losing-money-first-year
  - title: "Finding sponsors and Honeybadger"
    anchor: sponsors-and-honeybadger
  - title: "The 30-minute break format"
    anchor: thirty-minute-break-format
---

**Travis:** Okay, cool. Well, welcome to what I've been calling my unofficial, unprofessional interviews of conference organizers. So, a little bit of context: I decided that I'm going to organize my own Rails conference, and I wanted to reach out to a bunch of other conference organizers and just try to soak up their knowledge, get their experience, and ask them all kinds of questions about how they did what they did.

I know that you organized Southeast Ruby a couple times, and you actually wrote a really awesome blog post after the first one called "Organizing My First Conference: Southeast Ruby." I also listened to, I think, a podcast you did with Jason Swett on organizing Ruby conferences. So I think I'll skip over the whole story of you organizing that, but I want to dive a little bit deeper than maybe what that blog post was.

Just to clarify, though, was that first one a two-day conference or a one-day conference?

**Jason:** It was two-day. I think all of them were two-day.

**Travis:** They were two days. Okay. How many speakers did you have? I think it was like four keynote and then ten other talks. Did you have like fourteen speakers in two days?

**Jason:** Roughly, yeah. It alternated. I want to say it probably alternated some each year. The last year, we added some workshops in.

**Travis:** Okay. Cool. Workshops. What were the workshops?

**Jason:** Let's see here. Jason Swett came and gave one. It's been so long. I pulled this up. 2019, if it will load. Oh, connection private. Yeah. So Jason gave one on cleaning up legacy code, and Ernesto Tagwerker gave one on upgrading Rails. Then, oh, we actually had four that year. Noah Gibbs gave one on building your own web framework, and then Julian Fahrer and James Hart gave one on dockerizing Rails.

**Travis:** Nice. How did you like having those versus speakers?

<span id="workshops-separate-day" class="interview-anchor"></span>

**Jason:** I liked it. I forgot this year. Thursday was just workshops, and then Friday was just talks.

**Travis:** Oh, okay. So split up.

**Jason:** Yeah, it was split up. My understanding was that the attendees enjoyed that. I also wanted it to be where, when we go to big conferences, workshops compete with regular talks. They run side by side. We had two workshops running side by side, but it wasn't like, if I go to this workshop, I miss these two talks kind of thing. I think that went pretty well.

**Travis:** Cool. Yeah, no, that sounds like a great idea to me. For the workshops, did you open a CFP for those workshops, or did you reach out to people and say, hey, will you do this workshop?

**Jason:** I want to say it was in the CFP.

**Travis:** Oh, okay.

**Jason:** Yeah, it definitely was, because the people who did the dockerizing Rails one, I didn't know them before, so it would have definitely been.

**Travis:** Okay, cool. So you're like, call for talks, or if you want to do a workshop kind of a thing.

**Jason:** Yeah. And we did the workshop as an add-on. So you could just buy the conference ticket for the one day, but it was like an additional $80 to do the workshop.

**Travis:** Oh, okay, cool. I'm assuming for the workshop people that was the same kind of deal that the speakers got, like you would pay for their travel or something like that?

**Jason:** Yeah. We weren't able to fully pay for travel. The first year we paid for hotel rooms for speakers, and we lost, I mean, my wife and I lost so much money the first year that we were just like, we can't do this. I want to say we spent like seven or eight grand on hotel rooms the first year.

**Travis:** Yeah.

**Jason:** Running these small conferences—I mean running any conference, really—margins are small. But the workshops, if I remember correctly, they, much like the speakers, get a stipend. If we invite you to do a keynote, I think we'd do a little extra, because we invited you. I want to say maybe we did hotels for keynotes, but I can't exactly remember.

**Travis:** Okay. So for the first one specifically, I have more interest in that sometimes, because I like to hear about how people were thinking when they didn't know anything, and then maybe their reflections on that and how they would have changed stuff. But on that first one, when you reached out to your keynote speakers, do you remember if you already had connections with those people, or were you reaching out cold to get keynote speakers?

<span id="cold-keynote-outreach" class="interview-anchor"></span>

**Jason:** I was mostly reaching out cold. So Avdi Grimm, I did not know personally. We may have met at a Ruby conference or something like that. But at the time he was living in Knoxville, Tennessee, and it felt perfect. Like, hey, he could drive to it, right? Because of that, Avdi spoke every year as a keynote. It was cool. He called it his home conference.

Ben Orenstein, I met in person at MicroConf that same year, earlier in the year, and so I asked him in person. He was like, yeah, I'll do it. Ernie Miller, I don't actually think so. I knew of Ernie. I'd seen him talk. I loved Ernie, but I don't think we knew each other personally yet. But he was in Louisville at the time, which is a couple hours north of Nashville, and so he was like, yeah, I'd love to do it. And then Kinsey, I want to say we might have known each other through conferences before that.

But yeah, if I did know anyone, it couldn't have been like we were at this level. But everybody I asked was super receptive.

**Travis:** Awesome. That's cool to hear. What was the timeline on that first one? In the blog post, it says you had your paternity leave idea, probably your sleep-deprived crazy idea, in December 2016. And then when was that actual first conference?

**Jason:** That conference was in October of that year.

**Travis:** Okay. And when did you start working on it in earnest? How long was that?

**Jason:** We started pretty early in the year. There was only so much upfront we could do. Once we locked down the dates and the venue, we did that as early as we could. As an important thing to maybe note, it doesn't really matter, but we live in Memphis and the conference was in Nashville, and that's like a three-hour drive from us. So we went up there, looked at a venue, things like that, and locked that down probably March or April, if I had to guess.

Then it was a lot of sitting and waiting, watching ticket sales. They trickled in slowly. They kind of didn't ramp up till towards the end. So it's kind of like, oh, shit, is anyone going to be here? On and off throughout the year, but really the majority of work was at the beginning, and then definitely a couple of days before the conference, we were just in go mode.

**Travis:** Gotcha. How did you market it? In the blog post, it says you had some social media, RubyFlow, Reddit.

**Jason:** I forgot about RubyFlow. Yeah. I just put it out there. I put it on RubyConferences.org.

**Travis:** Did how you marketed change from the first year to the last year? Did you learn anything?

**Jason:** Not particularly. I didn't particularly change anything, but having the first year under our belt had established the conference as legitimate. People had actually come to this thing, had taken pictures, tweeted about it. Not like it was this huge popular conference, just that the next year, when it rolled around and we're like, hey, Southeast Ruby, it wasn't like—some people were like, oh, I've heard about that before, things like that.

**Travis:** Right. Gotcha. At the end of your post, you wrote a couple ideas that I wanted to ask you about now, to see if you applied them or had changed your mind on them or anything. So at the end of the post, one of the ideas you put was you wish you would have offered more tickets to people who wouldn't be able to attend conferences normally. Were you able to do that in later years? And how did you?

**Jason:** I'm trying to think. We were able to work with people with discounts and stuff if they write in. We gave away some sponsorship. One thing we actually did was bake in sponsorships, like, if you want to donate, giving away a ticket, things like that.

**Travis:** Right.

**Jason:** So we did that in later years. I was glad we did that. It's surprising how hard it is to give away free tickets, though, because it involves travel. A lot of times we'd be like, hey, here's a free ticket. They're like, oh, thanks, I can't make it. So you kind of cycle through the list.

**Travis:** Yeah. I think I read in the first year the tickets were like $175 or something like that. Did ticket prices go up, or did you keep it? Because that was actually a pretty cheap conference ticket, and I think that's really cool. I would like to keep ticket prices lower, so that hopefully more people are able to do it. Did that change at all?

<span id="losing-money-first-year" class="interview-anchor"></span>

**Jason:** It did. My wife and I funded the conference. We lost almost ten grand the first year. Luckily, I had some side consulting I had done and was able to write that off on my taxes, which helped. So we had to raise the price. I can't remember what it was in 2018, but by 2019 I'm pretty sure it went up to like $295. I could be getting that wrong.

**Travis:** I maybe am making the same mistake that you did the first year, but I'm looking at my venue price and I'm looking at some other prices, and I'm like, I think I could do this. I think I could keep my tickets under $200. I think something that you did the first year that you mentioned that you regretted was like room block and catering.

**Jason:** We actually didn't use a hotel the first two years, so we didn't have a room block. That was the year that we did pay for all speakers' hotels, and that was really our biggest expense.

**Travis:** You catered as well.

**Jason:** We had lunch catered. There are a lot of conferences afterwards that I went to that were like, you're on your own for lunch. I was like, damn, that's good. I wish we had. Still, all three years, we never did that, and I wish we would have. But by the third year, we kind of dialed in what we were going to spend. Something that helped, again, I think, after the first year, being established, and putting that in air quotes, it was easier—not easy, but easier—to get sponsors the next two years.

I think one year we had someone from DockYard write a blog post on the DockYard blog about the conference, and that was wonderful. It felt good that somebody liked it enough to do that. But all that stuff helped.

**Travis:** Yeah. How did you get sponsors that first year? Was that another just reaching out cold and you got lucky, or did you have some connections that helped there?

<span id="sponsors-and-honeybadger" class="interview-anchor"></span>

**Jason:** The first year, sponsors was tough. I'm looking at the list of sponsors. Honeybadger sponsored, I want to say they may have sponsored one of the after-parties. We did an open bar, and we did that at the venue. Hired bartenders, things like that.

Ramsey Solutions—so that's Dave Ramsey, the money guy. His company's whole operation is in Nashville, and they used to do a lot of Ruby. I don't know if they do anymore.

**Travis:** Really? I didn't know that.

**Jason:** Yeah, they were a big Rails shop. I want to say they sponsored financially as well. But what was really cool about working with them is they were like, hey, we're sending our employees, a handful of them, but also we're sending them to help. So if you need help setting up, so many wonderful individuals too. There's a guy named John Sloan. We became friends. We stayed in touch for a while. He was there all three years. Just great.

And Clear Function. They're a local company here in Memphis. They sponsored. But those were the three, if I remember, kind of like—I don't want to use the term lower-level. It just wasn't high monetary sponsorships, right? They were super helpful, but...

**Travis:** They weren't like huge companies donating.

**Jason:** They weren't like, oh, here's a $10,000 sponsorship, right? The other three were Icelab, Ambu Labs, and Prompt. Icelab and Ambu Labs were sponsors because they paid for travel for their speakers. And so I was like, hey, if you'll do that, I'll list you as a sponsor. And then Prompt actually merged with Open Sourcing Mental Illness. It's a kind of awareness nonprofit for mental health with developers. I had a personal connection. There's a developer here in Memphis who helps manage it.

I kind of tell you all the sponsors just to give you an idea. Just because they were listed as a sponsor, it for sure didn't mean it was necessarily directly financial, or even like, why did you lose so much money? It was very helpful. We just mismanaged the whole thing. No, we didn't know what we were doing.

**Travis:** Yeah, gotcha. So one of the—oh, go ahead.

**Jason:** Shout out to Honeybadger for sponsoring that after-party, because also I had no idea how much alcohol to buy. I ended up bringing boxes home, and friends would come over and be like, are you sure you don't want a whole handle of gin? You don't want to take this home?

**Travis:** You want to take a box.

**Jason:** You don't want to take this home?

**Travis:** Another thought that you put down at the end of that very first blog post was, make sponsorship more affordable and appealing. Did you?

**Jason:** Yeah, that is actually why we didn't have sponsors the first year too, is we did it too high. When you said at the beginning of this call, you wrote a blog post, I hadn't even thought about that blog post in like four years.

I want to say Ramsey became a sponsor because they're like, we're going to buy X number of tickets in exchange for our logo kind of thing. Clear Function might have been our only sponsor. Honeybadger was for the after-party. So the next years, we released a prospectus for sponsorship. The next year, actually, Ernie Miller, who was a keynote speaker the first year, was like, I love this. I want to help you. So he actually became a co-organizer with us, and he handled all the sponsorships that year too.

We put the prospectus together. I might even be able to find it. But we had more tiers. Do you want to buy a ticket for someone in the community? Do you just want your logo on the website? Do you want shout-out things like that? And so the next year we had much more in terms of sponsorship. Shipt was a sponsor. They're a shop in Alabama now, and then we had a couple of bronze sponsors. We had one company do the scholarship, so we actually split it up into real tiers, and that went a lot better.

By the last year, we didn't have as many sponsors, but 360, Bold Penguin, The Easy—these companies sponsored pretty high financially. And Honeybadger actually sponsored. Did they do all three years? I know for sure Honeybadger did the last year. This is my favorite thing about Honeybadger sponsorships: any conference you go to, they sponsor. It's not like a traditional sponsorship. They actually were like, hey, find something you need to do. So we got an ice cream truck to come to the conference, and we all went outside and had ice cream. I'd be remiss if I didn't sit here and talk about Honeybadger, because it's not like they sponsor—you know, I was on a podcast called Remote Ruby. It still goes, but they were our first and really only sponsor. And as far as I know, they're still sponsoring the podcast. They're just really good for the community. But I digress.

**Travis:** Yeah. You see them everywhere on sponsorship stuff. They give back a lot.

**Jason:** Yeah.

**Travis:** Another thought that you put down at the end of that was incorporate families more. What did you mean by that? And were you able to do anything around that in later years?

**Jason:** Not really. We did the conference on Thursday, Friday, I think every year. The idea was spend the weekend in Nashville if you want to. So there was always kind of the hope that that would happen. Could we provide childcare, things like that? But we were just so small. I saw RubyConf do that, I thought, oh, that's cool. I want to do that. But there's no way in hell I could afford to do that.

My son wasn't even one at the time we had that conference, but he was there with me. I think that was my oldest. That was probably a big motivator for me to want to include that more. But I don't know. There's also something beautiful about having some time away, so I don't know.

**Travis:** True. Yeah. I'm thinking of doing my conference in the summer. I'm trying to think about, okay, kids are out of school. If people want to make it a trip to exotic Albuquerque, New Mexico, how can I do a little bit more to make that easier?

**Jason:** I get that. It's a tough balance.

**Travis:** On that same blog post, the very last thought you put was, have co-organizers or more volunteers. Obviously, you just mentioned that the very next year you had a co-organizer. How did you guys split up responsibilities?

**Jason:** Good question. So Ernie did join us, and I took a lot of credit for Southeast Ruby, but I deserved probably none of it other than I was like, oh, I want to do this. Because really my wife was like a co-organizer. She had just become a stay-at-home mom, and so that freed her up a little bit to help with it. The first year, it was us at Costco the day before, spending a thousand dollars on things.

So we learned how to delegate a little bit more of that stuff. We also started offering volunteer tickets explicitly for free in exchange for showing up early, helping, being available. I think we did that. If we didn't do it the first year, we definitely did the second and third. I was really inspired to do that because of the Ramsey Solutions folks that first year. They were just super helpful.

Actually, the second year, this is a little bit of a digression, but the second year Ramsey Solutions was the actual venue. We had the conference at their old location. They had an event space that was hard to describe in terms of size. Imagine the size of a basketball gym or something like that. Full stage, lights, audio. They were like, yo, we want to have it here. They didn't charge us, and so that's why they were the diamond sponsor.

**Travis:** Amazing.

**Jason:** It wasn't Nashville proper, per se. It was Brentwood, technically. But people came, and that was a really successful one. We had a lot of help that year, because again, they were like, you're doing it here. Any employees that are going to attend the conference can help.

Ernie and I kind of split. He did more of the sponsorship. We came up with the prospectus together, but he handled more of the outreach or the finalizing the deals, things like that. We always did the CFP together. We also had some help doing the CFPs. I know Jacob Herrington helped us one year. He's a buddy of mine in Arkansas. We had some miscellaneous people help us with that because we didn't necessarily want it to just be me and Ernie doing it. We wanted more input.

**Travis:** Yeah.

**Jason:** I met a lot of really good people that I wouldn't have known outside of that by having them come speak, which is kind of the whole idea of the CFP. So I wouldn't say that I would have thrown it out. But I think if I were to do it again, I might try the Jason Swett style, where he doesn't do a CFP. He's just like, do you want to come talk? Do you want to come talk? I probably am aware of enough people in the community that I could pull that off. But at the same time, I don't know. There are more people that I would get to meet with the CFP.

Again, I digress. But to the question of volunteers, what do we do? When it came to the actual venue, Ernie and I and Shannon would all look together. Sponsorships, we did that earlier. Food and managing all that, Shannon, my wife, usually did most of that. So we were a pretty good team. Ernie is one of the finest humans in the world. I think everybody who's ever worked with him in any capacity says that.

**Travis:** Nice. I had another question. I lost it. Oh, the first year in the blog post, you mentioned you sold 87 tickets. How much bigger did it get over the years? Did you ever sell out?

**Jason:** No, never sold out. The second year we had ample amount of space. For all intents and purposes, we broke even. I can't remember the number of tickets we sold, but it surpassed 100. I think the second year was our biggest year. The third year did really well too. The third year, we finally did do a hotel. We did one downtown Nashville, and we used their event space. So even if it wasn't more tickets than the second or first year, the space was a little smaller, so it felt packed. It felt full. It was cool.

**Travis:** Yeah, it was over a hundred, both those other, the second and third years?

**Jason:** I want to say, if it wasn't, it was around there. It was pretty steady. Every time I give you a number, I'm going to include the 15 speakers too, right? So you at least have 15 people at your conference, no matter what. We stayed pretty steady. We were fortunate in that regard. We did three arguably vastly different conferences because we changed locations pretty dramatically within Nashville all three times. So we were pretty fortunate.

**Travis:** Nice. Can you think of anything that you did in the conference that maybe you didn't think at the time was a big deal, but afterwards people came up to you and were like, wow, I'm so glad you did this thing, or this thing was so cool? Is there anything like that?

<span id="thirty-minute-break-format" class="interview-anchor"></span>

**Jason:** Yeah. And it wasn't even my idea. Keep Ruby Weird was a conference in Austin. That is one of the greatest regrets of my life that I never got to go. Terrence Lee was one of the organizers. Terrence works at Heroku. Terrence is on Ruby Core. Really smart individual.

We were talking at RubyConf, I don't know, Kansas maybe. RailsConf Kansas City? I don't know. Something right before Southeast Ruby, and I was just talking to him about it. He said, the thing we do is we do 30-minute talks, 30-minute break, 30-minute talk, 30-minute break. And I was like, that is so much downtime. But let's try it.

Again, not my idea. Everybody loved that format. If anybody talked to me about Southeast Ruby, it was always, I love how much time there is to talk to people. And I'm like, cool, yeah, I'm really glad. So that is something we kept every year. It works in that format because it's single track, minus the day we had the workshops, but it's single track. There's not a ton of people there, so you're in a small space. You end up kind of just talking to people, even if you're not real social. You'll probably end up talking to someone. I think that was the thing that always made that special to people.

**Travis:** Did you borrow anything else from conferences that you went to? You saw stuff you liked and brought that to.

**Jason:** I wanted to try and bring the RubyConf, RailsConf experience on a smaller scale. But I can't think of anything I did that was unique. Arguably, maybe we had too many keynote speakers, even for a regional conference, because we always had four, except for the last year we only had two. But that was because it was technically a single day.

I'm trying to think of things I wish I would have borrowed from conferences. Not doing lunch. We were really fortunate. We had a few people with dietary restrictions we had to watch out for, and they were actually always super grateful. It was easy to set up. People are always grateful for that. But I wish I had just been like—Ruby on Ales used to happen, I want to say in Oregon. I think it was that conference, or some conference that predated me, I was told would be like, yo, here's a $20 or $30 voucher. Go eat lunch somewhere.

**Travis:** Oh, nice.

**Jason:** If it wasn't Ruby on Ales, it was another one. Maybe it was Rocky Mountain. But I was like, oh, that's a cool idea. It's just baked into the price because you're going to spend that on catering anyway. The first two years, because we weren't at a hotel, we were working with restaurants directly, and they have to come deliver it. Actually the third year, even though we were at a hotel, we still catered food. We had a minimum for food included, so we did coffee and candy and stuff. But effectively, you end up paying $20 a head for the shittiest box lunch ever. So it's like, why not give you $20 or $30? Even in downtown Nashville, you could eat lunch pretty well on 20 or 30 bucks.

Or just like other conferences, don't give them any money and say, there's two hours, it's enough time. I wish I would have done that. I think it might have been more enjoyable, maybe, for the attendees as well.

I really liked having a conference-sanctioned event outside of the conference. The first year, that was the bar at the venue. The second year, we rented out the upper floor of a bar and just had snacks and drinks. You got tickets and stuff. I was watching the check the whole night. That was the thing that actually always surprised me whenever we'd do an event like that, even like the speakers' dinners. I always would be like, oh shit, this is going to be so expensive, and surprisingly, it was always lower than what I thought it would be every time. But in the third year, what event did we do? I don't remember. That was something that I really liked doing. I don't know if we got that from another conference or what, but having some kind of optional conference-sponsored social gathering was always a success, at least in my perception of it.

**Travis:** Nice. Tell me about the speaker's dinner.

**Jason:** Speaker dinner was one of those things that's like, hey, I can't pay for your travel, but I can at least buy you a meal. That was always cool, selfishly, because it was a chance for me to hang out with keynote speakers who, if I invited them, obviously I kind of hold them in high regard already. Also, that's how I got to know Jason Swett. The year he spoke, we had speaker dinner, hung out. I got to spend time with Noah Gibbs. It was a cool chance for them to meet, but it was also just a really cool chance for me to get to spend some time with them.

Every year we did it. Again, the first year I was like, hey, we'll cover food, but not alcohol. But the bill was so cheap, I was like, what? So by the second and third year, it was like, dude, get whatever you want. I think by the last year we had gone to, not the fanciest one in the world, but we were at a steakhouse at the top of a building in Nashville. It was super cool. So we had some cool experiences with that. Definitely recommend that if you can swing it.

**Travis:** Yeah. Is there anything else that you wish you would have done, that you wish you would have spent more money on, or put more time into?

**Jason:** It might be impossible, but I wish I would have attended the conference more. I was able to the first year, but by the second and third year, there were too many moving parts.

Every year, all three years, I tried to record the talks on video, and I regret even trying, because I still have hard drives of these videos, but I never had the time. I didn't have the money to pay someone to do it, and I never had the time to do all of them. So I regret even trying to do that, because it's left me with a sense of failure in a way. The speakers probably looked forward to that. They probably wanted that. I wish I had kept it simpler in that regard, not trying to do everything.

I wish I would have tried harder with sponsors the first year. Sponsors, in my experience, have always been super chill. As long as you do what you say you will in exchange.

**Travis:** Pretty easy to work with.

**Jason:** Yeah. They typically want you to succeed as well. It benefits both of you, and it really helps.

I'll tell you something that we did that I really liked. I don't know if I would do it again. I really liked being in a hotel the last year. But typically with hotels, you have to do a room block. You have to be like, well, we'll rent these 30 rooms, and if only 20 people do, then we'll pay. You're on the hook for the last ten. That was stressful. But we filled our block, at least, so it worked out. I don't know that I want to experience that again.

**Travis:** Why did you like the experience of being in a hotel? Was it just because it was easier to keep everybody in the same place?

**Jason:** Yeah, and not everybody stayed there. We had locals, but it was not the cheapest place. I had friends still doing Airbnbs and stuff. But it was nice, because there's a lot more opportunity. You walk downstairs and people are in the restaurant or at the bar, and it just created a lot more opportunity outside of the conference to see people.

I enjoyed that. When I go to conferences, I always try and get the hotel they recommend. If I go to RailsConf in a couple weeks, there's the hotel they have, and I always try and get the one they recommend. Same thing with Rails World. That's where the speakers are. That's where people are hanging out. And if the conference is there too, there's something nice. It's like, oh, it's two o'clock and I just can't do it right now. Just being able to go up to your room. It's a nice thing.

**Travis:** Yeah, very convenient. Do you have a favorite conference?

**Jason:** Like I've ever been to?

**Travis:** Yeah.

**Jason:** That's tricky. Sin City's up there. I have just a weird fascination with Vegas. I'm not even a big gambler, but I have a shelf in my office with Vegas stuff on it. The year before Swett decided to do Sin City, I'd started looking at doing a Ruby conference in Vegas. I just never pulled the trigger on it, and I'm glad, because Swett did all the work for me and I got to go.

Sin City's up there, probably, as one of my favorites. Not just because it was Vegas, but it had all the pieces to make it special. You can go do whatever you want, pretty much. Vegas never shuts down. One of my favorite memories is a group of people, not this past year, but in 2023, I guess, or 2022, whichever one. A bunch of us ended up in Old Town in downtown Vegas, on Fremont Street, the last night. One guy is teaching everyone how to play craps, and everyone's just having a blast. The conference was fun. Swett always had good technical speakers. It was so laid back. That was always special to me.

The first RailsConf I went to in 2015, it wasn't special, but it's special to me because I met Aaron Patterson. I met DHH. Not that they remember me, but it was special to me because these are people I've read so much of their stuff. I've watched talks. I met Aaron Patterson, and he was like, here, here's a sticker of my cat. And I was like, that's so smart. That gives him a thing to connect with someone without having to necessarily carry a conversation. I thought it was genius.

That one's special to me because it's the first time I got to see the Ruby community in person. It was special to me. Ruby Central as a whole, I know things got weird with RailsConf and Rails World and stuff like that, but Ruby Central as a whole, especially Evan and Abby Phoenix, Marty Haught, all of them who were on Ruby Central at that time, made those conferences good. They're really good. They were well-oiled machines, even if I don't know if it was like that behind the scenes. It appeared that way.

It holds a special place in my heart, because for the last, God, almost ten years—shit, for the last ten years, it's been the avenue by which I gained new relationships, new friends, everything. Rails World is fun. I don't think I've been to a Ruby conference I don't like is maybe the best way to describe it, except for maybe the year at RubyConf where they didn't have water.

**Travis:** Oh, a great water debacle. Alright. Well, we'll wrap this up here so you can get back to your day. But do you have any resources that you would recommend for first-time conference organizers, or any people that you would recommend that I talk to next in this kind of format?

**Jason:** I think you're building the resource.

**Travis:** This podcast.

**Jason:** You're building the resource for people, because the thing I did was try and talk to people who had done it. When Jeremy Smith started, I think I talked to him about some of this stuff. I know you talked to Jeremy recently on this. I love Jeremy Smith. He came to Southeast Ruby. I think the first year he was like, hey, is there a place to park a camper van? It was awesome.

We didn't really become friends until a moment at Sin City Ruby, I want to say the first year. We had breakfast, and it was me—I can't remember who was there, but Jeremy was there. It was just four of us, and we just started talking. Jeremy is such a good dude.

If you haven't already, reach out to Jason Swett. I know his experience this year with the Tropicana, where he did the first two Sin Cities, with it being gone, changed his experience. Did he do it at the MGM?

**Travis:** Yeah.

**Jason:** Because it's a much bigger entity with much higher expectations, where the Tropicana, just walking in there, you're like, oh, this place doesn't give a shit about anything.

**Travis:** Yeah.

**Jason:** Also what made that place so special, right? But yeah, definitely talk to Jason Swett if you can. If you could find any of the people who used to do Keep Ruby Weird, like Terrence Lee, Richard Schneeman, Caleb—I can't remember Caleb's last name right now. There's also, I don't know, maybe he helps with Keep Ruby Weird, but Nickolas Means. He's a conference speaker for sure. He's got a lot of conference experience, even if he's never organized one. You might try and find Nickolas and tell him that I recommended him, because he is just a plethora of knowledge and one of my favorite human beings in the world.

**Travis:** Awesome. I plan to, after I interview a bunch of organizers, also interview speakers about their experiences, and just people who have been to a bunch of conferences. Just get all kinds of perspectives.

**Jason:** Yeah. You talked to Marty Haught, right?

**Travis:** Yeah.

**Jason:** Evan Phoenix also might be a good one, or if you could talk to—I don't know if she would want to—Evan's wife Abby was one of the core people who made the Ruby and RailsConfs happen for a while. I don't know if she would be interested in going on podcasts, but I worked with her a couple of times, and they're great people.

**Travis:** Awesome.

**Jason:** Sorry, that's probably more than you wanted.

**Travis:** No, that's good. Gives me a lot of homework. Alright. Well, hey.

**Jason:** What's the name of your conference?

**Travis:** Right now, I'm thinking I'm going to call it Blastoff Rails. I want to do a conference, but I want to do it different. I want to do talks or workshops, but I'm also thinking I want to do event-type stuff.

One of my ideas is, I need to find somebody that'll be willing to do this, but have you seen the show _Hot Ones_?

**Jason:** Yeah, I know what you're talking about.

**Travis:** I want to do a Hot Ones interview with a Rails community famous person, and get them up because it's New Mexico, right? We have stuff. Bring them, and they can try chili, and we can ask them questions, and it'll be entertaining. I kind of want to do entertainment-type stuff at the conference too. So probably Blastoff Rails, and I'm going to try and do it in June of next year. I'm giving myself a year, and I'm glad I did, because everything is taking longer than I thought it would.

**Jason:** Listen, I'll tell you this. I know we're out of time, but one thing I want to mention to that point is, I almost brought back Southeast Ruby two years ago. But I said if I was going to do it, I was going to do it in Memphis because I live here. I was going to be like, yo, we have six speakers, and we're just going to hang out. It's basically going to be an excuse to invite all of my Ruby friends and anyone who wants to come hang out. I think there's something special there. I like that idea. I like your idea. That's cool.

Is there a reason you're going with more specific Rails than Ruby?

**Travis:** Because they are about the talks, but they're about the hallway track too, and the experience. I want to elevate the stuff outside of the talks, just to see what I can do and see what we can create there.

After my interview with Marty Haught, he recommended a book called _The Art of Gathering_, which is about creating gatherings, aka conferences. One of the things in there was narrowing your purpose can be beneficial, because it can make people want to participate more. Rather than saying, we're a Ruby conference for anybody who loves Ruby, just come—that can work for something like Ruby Central because they have this institution. People know them.

But for myself, I feel like if I did something really general, it might not give people enough reason to come. So if I went narrow, and I kind of want to go even narrower than Rails but I just haven't committed to anything yet, like if I did Rails Builders Conference where all the talks are themed around what people have built with Rails, and all the activities are like building stuff with Rails, I feel like if I went narrower I might be able to get people to want to come a little bit more. That's the theory at this point.

**Jason:** No, I was actually just curious. I have no hard stance either way. I was just curious, because most of the time when we do these regional things, they are Ruby, but the talks end up being, not all of them, but a lot of them end up just being Rails and Rails and Rails.

**Travis:** Yeah. Well, somebody I really want to talk to is Andrew. I can't remember his last name. He did Rails SaaS.

**Jason:** Oh, Andrew Culver. Yeah, look at that one.

**Travis:** Yeah, because that was kind of what I want to do. He had a very narrow niche: it's Rails and it's SaaS. I've heard so many good things about that conference as well.

**Jason:** Yeah, that conference was special, and for different reasons. It was really cool.

**Travis:** Yeah.

**Jason:** Cool. Well, I'll stop interrogating you. I want to learn more.

**Travis:** No worries. Always good talking with you, Jason. Thank you for your time. Are you going to be at RailsConf this year, the last one?

**Jason:** I'll be at RailsConf, and right now I'll be at Rails World. So all the Rails.

**Travis:** Yeah, I didn't get a Rails World ticket, but I will see you at RailsConf.

**Jason:** All right. I'll see you in a few weeks, then.

**Travis:** Yup. Alrighty, take care, man. I'll talk to you.

**Jason:** I appreciate it.

**Travis:** All right.
