from env import Env
import random
class Character:
    def __init__(self, soul_point, soul1, soul2, tot_trig, direct_attack):
        self.soul_point = soul_point
        self.soul1 = soul1
        self.soul2 = soul2
        self.tot_trig = tot_trig
        self.direct_attack = direct_attack

    def attack(self, env):
        self.soul_point += self.direct_attack
        trig = random.randint(0, self.tot_trig)
        if trig < self.soul2:
            self.soul_point += 2
        elif trig < self.soul1 + self.soul2:
            self.soul_point += 1
        cancel = env.cancelable_damage(self.soul_point)
        return env, cancel

    def attack_phase(self, env):
        env, _ = self.attack(env)
        return env

