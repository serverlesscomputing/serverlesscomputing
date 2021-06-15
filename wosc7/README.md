
To generate wosc7-proposal.pdf

```
grip wosc7-proposal.md
weasyprint  http://localhost:6419/ wosc7-proposal.pdf
```


To generate cfp.txt:

```
lynx --display_charset=utf-8 --dump cfp/index.html >| cfp/cfp.txt
```

To generate cfp.pdf

```
weasyprint  cfp/index.html cfp/cfp.pdf
```

To install tools

```
pip3 install grip
pip3 install weasyprint
```

TODO TBW how to istsall grip and lynx  
