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

The template system is made of a bunch of layers. netconfd comes with a set
of modules and widgets, but you can make your own or override the defaults.

A *widget* is a basic chunk of the interface, a parameter with slots for a
getter, setter, description, title, caching properties, etc. But in the
widget definition itself, mind you, none of these things are filled in.
The widget definition is an XSLT template that defines how to turn *invocations*
of that widget into HTML.

*Modules* are sets of *widget invocations*. For example, the SSH module might have
a 'port' property, which is an invocation of the "textbox" widget, containing
the callback information necessary for the conf server to apply changes and
display the current value, and the metadata the widget needs to generate the
HTML of the invocation. Invocations within a module are called *tweakables.*

*Pages* pick and choose available tweakables from modules and assemble them as
logical groups. Each page corresponds to an actual page that you can navigate
to in your browser, and contains tweakables cherry-picked from the modules.
This is almost the top layer of the templating, but not quite.

The highest layer is the *global template*, which does things like initialize
Backbone.js and provide whatever structure will be present in every page.
This is the common skeleton of the entire presentation layer, and you can
change the entire look of the interface across all pages simply by overriding
this and the style sheet(s).

As you can see, every single layer of this has defaults but is fully open to
customization and overriding. Much like [Zombocom](http://zombo.com/), the only
limit is yourself.

### Conf server

The conf server is another service that runs in the same process space, though
in a different thread or greenlet than the http daemon that the template engine
runs on top of. It communicates on a different port by default, though as a
Backbone.js server, it can optionally be run on the same port under a dedicated
directory.

This server recieves GET and POST requests for tweakables, and translates them
into the proper system administration commands based on the tweakable's
definition. This is all statelessly authenticated with cookies on top of SSH,
like the rest of the interface is. It also shares conf data with the other
parts of the process, which means it operates off the same playbook as the
template engine at all times.

Another option for security is to run multiple conf-only processes for each
set of permissions that will be needed, so you can isolate what permissions
each instance is allowed. Sound config will run as a group that can manipulate
sound parameters on the system, network config server will run as the group
for that, etc. This lets you lock down your system a lot tighter against
exploits, which is always a risk that these kinds of applications have to take
into account. Note that this is quite incompatible with the "subdirectory"
approach listed in the first paragraph, although if you set up nginx as a
unifying reverse proxy to your various netconfd web services, this is easy
enough to work around.

## Won't this just discourage people from learning the command line?

It makes it much less of a prerequisite, but I don't want to cripple anyone's
learning process, even by enabling convenience. So the default interface will
offer a "look inside" button for every tweakable on every page, where you can
see the command or configuration location/flag for every getter and setter.
Investigating how a module works on the inside is as easy as clicking a button.

Obviously I can't guarantee that custom-branded installs of netconfd will
retain this feature. Some distributors may decide that such stuff is unfriendly
or some other nonsense, and they are free to disable/remove that code, of
course. It's all part of the front-end anyways, you don't even have to dig into
the daemon code to figure out how - it's just XML, HTML, XSLT and JS.

But I do think that providing this kind of awesome feature, fully implemented,
by default, will encourage most customizers to retain the feature in some
variation or another. Because nobody else has to write it from scratch, so why
not just copy and paste it over at the very least? And that will make netconfd,
even in crazy custom variations, that much more attractive to the hackers that
make up my target demographic.

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
