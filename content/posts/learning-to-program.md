+++
date = '2018-02-28'
description = 'Advice on learning to program. Somewhat dated, but still useful.'
+++

# Learning to Program

For general purpose programming there are a *lot* of good resources online. 

Some programming languages and resources to check out:

- [Scratch][scratch_homepage] is a fun, graphical language aimed at school kids.
  Creating animations and sounds is easy, and kids (and adults) learn
  a lot.
- [Python][learn_python_the_hard_way] is a great general purpose language. (I use it every day.)
- [C][learn_c_the_hard_way] is an imperative language that is old, but still used everywhere.
- [Java][java_oracle_tutorials] is an object oriented language used by big corporations. It's very well documented.
- [Racket][racket_with_pictures] is a functional language with great resources for teaching programming.
  The [Racket with Pictures][racket_with_pictures] tutorial, like Scratch, emphasizes things you can see.
- [JavaScript][javascript_com] is the programming language of the internet. It
  really has almost _nothing_ to do with Java other than having it in its name.
  It looks like C, but it is evolving quickly.

## Start with Python and [Learn Python the Hard Way](https://learnpythonthehardway.org/book/) 

Setting things up takes some effort, but it's worth sticking with it. Zed
will step you through everything you need to do.

If you get discouraged with setting up Python, [download
Racket][racket_download] and do the [Introduction to Racket with Pictures][racket_with_pictures].

Note: a coworker warns me that Zed's lectures (the author of "the hard way"
websites) contain a lot of objectionable language. The website uses nice 
language, so perhaps the videos do too, but I've never
watched them. The written tutorials were plenty for me.


## Online resources by category


### Python

General purpose language.

I use this one daily at work and for many personal projects.

Found on all major Linux systems. (That includes the [Raspberry Pi OS](https://www.raspberrypi.com/documentation/computers/os.html) which is a derivative of [Debian](https://www.debian.org/).)

Can also install/run on windows.

*Links*

- https://learnpythonthehardway.org/book/ [Learn Python the Hard Way is recommended][learn_python_the_hard_way]
- [https://wiki.python.org/moin/BeginnersGuide][python_beginners]
- [MIT Introduction to Programming courses][mit_intro_to_programming]
    - [Introduction to CS][mit_intro_cs]
    - [Gentle introduction][mit_gentle_intro]


### [Scratch](https://scratch.mit.edu/)

Graphical language aimed at kids.

A kid presented on Scratch at OpenWest last year. He had a surprisingly good understanding of programming principles.

Can use online after registering.

Can also download for learning offline.


*Links*

- [Scratch Homepage][scratch_homepage]
- [Download 1.4](https://scratch.mit.edu/scratch_1.4/)
- [Download](https://scratch.mit.edu/scratch2download/)
- [Online class at Harvey Mudd using Scratch](https://www.edx.org/course/programming-scratch-harveymuddx-cs002x)



### Racket

Functional Programming language.

For something fun to play around with, check out the [Introduction with Pictures][racket_with_pictures].

This probably is the fastest to get started with: their installer is
just click and go no matter your system.

- [Download Racket][racket_download]
- [Introduction with Pictures][racket_with_pictures]
- [Racket Home Page][racket_homepage]

[racket_with_pictures]: https://docs.racket-lang.org/quick/
[racket_download]: https://download.racket-lang.org/
[racket_homepage]: https://racket-lang.org/


### C

Procedural language. High level language compared to assembly. 

Is what Linux is written in.

Is not C++. 

Has a good "Learn C the Hard Way" course https://c.learncodethehardway.org/book/ (Recommended.)

*Links*

- [Learn C the Hard Way][learn_c_the_hard_way]
- [C Standard Library][c_stdlib]

[learn_c_the_hard_way]: https://c.learncodethehardway.org/book/ "Learn C the hard way"
[c_stdlib]: https://en.wikibooks.org/wiki/C_Programming/Standard_libraries
    

### Java

Object Oriented Programming language.

Is *not* JavaScript.

Oracle has tutorials to walk you through the language.

The [eclipse editor][eclipse_download] is a popular editor for Java.

Watch [MIT Introduction to Programming with Java][mit_intro_java] if you prefer lectures to reading.

*links*

- [Download Eclipse Editor][eclipse_download] Editors and IDEs make life much nicer when coding in java.
- [Install Java][java_download], because without it, eclipse will not be able to run.
- Go through some of the [java tutorials][java_oracle_tutorials].


### JavaScript

Is *not* Java. JavaScript is also known as ECMAScript. Unlike C, which changes maybe every ten years, JavaScript is changing almost yearly.

Runs in web browsers, on web servers, and is easy to learn. (Learning to use it well requires more time.)

Go to [javascript.com][javascript_com] to get a taste.

Mozilla has a [good reference][javascript_reference] for the JavaScript language, including the changes in the ECMAScript standard. Since ECMAScript is another name for JavaScript "changes in the ECMAScript standard" is another way to say "changes in JavaScript."

Since every browser runs javascript, you can open the developer tools and play around with JavaScript in Firefox, Chrome, or Windows Explorer. (I'm not sure about Safari or Opera.)

In Firefox, hit Control-Shift-I to open the developer tools.

In Chrome, hit Control-Shift-J to open the developer tools.

In Windows Explorer, hit F12.

In each all of those browsers one can also look for Tools or Developer Tools in the menus.


### For questions

- check out [https://stackoverflow.com/][stackoverflow]
- email me. I am more than happy to help. 
- do what the professionals do: grab a stuffed animal and explain your
  problem to it. If this sounds odd, see [Rubber Duck Debugging][rubber_duck_debugging]. Also watch
  Castaway and note the role that Wilson plays in the film.



[eclipse_download]: https://www.eclipse.org/downloads/packages/release/Neon/2
[stackoverflow]: https://stackoverflow.com/
[java_download]: https://www.oracle.com/technetwork/java/javase/downloads/index.html
[java_oracle_tutorials]: https://docs.oracle.com/javase/tutorial/java/index.html
[javascript_com]: https://www.javascript.com
[javascript_reference]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[learn_python_the_hard_way]: https://learnpythonthehardway.org/book/ (Recommended)
[mit_gentle_intro]: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011
[mit_intro_cs]: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011
[mit_intro_java]: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-092-introduction-to-programming-in-java-january-iap-2010 "MIT Introduction to Programming in Java"
[mit_intro_to_programming]: https://ocw.mit.edu/courses/intro-programming/
[python_beginners]: https://wiki.python.org/moin/BeginnersGuide
[scratch_homepage]: https://scratch.mit.edu/
[rubber_duck_debugging]: https://en.wikipedia.org/wiki/Rubber_duck_debugging
