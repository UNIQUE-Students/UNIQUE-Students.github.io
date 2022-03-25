---
title: Playground
subtitle: Hugo
layout: page
---
# The playground of {{ page.subtitle }}

This is a dummy page on the website of [USS 2021](https://uss2021.github.io/) for you to play around. Feel free to modify the content and use it for `git` and GitHub tests.

## Intro to Markdown

This page is written with [Markdown](https://en.wikipedia.org/wiki/Markdown). Markdwon is a _markup language_, which means that it is a system for writing text alongside other information which is readable by a computer. Other markup languages are [HTML](https://en.wikipedia.org/wiki/HTML) and [XML](https://en.wikipedia.org/wiki/Extensible_Markup_Language). However, Markdown is _lightweight_ which means that the annotations are fairly simple and the overall result is easily readable. 

For example, you can easily write text **in bold** by enclosing the piece of text with a pair of asterisks (`**`). _Italics_ is made signed with enclosing underscores (`_`). And of course you can combine _**bold and italics**_---guess how? It's also possible to do ~~this kind of stuff~~. By the way, since a couple of years ago, Slack, Whatsapp and Telegram, and other messaging apps, also support this kind of markup annotations, as you may know. 

Creating hyperlinks is also really easy. Here's [one link to a pretty random website](http://drawing.garden/). To create a hyperlink, you enclose the text of the link with square brackets, [like this], immediately followed by the actual URL enclosed with parentheses, that is (https://uss2021.github.io/).

Markdown also allows to easily write `fixed width text`, using _backticks_: \`code\`. This is useful for writing formatting pieces of code. But it's also possible to write code blocks by enclosing the code with 3 backticks (\`\`\`). For example, this illustrates the basic workflow with `git`:

```
git clone https://github.com/uss2021/uss2021.github.io.git web_uss2021
cd web_uss2021
git checkout -b playground-branch
touch new-file
echo "banana" > new-file
git status
git add new-file
git commit -m "new file with banana"
git push
```

## Other beauties of Markdown

This is, of course, not all Markdown can do! There are many more formatting options, and what is great of it is that everything is quite intuitive and easy to learn and remember. There are multiple resources online to learn about Markdown. One example is the [Markdown Guide](https://www.markdownguide.org/), which has a [Getting started guide](https://www.markdownguide.org/getting-started/), an overview of the [syntax](https://www.markdownguide.org/basic-syntax/) and a [cheatsheet](https://www.markdownguide.org/cheat-sheet/). Let's look at some of the more common features of Markdown in this page!

### Lists

#### Unordered lists

Unordered lists can be built using asterisks (`*`), dashes (`-`) or plus signs (`+`). And indentation is supported to create different levels:

* Brain
    * Visual cortex
        * V1
        * V2
        * V4
    * Auditory cortex
        * A1
        * A2
        * A3
* Artificial neural networks
    * Convolutional layers
    * Recurrent layers

#### Ordered lists

Guess how you can create ordered lists?

1. Un
    1. Eins
    2. Zwei
    3. Drei
2. Deux
3. Trois
    1. Uno
    2. Dos
    3. Tres

### Horizontal rules

Horizontal rules can be created with a sequence of three dashes (`---`), or three asteriks or underscores.

---

New stuff below the rule.

### Sections or Headers

Maybe you have noticed that this page is organised in headings at different levels. The title of the first level is preceded by one number sign (`# Heading 1`), the second by two (`## Heading 2`), and so on and so forth.

### And more

Check [this syntax guide](https://www.markdownguide.org/basic-syntax/) for how to do other things, and try some of it right here!

