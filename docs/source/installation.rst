Installation
==========================================

Standard
------------------------------------------

Installation is supported on Python >=3.7 via pip. This is typically all that's
required.


.. code-block::

      pip install dcargs


Development
------------------------------------------

If you're interested in development, :code:`dcargs` can also be installed from
source.

.. code-block::

      # Clone repository.
      git clone git@github.com:brentyi/dcargs.git
      cd dcargs

      # Install development dependencies.
      pip install -e ".[testing,type-checking]"

      # Run tests.
      pytest

      # Check types.
      mypy --install-types .

