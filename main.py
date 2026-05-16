from pathlib import Path
import sys

_workspace_root = Path(__file__).resolve().parent
_venv_site_packages = _workspace_root / ".venv" / "lib" / "python3.12" / "site-packages"
_venv_site_packages_alt = (
    _workspace_root / ".venv" / "lib64" / "python3.12" / "site-packages"
)

for _site_packages_path in (_venv_site_packages, _venv_site_packages_alt):
    if _site_packages_path.is_dir():
        site_packages_str = str(_site_packages_path)
        if site_packages_str not in sys.path:
            sys.path.insert(0, site_packages_str)


"""Importing flat files from the web with urllib"""
# from urllib.request import urlretrieve
# import pandas as pd

# # assign url of file:
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
# urlretrieve(url, "data/winequality-white.csv")  # save file locally

# # read file into DataFrame & print its head
# df = pd.read_csv("data/winequality-white.csv", sep=";")
# print(df.head())


"""Importing flat files from the web with pandas"""
# import matplotlib.pyplot as plt
# import pandas as pd

# # assign url of file:
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

# # read file into DataFrame & print its head
# df = pd.read_csv(url, sep=";")
# print(df.head())

# # Plot first column of df
# df.iloc[:, 0].plot.hist()
# plt.xlabel("fixed acidity")
# plt.ylabel("count")
# plt.show()


""" Importing non-flat files from the web with pandas"""
import pandas as pd

# assign url of file:
url = "https://assets.datacamp.com/course/importing_data_into_r/latitude.xls"

# read in all sheets of Excel file
xls = pd.read_excel(url, sheet_name=None)

# print the sheetnames to the shell
print(xls.keys())
