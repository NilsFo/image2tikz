[![GitHub Stars](https://img.shields.io/github/stars/RUB-NilsFo/image2tikz.svg?style=social&label=Star)](https://github.com/NilsFo/image2tikz)
&nbsp;
[![GitHub Downloads](https://img.shields.io/github/downloads/NilsFo/image2tikz/total?style=social)](https://github.com/NilsFo/image2tikz/releases)


[![Follow us on Twitter](https://img.shields.io/twitter/follow/NilsFoer?style=social&logo=twitter)](https://twitter.com/intent/follow?screen_name=NilsFoer) &nbsp;

[![Contributors](https://img.shields.io/github/contributors/NilsFo/image2tikz?style=flat)](https://github.com/NilsFo/image2tikz/graphs/contributors)
&nbsp;
[![License](https://img.shields.io/github/license/NilsFo/image2tikz?color=green&style=flat)](https://github.com/NilsFo/image2tikz/LICENSE)
&nbsp;
![Size](https://img.shields.io/github/repo-size/NilsFo/image2tikz?style=flat)
&nbsp;
[![Issues](https://img.shields.io/github/issues/NilsFo/image2tikz?style=flat)](https://github.com/NilsFo/image2tikz/issues)
&nbsp;
[![Pull Requests](https://img.shields.io/github/issues-pr/NilsFo/image2tikz?style=flat)](https://github.com/NilsFo/image2tikz/pulls)
&nbsp;
[![Commits](https://img.shields.io/github/commit-activity/m/NilsFo/image2tikz?style=flat)](https://github.com/NilsFo/image2tikz/)

***

# image2tikz
Turns your raster images into tikz code.
Use to recreate your images as PDFs.
Output keeps bitmap properties.

Runs with questionable performance.

### Why do this?
_“Your scientists were so preoccupied with whether they could, they didn’t stop to think if they should.”_

## Usage
Intended as a CLI application.
Use with 8-bit bitmap images without alpha channel.
Use command line arguments to customize execution.

In a nutshell, run this tool like this:

```python  image2tikz.py -i <path/to/your/image>```


### Help
For help, use the `-h` argument:

```python  image2tikz.py -h```

You can also create a _Issue_ or _Pull Request_ to help.
Feedback is welcome.

### Example Data
See the `example` directory of this repository for example input and output data.
Located there is a `mandrill.png`.
Converted pixel info (script output) is saved as a `.pgf` text file.
It can be compiled to `.pdf` with LaTeX.

### Note
High resolution images quickly exceed tikz' maximum memory limit.
Recommended image size is 32x32 pixel.
You also may include this library in your tex document:

````
\usepackage{morefloats}
````
