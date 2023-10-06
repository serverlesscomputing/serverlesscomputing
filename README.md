# WoSC website

## Instructions

### To run locally

Install ruby and Jekyll: https://jekyllrb.com/docs/

Install required gems with:

```bash
bundle install
```

Run server with command:

```bash
bundle exec jekyll serve
```


### Add a new WOSC edition

1. Copy previous edition directory and paste replacing new edition number (e.g. `cp -r wosc7 wosc8`)

2. Change edition number (only number!) at the top of all all *.md files of the new edition folder

3. Make any necessary change to call for papers (dates, chairs...)

4. Update `_config.yml`:
    1. Add defaults for new edition (papers, demos and keynotes). Remember to update the edition number in `path` and `permalink` sections
    2. Update current edition name and number in `wosc` section
    3. Add new edition in the `Previous Editions` link menu list

### Add a paper/demo/keynote

1. Copy template from the template folder and paste to corresponding directory (example: _papers/wosc7 for a wosc7 paper)

2. Rename to pX.md for papers, dX.md for demos and kX.md for keynotes, where X is the paper/demo/keynote number (p1.md, d2.md ...)

3. Edit the file and fill in info required

4. For presentation slides, upload the PDF file to woscX/presentations/, where X is the wosc edition. Indicate the PDF file name in the .md file.


## Gallery

To generate gallery for the workshop

Install thumbsup from https://thumbsup.github.io/docs/

Copy JPG files to photos/ subdirectory in woscN/ directory

```
cd woscN
mkdir photos
```

### WoSC  Gallery


```
cd wosc4/
thumbsup --input ./photos --output ./gallery --title 'Fourth International Workshop on Serverless Computing (WoSC) 2018 Gallery' --theme cards --thumb-size 200 --albums-from date  
```

```
sed -i '' -e 's/index.html/..\/index.html/g' gallery/2018-12.html
```

And link form woscN index.htmnl page

```
cd wosc3/
thumbsup --input ./photos --output ./gallery --title 'Third International Workshop on Serverless Computing (WoSC) 2018 Gallery' --theme cards --thumb-size 200 --albums-from date  
```



Then edit gallery/2018-07.html
to point to workshop index.html with ../index.html:


```
sed -i '' -e 's/index.html/..\/index.html/g' gallery/2018-07.html
```


### WoSC 2 Gallery

```
cd wosc2/
thumbsup --input ./photos --output ./gallery --title 'Second International Workshop on Serverless Computing (WoSC) 2017 Gallery' --theme cards --thumb-size 200 --albums-from date  --sort-media-by filename
```



Then edit gallery/2017-12.html
to point to workshop index.html with ../index.html:


```
sed -i '' -e 's/index.html/..\/index.html/g' gallery/2017-12.html
```

### TODO Using Docker 

Currently fails missing .config somehow ...

```
docker run -t -v `pwd`:/work -u $(id -u):$(id -g) thumbsupgallery/thumbsup thumbsup --input ./photos --output ./gallery --title 'Second International Workshop on Serverless Computing (WoSC) 2017 Gallery' --theme cards --thumb-size 200 --albums-from date  --sort-media-by filename
```


### Wosc17 Gallery

Run:

```
cd wosc17/
thumbsup --input ./photos --output ./gallery --title 'First International Workshop on Serverless Computing (WoSC) 2017 Gallery' --theme cards --thumb-size 200 --albums-from date  --sort-media-by filename
```

Then edit gallery/2017-06.html
to point to workshop index.html with ../index.html:

```
sed -i '' -e 's/index.html/..\/index.html/g' gallery/2017-06.html
```

or manually:

```
        <h1><a href="../index.html">ICDCS Wworkshop on Serverless Computing (WoSC) 2017 Gallery</a></h1>
```

```
    <a class="breadcrumb-item" href="../index.html">Home</a>&nbsp;/&nbsp;<a class="breadcrumb-item" href="2017-06.html">2017-06</a>
```

### Tutorial Gallery

Run:

```
cd tutorial/
thumbsup --input ./photos --output ./gallery --title 'Serverless Tutorial 2017 Gallery' --theme cards --thumb-size 200 --albums-from date 
```

```
sed -i '' -e 's/index.html/..\/index.html/g' gallery/2017-06.html
```
