import numpy as np
import random

class Env:
    def __init__(self, deck_n, deck_c, clock_n, clock_c, wait_n, wait_c, level):
        self.deck_n = deck_n
        self.deck_c = deck_c
        self.clock_n = clock_n
        self.clock_c = clock_c
        self.wait_n = wait_n
        self.wait_c = wait_c
        self.level = level
        self.top_check = []
    
    def query_state(self):
        return self.deck_n, self.deck_c, self.wait_n, self.wait_c
    
    def get_top_card(self):
        if len(self.top_check) == 0:
            damage_check = np.random.rand() < self.deck_c / self.deck_n
        else:
            damage_check = self.top_check.pop(0)
        return damage_check
    
    def query_top_card(self):
        if len(self.top_check) == 0:
            damage_check = np.random.rand() < self.deck_c / self.deck_n
        else:
            damage_check = self.top_check[0]
        return damage_check
    
    def refresh(self):
        self.deck_n = self.wait_n
        self.deck_c = self.wait_c
        self.uncancelable_damage(1)

    def level_check(self):
        if self.clock_n >= 7:
            self.level += 1
            self.clock_n -= 7
            self.wait_n += 6
            self.wait_c += self.clock_c
            self.clock_c = 0

    def check_death(self):
        return self.level >= 4
    
    def cancelable_damage(self, d):
        for i in range(d):
            damage_check = self.get_top_card()
            self.deck_n -= 1
            self.deck_c -= damage_check
            if self.deck_n == 0:
                self.refresh()
            if damage_check:
                self.wait_n += i + 1
                self.wait_c += 1
                return True
        self.clock_n += d
        self.level_check()
        return False

    def uncancelable_damage(self, d):
        for i in range(d):
            damage_check = self.get_top_card()
            self.deck_n -= 1
            self.deck_c -= damage_check
            if self.deck_n == 0 and len(self.top_check) == 0:
                self.refresh()
            self.clock_n += 1
            self.clock_c += damage_check
            self.level_check()
    
    def wait2deck(self, d_non):
        self.deck_n += min(self.wait_n - self.wait_c, d_non)
    
    def top_check_remove_climax(self, d):
        pre_top = []
        for i in range(d):
            damage_check = self.query_top_card()
            if damage_check:
                self.deck_n -= 1
                self.deck_c -= 1
                if self.deck_n == 0:
                    self.refresh()
            else:
                pre_top.append(damage_check)
        self.top_check = pre_top

    def top_check_reorder(self, d):
        pass