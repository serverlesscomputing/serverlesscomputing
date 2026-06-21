
## To generate proposal.pdf

```
mdpdf wosc11-proposal.md -o wosc11-proposal.pdf
```

## To generate cfp.txt:

lynx **ignores CSS entirely** (no `@media print` support), so the navbar,
footer, scroll-to-top button, etc. would otherwise appear in the dump. Strip
them with `sed` before piping to lynx, and use `--nolist` to drop link-number
footnotes:

```
sed -e '/<!-- Navigation-->/,/<\/nav>/d' \
    -e '/<!-- Footer-->/,/<\/footer>/d' \
    -e '/<a class="scroll-to-top/d' \
    cfp/index.html | lynx --display_charset=utf-8 --dump --nolist -stdin >| cfp/cfp.txt
```

## To generate cfp.pdf

WeasyPrint **does** honor `@media print` and `media="print"` stylesheets, so
the navbar/footer/toggle are hidden by the print stylesheet at `css/print.css`
that every page links — no preprocessing needed:

```
weasyprint cfp/index.html cfp/cfp.pdf
```

Then open cfp/cfp.pdf and cfp/cfp.txt and verify all looks good before committing (minor edits in .txt may be necessary).

## To install tools

```
pip3 install grip
pip3 install mdpdf
pip3 install weasyprint
```

```
brew install lynx
```
