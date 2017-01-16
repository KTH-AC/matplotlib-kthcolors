# Matplotlib KTH Colors
Collection of KTH colors for matplotlib


## Installation
Installation steps may vary depending on your OS.
In general, I would expect the following instructions to work just fine.

You need Python 2 or 3 on your computer.
Moreover, you need `python-pip` and `python-setuptools`.
In the remote event that you do not have them already, grab them with your favorite package manager.
For example, on Linux, type this in a terminal:
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
  sudo python setup.py sdist bdist_wheel
  sudo pip install ./dist/kthcolors-0.0.2.tar.gz
  ```

3. If you want, you can remove the repository directory now.

  ```
  cd ..
  sudo rm -r matplotlib-kthcolors
  ```


## Usage

1. Import the module `kthcolors`.
2. Use `matplotlib` as usual.
3. Enjoy.

See `example.py` for example usage.

## Uninstall

1. Type this in a terminal

  ```
  sudo pip uninstall kthcolors
  ```

2. Write a mail to <antonio.adaldo.89@gmail.com> to let me know what went wrong.
