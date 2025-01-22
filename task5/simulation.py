"""File containing details for Simulation class"""

import matplotlib.pyplot as plt
import dice

class Simulation():
    """Simulation class definition"""

    def __init__(self, cnt_dice: int, cnt_rows: int):
        """Simulation constructor"""
        self.cnt_dice = cnt_dice
        self.cnt_rows = cnt_rows

        self.dice = dice.Dice()
        self.list_matches = None

    def fine_tune_simulation(self, cnt_dice: int, cnt_rows: int):
        """Method to modify the simulation parameters"""
        self.cnt_dice = cnt_dice
        self.cnt_rows = cnt_rows

    def get_roll(self):
        """Helper method do get a roll baed on count off dices"""
        current_roll = 0
        for _ in range(self.cnt_dice):
            current_roll += self.dice.roll()

        return current_roll

    #%%
    def simulate(self, visualize=False):
        """method to perform the simulation"""

        # the 0 index will not be used we will use indexxes 1 to X depending on the count of dices
        list_matches = [0 for x in range(6 * self.cnt_dice +1)]

        for _ in range(self.cnt_rows):
            current_roll = self.get_roll()
            list_matches[current_roll] +=1

        if visualize:
            fig, ax = plt.subplots()

            fruits = [str(x) for x in range(1,self.cnt_dice*6 + 1)]
            counts = list_matches[1::]

            #bar_labels = ['red', 'blue', '_red', 'orange']
            #bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

            ax.bar(fruits, counts) #, label=bar_labels, color=bar_colors)

            ax.set_ylabel('Num of rolls per outcome')
            ax.set_title('Dice outcomes')
            #ax.legend(title='Legend title')

            plt.show()
        else:
            print(list_matches[1::])
