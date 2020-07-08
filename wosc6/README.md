
To generate wosc6-proposal.pdf

```
grip wosc6-proposal.md
```

To generate cfp.txt:

```
lynx --dump cfp/index.html >| cfp/cfp.txt
```

To generate cfp.pdf

```
weasyprint  cfp/index.html cfp/cfp.pdf
```

To install tools

```
pip3 install weasyprint
```

TODO TBW how to isntall grip and lynx  
