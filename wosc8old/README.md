
To generate wosc8-proposal.pdf

```
grip wosc8-proposal.md
weasyprint  http://localhost:6419/ wosc8-proposal.pdf
```


To generate cfp.txt:

```
lynx --display_charset=utf-8 --dump cfp/index.html >| cfp/cfp.txt
```

To generate cfp.pdf

```
weasyprint  cfp/index.html cfp/cfp.pdf
```

Then open open cfp/cfp.pdf and cfp/cfp.pdf and verify all looks good before committing 
(minor edits in .txt may be necessaey)

To install tools

```
pip3 install grip
pip3 install weasyprint
```

