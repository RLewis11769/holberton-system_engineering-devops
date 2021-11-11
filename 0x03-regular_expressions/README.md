# RegEx

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
#!/usr/bin/env ruby
puts ARGV[0].scan(/[0-9]/).join
```

## Mandatory

### 0-simply_match_holberton.rb
- Match "Holberton" exactly
	- Case-sensitive
	- Test examples and expected results:
		```
		$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
		Holberton$
		$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
		HolbertonHolberton$
		./0-simply_match_holberton.rb "holberton" | cat -e
		```

### 1-repetition_token_0.rb
- Match hb, between 2-5 t, then n
	- {} refers to character directly before
	- {min, max} number of times letter exists
	- Test examples and expected results:
		```
		$ ./1-repetition_token_0.rb hbtttn
		hbtttn
		$ ./1-repetition_token_0.rb hbtn
		$ ./1-repetition_token_0.rb hbttttttn
		```

### 2-repetition_token_1.rb
- Match htn and hbtn, nothing else
	- ? indicates preceding character is optional
	- t? is identical to t{0,1}
	- Test examples and expected results:
		```
		$ ./2-repetition_token_1.rb htn
		htn
		$ ./2-repetition_token_1.rb hbtn
		hbtn
		$ ./2-repetition_token_1.rb hbttn
		```

### 3-repetition_token_2.rb
- Match hb, any positive number of t, then n
	- + indicates preceding character exists 1 or more times
	- t+ is identical to t{1,}
	- Test examples and expected results:
		```
		$ ./3-repetition_token_2.rb hbtn
		hbtn
		$ ./3-repetition_token_2.rb hbtttttttttttttttttttttttn
		hbtttttttttttttttttttttttn
		$ ./3-repetition_token_2.rb hbn
		```

### 4-repetition_token_3.rb
- Match hb, any number of t including 0, then n
	- * indicates preceding character exists 0 or more times
	- t* is identical to t{0,}
	- Test examples and expected results:
		```
		$ ./4-repetition_token_3.rb hbn
		hbn
		$ ./4-repetition_token_3.rb hbbbtn
		hbtn
		$ ./4-repetition_token_3.rb hbbbtn
		hbtn
		$ ./4-repetition_token_3.rb hn
		```

### 5-beginning_and_end.rb
- Match h, any character, then n
	- . indicates any single character
	- Test examples and expected results:
		```
		$ ./5-beginning_and_end.rb hbn
		hbn
		$ ./5-beginning_and_end.rb h7n
		h7n
		$ ./5-beginning_and_end.rb hn
		$ ./5-beginning_and_end.rb hbtn
		```

### 6-phone_number.rb
- Match 10-digit number (as in phone number)
	- [] indicates any in range (in this case 0-9, all single digit numbers)
	- {} indicates exact number of characters
	- ^blah$ indicates exact match
		- Essentially "Is this character within 0-9?" 10 times EXACTLY, no extra characters
	- Test examples and expected results:
		```
		$ ./6-phone_number.rb 0123456789
		0123456789
		$ ./6-phone_number.rb 01234567899
		$ ./6-phone_number.rb " 0123456789"
		$ ./6-phone_number.rb "012-345-6789"
		```

### 7-OMG_WHY_ARE_YOU_SHOUTING.rb
- Matches all capital letters
	- [] indicates any in range (in this case A-Z, all capital letters)
	- Test examples and expected results:
		```
		$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "HELLO"
		HELLO
		$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr has Yummy chocOlate cUps"
		ILOVEYOU
		$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "bye"
		```

## Advanced

### 101-passed_linkedin_regex_challenge.jpg
- Complete LinkedIn RegEx puzzle and provide screenshot
![LinkedIn puzzle](https://github.com/RLewis11769/holberton-system_engineering-devops/blob/main/0x03-regular_expressions/pics/LinkedInPuzzle.png)

## Basics

### References

Test at [RegExr](https://regexr.com/)!!!

![RegEx Cheatsheet](https://github.com/RLewis11769/holberton-system_engineering-devops/blob/main/0x03-regular_expressions/pics/RegExCheatsheet.png)

### Anchors

- ^
	- Indicates following character is at beginning of line
- $
	- Indicates preceding character is at end of line

### Counting Operators

- .
	- Stand-in for any single character
- ?
	- Indicates preceding character is optional
- *
	- Indicates preceding character exists between 0 and unlimited times
- +
	- Indicates preceding character exists between 1 and unlimited times
- {}
	- Indicates number of times character preceding character exists
		- {num} - exact number of times
		- {min, max} - range of times

### Grouping Operators

- []
	- Indicates character "class"
	- Essentially shorthand for | OR
		- [AZ] means A or Z
		- [A-Z] means any single character between A and Z
		- [a-zA-Z] means any single character
		- [0-9]{3} means exactly 3 digits
			- 1234 would return 123 although 123456 would return both groupings
- ()
	- Indicates character "group"
	- Isolates grouping from rest of string so can find substrings
		- (AZ) means exactly AZ
		- (A-Z)y means exactly A-Zy
		- (a-z)+ means a-za-z where a-z+ would mean a-zz

### Look-Ahead / Look-Behind
- (?<=)
	- Positive lookbehind
	- Finds character followed by character in grouping
		- (?<=the).
			- String: "the they then"
			- Matches: " " and "y" and "n"
		- (?<=from..?)\w+
			- String: "from:me from: you"
			- Matches: "me" "you"
	- Inverted by negative lookbehind (?<!)
- (?=)
	- Positive lookahead
	- Finds character preceding by character in grouping
		- .(?=at)
			- String: fat cat
			- Matches: "f" and "c"
	- Inverted by negative lookahead (?!)

### Special Characters

- |
	- Logical or
		- A|Z means A or Z
- \
	- Escape character
		- for any quantifier
		- \b - word boundary
			- \b\S - first character in word
			- \S\b - last character in word
		- \d - digit
		- \w - word
		- \s - whitespace (including spaces, tabs, and linebreaks)
	- Include inverse
		- \D - not digit
		- \W - not word (same as \s)
		- \S - not whitespace (same as \w)
