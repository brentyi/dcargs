.. Comment: this file is automatically generated by `update_example_docs.py`.
   It should not be modified manually.

10. Multiple Subparsers
==========================================


Multiple unions over nested types are populated using a series of subparsers.



.. code-block:: python
       :linenos:

       from __future__ import annotations
       
       import dataclasses
       from typing import Literal, Tuple, Union
       
       import dcargs
       
       # Possible dataset configurations.
       
       
       @dataclasses.dataclass
       class MnistDataset:
           binary: bool = False
           """Set to load binary version of MNIST dataset."""
       
       
       @dataclasses.dataclass
       class ImageNetDataset:
           subset: Literal[50, 100, 1000]
           """Choose between ImageNet-50, ImageNet-100, ImageNet-1000, etc."""
       
       
       # Possible optimizer configurations.
       
       
       @dataclasses.dataclass
       class AdamOptimizer:
           learning_rate: float = 1e-3
           betas: Tuple[float, float] = (0.9, 0.999)
       
       
       @dataclasses.dataclass
       class SgdOptimizer:
           learning_rate: float = 3e-4
       
       
       # Train script.
       
       
       def train(
           dataset: Union[MnistDataset, ImageNetDataset] = MnistDataset(),
           optimizer: Union[AdamOptimizer, SgdOptimizer] = AdamOptimizer(),
       ) -> None:
           """Example training script.
       
           Args:
               dataset: Dataset to train on.
               optimizer: Optimizer to train with.
       
           Returns:
               None:
           """
           print(dataset)
           print(optimizer)
       
       
       if __name__ == "__main__":
           dcargs.cli(train)

------------

.. raw:: html

        <kbd>python 10_multiple_subparsers.py</kbd>

.. program-output:: python ../../examples/10_multiple_subparsers.py

------------

.. raw:: html

        <kbd>python 10_multiple_subparsers.py --help</kbd>

.. program-output:: python ../../examples/10_multiple_subparsers.py --help

------------

.. raw:: html

        <kbd>python 10_multiple_subparsers.py mnist-dataset --help</kbd>

.. program-output:: python ../../examples/10_multiple_subparsers.py mnist-dataset --help

------------

.. raw:: html

        <kbd>python 10_multiple_subparsers.py mnist-dataset adam-optimizer --optimizer.learning-rate 3e-4</kbd>

.. program-output:: python ../../examples/10_multiple_subparsers.py mnist-dataset adam-optimizer --optimizer.learning-rate 3e-4
