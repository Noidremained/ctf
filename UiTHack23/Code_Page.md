# Code Page
## Challenge description
>I fired up my old machine, the whirling and clicking of the hard drive was comforting. I opened up the terminal and typed in the passcode: 2 1 0 2 7 and was greeted with the homescreen. There I found with a weird file, but im no Klingon. Can you help me translate it?
## Solution
So, naturally I tried a lot of stuff that didn't end up anywhere, and I don't remember all of it, so I'll mostly just include what did work out.
I spent some time in CyberChef without much luck before I thought to check the hint for the task which was:

>Professor: "So the American government went to IBM to come up with an encryption standard, and they came up with—"  
Student: "EBCDIC!"

"EBCDIC" stands out as the important part of the hint and a quick google search finds that it is an encoding made by IBM.
Ok, so then I go back to CyberChef and choose the decode text operation with EBCDIC International as the encoding. The resulting string is not readable so I try the encode operation instead and this time we get:

```
....a.k..{lo..º.nº..an.la..on}
```

It's not the whole flag, but we can at least see that it has the right form. And we can fill in the missing letters before the bracket so that we get:

```
UiTHack23{lo..º.nº..an.la..on}
```

I then took some more detours before thinking that maybe the two '```º```' are supposed to be underscores. While thinking that it may not be the intended way to do it, I decided to use https://word.tips/word-solver/ to find the rest of the flag. So I set it to find a word
with 11 letters, ending with "on" and containing "an_la" ('_' meaning unspecified letter). This gave me "granulation" and "translation", where "translation seems the more likely one, and perhaps something I should've been able to see for myself without the help of this tool, but oh well, at least I didn't 
need to use the tool for the two first words. After finding "translation" I quickly guessed that the other words had to be "lost in" and thought to myself that maybe filling in the words by guessing like this was the intended way after all. So then we have the flag:

```
UiTHack23{lost_in_translation}
```
