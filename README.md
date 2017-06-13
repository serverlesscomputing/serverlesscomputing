# serverlesscomputing


## Gallery

To generate gallery for the workshop

Install thumbsup from https://thumbsup.github.io/docs/

Then run:

```
cd wosc17/
```

```
thumbsup --input ./workshop-pictures --output ./gallery --title 'First International Workshop on Serverless Computing (WoSC) 2017 Gallery' --theme cards --thumb-size 200 --albums-from date  --sort-media-by filename
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

