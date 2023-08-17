# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from git.repo import Repo
import os
import shutil
import stat

def file_remove_readonly(func, path, execinfo):
    os.chmod(path, stat.S_IWUSR)#修改文件权限
    func(path)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    n ="dasdas:dsa"
    print(n.index(':'))
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # download_path = os.path.join('santa', 'NB')
    # # # print(download_path)
    # # # Repo.clone_from('https://gitee.com/NJU-TJL/PacManX', to_path=download_path).git.checkout('v1.0')
    # # # download_path = os.path.join('santa', 'dsasdNB')
    # Repo.clone_from('https://gitee.com/NJU-TJL/PacManX.git', to_path=download_path, b='v1.0')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
