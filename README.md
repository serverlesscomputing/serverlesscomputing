# serverlesscomputing


## Gallery

To generate gallery for the workshop

Install thumbsup from https://thumbsup.github.io/docs/

Copy JPG files to photos/ subdirectory in woscN/ directory

```
cd woscN
mkdir photos
```

### WoSC 2 Gallery

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

Currently fails missing .congif somehow ...

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
