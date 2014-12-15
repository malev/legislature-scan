# Legislature Scanner

Texas Legislative Session is around the corner and people are starting to feel the excitement. Everyone is counting the seconds till Jan. 13, 2015. And someone will have to count the votes.

After every voting session, a machine at the legislature prints a paper like this:

![votes](http://src.codingnews.info.s3.amazonaws.com/IMG_20140919_113410.jpg) 

And someone has to count the votes by hand. This is where **legislature-scan** enter the room:

    pip install legislature-scanner

And from the interpreter just:

```python
>>> from legislature-scanner import LegScanner
>>> leg_scanner = LegScanner('IMG_20140919_113410.jpg')
>>> leg_scanner.count(roster=2013)
{
  "Gonzalez": "nay",
  "Bonnen, D": "*",
  "Bonnen, G": "*",
  # ...
}
```

From the command line:

    $ python all.py data/IMG_20141006_184225.jpg

**Happy session!**

# TODO

* Add README
* Make it work!
* Add setup.py
* Make it a python package
* Update roster with 2015 names

# More info
* http://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/
* http://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
