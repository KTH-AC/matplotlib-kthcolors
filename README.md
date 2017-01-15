# matplotlib-kthcolors
Collection of KTH colors for matplotlib


## Installation
Installation steps may vary depending on your OS.
In general, I would expect the following instructions to work just fine.

You need `python-pip` and `python-setuptools`. In the remote event that you do not have them already, grab them with your favorite package manager.
For example, on Linux:
```
sudo apt-get install python-pip python-matplotlib
```

1. Clone this repository.

  ```
  git clone https://github.com/adaldo/matplotlib-kthcolors
  ```

2. Enter the repository directory and run the setup script.

  ```
  cd matplotlib-kthcolors
  python setup.py install
  ```

3. If you want, you can remove the repository directory now.

  ```
  cd ..
  sudo rm -r matplotlib-kthcolors
  ```


## Usage

1. Import the module `kthcolors`.

2. Use `matplotlib` as usual. Here is an example.

  ```
  import kthcolors
  import matplotlib.pyplot as plt

  plt.figure()
  plt.plot([1,2],[2,3],color='kthblue')
  plt.show()
  ```

3. Enjoy.


## Uninstall

1. Type this in a terminal

  ```
  pip uninstall kthcolors
  ```

2. [Write me a mail](people.kth.se/~adaldo) to let me know what went wrong.
