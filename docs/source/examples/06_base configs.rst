.. Comment: this file is automatically generated by `update_example_docs.py`.
   It should not be modified manually.

6. Base Configs
==========================================


We can integrate ``dcargs.cli()`` into common configuration patterns: here, we select
one of multiple possible base configurations, and then use the CLI to either override
(existing) or fill in (missing) values.

Note that our interfaces don't prescribe any of the mechanics used for storing or
choosing between base configurations. A Hydra-style YAML approach could just as easily
be used for the config libary (although we generally prefer to avoid YAMLs; staying in
Python is convenient for autocompletion and type checking). For selection, we could also
avoid fussing with ``sys.argv`` by using a ``BASE_CONFIG`` environment variable.



.. code-block:: python
       :linenos:

       import sys
       from dataclasses import dataclass
       from typing import Callable, Dict, Literal, Tuple, TypeVar, Union
       
       from torch import nn
       
       import dcargs
       
       
       @dataclass(frozen=True)
       class AdamOptimizer:
           learning_rate: float = 1e-3
           betas: Tuple[float, float] = (0.9, 0.999)
       
       
       @dataclass(frozen=True)
       class SgdOptimizer:
           learning_rate: float = 3e-4
       
       
       @dataclass(frozen=True)
       class ExperimentConfig:
           # Dataset to run experiment on.
           dataset: Literal["mnist", "imagenet-50"]
       
           # Optimizer parameters.
           optimizer: Union[AdamOptimizer, SgdOptimizer]
       
           # Model size.
           num_layers: int
           units: int
       
           # Batch size.
           batch_size: int
       
           # Total number of training steps.
           train_steps: int
       
           # Random seed. This is helpful for making sure that our experiments are all
           # reproducible!
           seed: int
       
           # Activation to use. Not specifiable via the commandline.
           activation: Callable[[], nn.Module]
       
       
       # Note that we could also define this library using separate YAML files (similar to
       # `config_path`/`config_name` in Hydra), but staying in Python enables seamless type
       # checking + IDE support.
       base_configs = {
           "small": ExperimentConfig(
               dataset="mnist",
               optimizer=SgdOptimizer(),
               batch_size=2048,
               num_layers=4,
               units=64,
               train_steps=30_000,
               # The dcargs.MISSING sentinel allows us to specify that the seed should have no
               # default, and needs to be populated from the CLI.
               seed=dcargs.MISSING,
               activation=nn.ReLU,
           ),
           "big": ExperimentConfig(
               dataset="imagenet-50",
               optimizer=AdamOptimizer(),
               batch_size=32,
               num_layers=8,
               units=256,
               train_steps=100_000,
               seed=dcargs.MISSING,
               activation=nn.GELU,
           ),
       }
       
       
       T = TypeVar("T")
       
       
       def cli_from_base_configs(base_library: Dict[str, T]) -> T:
           """Populate an instance of `cls`, where the first positional argument is used to
           select from a library of named base configs."""
           # Get base configuration name from the first positional argument.
           if len(sys.argv) < 2 or sys.argv[1] not in base_library:
               valid_usages = map(lambda k: f"{sys.argv[0]} {k} --help", base_library.keys())
               raise SystemExit("usage:\n  " + "\n  ".join(valid_usages))
       
           # Get base configuration from our library, and use it for default CLI parameters.
           default_instance = base_library[sys.argv[1]]
           return dcargs.cli(
               type(default_instance),
               prog=" ".join(sys.argv[:2]),
               args=sys.argv[2:],
               default_instance=default_instance,
               # `avoid_subparsers` will avoid making a subparser for unions when a default is
               # provided; in this case, it simplifies our CLI but makes it less expressive
               # (cannot switch away from the base optimizer types).
               avoid_subparsers=True,
           )
       
       
       if __name__ == "__main__":
           config = cli_from_base_configs(base_configs)
           print(config)

------------

.. raw:: html

        <kbd>python 06_base_configs.py</kbd>

.. program-output:: python ../../examples/06_base_configs.py

------------

.. raw:: html

        <kbd>python 06_base_configs.py small --help</kbd>

.. program-output:: python ../../examples/06_base_configs.py small --help

------------

.. raw:: html

        <kbd>python 06_base_configs.py small --seed 94720</kbd>

.. program-output:: python ../../examples/06_base_configs.py small --seed 94720

------------

.. raw:: html

        <kbd>python 06_base_configs.py big --help</kbd>

.. program-output:: python ../../examples/06_base_configs.py big --help

------------

.. raw:: html

        <kbd>python 06_base_configs.py big --seed 94720</kbd>

.. program-output:: python ../../examples/06_base_configs.py big --seed 94720
