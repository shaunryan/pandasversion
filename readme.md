# Pandas Compatability Test


### Run the Test

Build the docker files:
```
docker build -t pandas:0.19.2 -f pandas0-19-2.dockerfile .
docker build -t pandas:1.0.1 -f pandas1-0-1.dockerfile .
```

Run the test:

```
docker-compose up
```

### Expected Output

**Python 3.7.1 & pandas:1.0.1 will fail**

```
pandas101_1   | raise TypeError(f"dtype '{dtype}' not understood")
pandas101_1   | TypeError: dtype '<enum 'Color'>' not understood
```

**Python 3.5.2 & pandas:0.19.2 will succeed**

Note that in order to get this to succeed I had to downgrade numpy below what comes with pandas. The packaged version of numpy doesn't work either.

This will however run successfully on databricks runtime 5.5

```
pandas0192_1  |   color    make    model  year
pandas0192_1  | 0     1  toyota  corolla  2014
pandas0192_1  | 1     2   honda    civic  2018
pandas0192_1  | 2     3  hyndai   accent  2020
pandas0192_1  | 3     4  nissan   sentra  2017
```


