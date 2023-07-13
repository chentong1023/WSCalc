import sys
sys.path.append("..")
from env import Env
from series import Base_Series
from character import Character
import matplotlib.pyplot as plt

def main():
    iter_num = 10000
    low = []
    mid = []
    high = []
    axis_name = []
    for level_i in [2, 3]:
        for clock_i in range(7):
            low_count = 0
            mid_count = 0
            high_count = 0
            for iter in range(iter_num):
                series = Base_Series(10, 0, 50)
                low_density_env = Env(50-5-5-5-level_i-clock_i, 6, clock_i, 0, 0, 0, level_i) # 5 hands, 5 fields, 5 stocks, 6 climax, rate: 5.0
                mid_density_env = Env(50-6-5-6-level_i-clock_i, 7, clock_i, 0, 0, 0, level_i) # 6 hands, 5 fields, 6 stocks, 7 climax, rate: 4.0
                high_density_env = Env(50-7-5-8-1-level_i-clock_i, 8, clock_i, 0, 0, 0, level_i) # 7 hands, 5 fields, 8 stocks, 1 memory, 8 climax, rate: 3.0
                low_count += series.kill(low_density_env)
                mid_count += series.kill(mid_density_env)
                high_count += series.kill(high_density_env)
            low.append(low_count / iter_num)
            mid.append(mid_count / iter_num)
            high.append(high_count / iter_num)
            axis_name.append("%d-%d"%(level_i, clock_i))
    plt.plot(axis_name, low, label='low_density')
    plt.plot(axis_name, mid, label='middle_density')
    plt.plot(axis_name, high, label='high_density')
    plt.legend(loc='upper left')
    plt.title("[demo]3 Simple 2 soul character")
    plt.savefig("../fig/demo.png")
    plt.show()


if __name__ == "__main__":
    main()