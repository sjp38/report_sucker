Report Sucker
=============
Nobody likes report, but should suck somebody. Report sucker sucks report
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

for example, see `trans_rule_example` and `weekly_report_template.odt`.
Then,
`$ ./make_report.py weekly_report_template.odt test_out.odt trans_rule_example`
and see `weekly_report_template.odt` and `test_out.odt` again.

License
-------
GPL v3

Author
------
SeongJae Park (sj38.park@gmail.com)

