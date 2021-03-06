# Alternative tools

The core functionality of `dcargs` — generating argument parsers from type
annotations — can be found as a subset of the features offered by many other
libraries. A summary of some distinguishing features:

|                                                                                                          | Literals                                                 | Generics | Docstrings as helptext | Nesting | Subparsers | Containers |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------- | ---------------------- | ------- | ---------- | ---------- |
| **dcargs**                                                                                               | ✓                                                        | ✓        | ✓                      | ✓       | ✓          | ✓          |
| [datargs](https://github.com/roee30/datargs)                                                             | ✓                                                        |          |                        |         | ✓          | ✓          |
| [tap](https://github.com/swansonk14/typed-argument-parser)                                               | ✓                                                        |          | ✓                      |         | ✓          | ✓          |
| [simple-parsing](https://github.com/lebrice/SimpleParsing)                                               | [soon](https://github.com/lebrice/SimpleParsing/pull/86) |          | ✓                      | ✓       | ✓          | ✓          |
| [argparse-dataclass](https://pypi.org/project/argparse-dataclass/)                                       |                                                          |          |                        |         |            |            |
| [argparse-dataclasses](https://pypi.org/project/argparse-dataclasses/)                                   |                                                          |          |                        |         |            |            |
| [dataclass-cli](https://github.com/malte-soe/dataclass-cli)                                              |                                                          |          |                        |         |            |            |
| [clout](https://pypi.org/project/clout/)                                                                 |                                                          |          |                        | ✓       |            |            |
| [hf_argparser](https://github.com/huggingface/transformers/blob/master/src/transformers/hf_argparser.py) |                                                          |          |                        |         |            | ✓          |
| [pyrallis](https://github.com/eladrich/pyrallis/)                                                        |                                                          |          | ✓                      | ✓       |            | ✓          |

Note that most of these other libraries are generally aimed specifically at
_dataclasses_ rather than general typed callables, but offer other features that
you might find useful, such as registration for custom types (`pyrallis`),
different approaches for serialization and config files (`tap`, `pyrallis`),
simultaneous parsing of multiple dataclasses (`simple-parsing`), etc.
