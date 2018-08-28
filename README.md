# Summary Separator
---
## What is this?
This is a short script to parse TensorFlow summaries and separate them into one files per summary tag.

I wrote this so I can continue using TensorFlow's [summary operations][1] with large summary files. After a few hundred thousand events, they grow too large to be efficiently displayable by [TensorBoard][2] and have to be processed elsewhere.


[1]: https://www.tensorflow.org/api_guides/python/summary#Generation_of_Summaries
[2]: https://www.tensorflow.org/guide/summaries_and_tensorboard


---
## How it works
To execute, the script needs the following paramters:

    python summary_separator.py -f path/to/file -t tag1,tag2,tag3 -o path/to/output

* path/to/file: File path of the summary file you want to work with. Relative or absolute path both work.

* tags: a list of summary tags to filter for, separated by comma and without whitespace. No quotes needed.
  * omitting this parameter or passing "all" will filter for all tags
  * only takes full tag names, no wildcards
* path/to/output: Path to where the output files will be placed
