Report Sucker
=============
Nobody likes report, but someone should suck it. Report sucker sucks report
instead of you.

Report Sucker is a simple tool helps writing odt template report.
Simply using template odt file and keyword, replace keyword with you preferred
text.

Usage
-----
```
./make_report.py <template odt> <output odt> <trans data>
```

Trans data
----------
trans data consists in next template:
```
<text in template 1>
<text to replace the text in template 1>
<blank line with no whitespace 1>
<text in template2>
<text to replace the text in template2>
<blank line with no whitespace 2>
...
...
<text in template n>
<text to replace the text in template n>
<blank line with no whitespace n>
```

For example:
```
Main title
Progress report 3rd Week, March 2014, Knights Of Round Table

basic info
Basic Information

name bullet
Name Sir. LANCELOT

project bullet
Contribution type and project

project info
Holy Grail Seeking(Contributor)

Project abstraction table title
Project abstraction

Project abstraction contents
1. Holy Grail is Holy Cup
 - Journey to seek Holy Grail
 - You're banging together two coconuts.
 - Are you suggesting coconuts migrate?
 - run away!!!
```

For more example, see `trans_rule_example` and `weekly_report_template.odt`.
Then,
`$ ./make_report.py weekly_report_template.odt test_out.odt trans_rule_example`
and see `weekly_report_template.odt` and `test_out.odt` again.

License
-------
GPL v3

Author
------
SeongJae Park (sj38.park@gmail.com)

