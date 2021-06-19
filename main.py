# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from utils_package import base_module

import model_zoo.wide_and_deep.train as wideDeepModel
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    temp = wideDeepModel.TrainWideDeeoModel()
    temp.train_model()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/