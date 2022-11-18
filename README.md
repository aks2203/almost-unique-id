# almost-unique-id
Get almost unique ID names. This package randomly selects an `adjective-Name` pair from 24,567,933 unique pairs. 

These IDs serve much the same pupose as generating a random hex string, that is to get random names for things that are (extrememly) unlikely to overlap. This project was developed alongside several scientific research projects where many trial of an experiment needed to be named distictly. We find that Enlglish languane keys are easier to discuss and remember than some number of digits/letters that might be unpronounceable. 

Feel free to use this for any such application. If you have a use for this that you think is worth mentioning in the README, feel free to open a PR and add it so the description.

## Installation

This package is installable with pip:

```
$ pip install almost-unique-id
```

Or, you can install it from source by git cloning it and installing with pip as follows.

```
$ git clone https://github.com/aks2203/almost-unique-id.git
$ cd almost-unique-id
$ pip install -e .
```

## Example

```
from almost_unique_id import generate_id

run_id = generate_id()
```

### Sources:

The names and adjectives are copied from other sources. An effort was made to find a list without explicit content.

The names are copied from this [file](https://www.usna.edu/Users/cs/roche/courses/s15si335/proj1/files.php%3Ff=names.txt.html). 

The adjectives are copied from thi [file](https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913).

## Development and Contribution

*We believe in open-source community driven software development. Please open issues and pull requests with any questions or improvements you have.*

