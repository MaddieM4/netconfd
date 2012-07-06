---
title: netconfd - Easy, pretty web administration
layout: default
---

## What is netconfd?

netconfd is a modular, flexible daemon for web-based system administration. It
uses XML and XSLT to construct a frontend web interface, and Backbone.js/AJAX
to do live updates based on the actual state of the system, and changes made
by the user.

Because it's so flexible, it's easy to put your own branding on it, meaning it
could easily become the common foundation for all sorts of configuration
interfaces for all sorts of devices. It will be initially targeted at mesh
networking systems, but there's no reason people can't use it for other things
and grow the official module set.

![Project logo][logo]

## Why make netconfd? Don't most things have web interfaces already?

Yep. Shitty, half-assed interfaces. And that's not an indictment of the projects
that use them - those interfaces are shitty and half-assed because the devs
have better things to do in their actual domain and interests than roll their
own interface from scratch. The underlying truth is that they shouldn't have to
reinvent the wheel to make configuration less daunting. They need a different
project that they can offload 90% of that work onto and then slap their own
label on the finished product.

netconfd is that thing.

With netconfd, you can just write some scripts and some XML and you have
yourself a netconfd module. Then anyone can compose their own interface
based on your module, including you, of course. If it can be configured with a
text editor or the command line, you can configure it with netconfd, and likely
in an easier-to-understand way for those who are unfamiliar with the tech.

## How does it work?

netconfd is made primarily of two parts: the templating engine, and the conf
server. The templating engine serves up HTTP, on port 80 by default. The conf
server runs in the same process but on a different port, accepting AJAX calls
to get or set parameters.

### Templating engine

![Templating Diagram][templating]

TBW

### Conf server

TBW


## Where can I get it?

Hold your horses, buckaroo. netconfd is still in the design phase. Even after
the basic platform is written, it won't be stable or secure enough for real
world use, though I have no problem with you experimenting with it.

The sad truth is that at the time of this writing, the code does not exist.
Nothing to download. Sorry. You can expect something downloadable by the end of
July 2012 at the latest - if there's still nothing up, *then* you can call it
vaporware, but until then, I'd appreciate the benefit of the doubt.

## I'm an angry bastard and I want to hit someone.

[Philip Horger](http://orchard.crabdance.com) maintains this software. Sorry if
it gave you a hulk rage. I'm probably the person you want to hit but please,
find some positive outlets. You can't live like that forever, man.

[templating]: images/templating.png
[logo]: images/logo.png
