

## To generate cfp.txt:

```
lynx --display_charset=utf-8 --dump cfp/index.html >| cfp/cfp.txt
```

## To generate cfp.pdf

```
weasyprint  cfp/index.html cfp/cfp.pdf
```

Then open open cfp/cfp.pdf and cfp/cfp.pdf and verify all looks good before committing (minor edits in .txt may be necessaey)


## To generate wosc9-proposal.pdf

```
mdpdf wosc9-proposal.md -o wosc9-proposal.pdf
```


## To install tools

```
pip3 install grip
pip3 install mdpdf
pip3 install weasyprint
```

```
brew install lynx
```
