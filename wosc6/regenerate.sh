lynx --display_charset=utf-8 --dump cfp/index.html >| cfp/cfp.txt
weasyprint cfp/index.html cfp/cfp.pdf
