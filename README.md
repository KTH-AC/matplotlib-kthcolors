# matplotlib-kthcolors
Collection of KTH colors for matplotlib

## Installation
Installation steps may vary depending on your OS.
In general, I would expect the following instructions to work just fine.
If you have trouble, see [this page in the python documentation](https://docs.python.org/2.7/distutils/introduction.html#distutils-simple-example).

- Clone this repository.
```
git clone https://github.com/adaldo/matplotlib-kthcolors
```
- Enter the repository directory and run the setup script.
```
cd matplotlib-kthcolors
python setup.py install
```

## Usage
- Import the module `kthcolors`.
- Use `matplotlib` as usual. Here is an example.
```
import kthcolors
import matplotlib.pyplot as plt

plt.figure()
plt.plot([1,2],[2,3],color='kthblue')
plt.show()
```
- Enjoy.
