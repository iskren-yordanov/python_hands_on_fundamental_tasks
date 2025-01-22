"""Entry point for task 6"""

import simulation

def main():
    """Main function"""
    print("Simulation with 2 dices and 5000 rolls")
    s = simulation.Simulation(4,5000)
    s.simulate(visualize=True)

    print("Simulation with 4 dices and 500 rolls")
    s.fine_tune_simulation(4,500)
    s.simulate()

    # this is nornal distrubution

if __name__=="__main__":
    main()
