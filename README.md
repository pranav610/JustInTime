# JustInTime - A Motor Part Shop Software

A motor part shop software inspired by the just-in-time (JIT) philosophy. <br />
The software has following amazing features:

<ul>
    <li>Generate the revenue for each day.</li>
    <li>Generate the revenue graph the end of the month.</li>
    <li>List of the items to be ordered at the end of each day.</li>
    <li>Features to add/edit/remove certain Vendors or items.</li>
</ul>


## 1. Prerequisites
### 1.1 **Ubuntu** or **Windows**
This software has been tested on Ubuntu 20.04 and Windows 11.

### 1.2. **Libraries** 
We used the following libraries:  [Matplotlib](https://matplotlib.org/), [PyQt5](https://pypi.org/project/PyQt5/), [PySide2](https://pypi.org/project/PySide2/), [sqlparse](https://pypi.org/project/sqlparse/) 
```bash
  pip install -r requirements.txt
```
## 2. Software Installation
Clone the repository
```bash
  git clone https://github.com/pranav610/JustInTime
```

Open the folder
```bash
  cd JustInTime
```

Copy ```DataBase.db``` from ```preData``` folder and paste in the ```JustInTime``` folder
```bash
  sudo cp preData/DataBase.db ./
```
Start the application

```bash
  python3 main.py
```

## Screenshots

<img src = "./images/SoftwareOverview.gif" alt = "main.gif" />

  
## TODO

- Adding features so that Vendors and Customers can use the same software remotely.

  
## Authors

- [@Sidharth](https://github.com/sidvisw)
- [@Pranav](https://github.com/pranav610)
- [@Swapnil](https://github.com/linpawsivsasay123)

  