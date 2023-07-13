from character import *

class Base_Series:
    def __init__(self, soul1, soul2, tot_trig):
        self.ch1 = Character(soul_point=2, soul1=soul1, soul2=soul2, tot_trig=tot_trig, direct_attack=0)
        self.ch2 = Character(soul_point=2, soul1=soul1, soul2=soul2, tot_trig=tot_trig, direct_attack=0)
        self.ch3 = Character(soul_point=2, soul1=soul1, soul2=soul2, tot_trig=tot_trig, direct_attack=0)
    def climax_phase(self, env):
        return env
    def kill(self, env):
        env = self.climax_phase(env)
        env = self.ch1.attack_phase(env)
        env = self.ch2.attack_phase(env)
        env = self.ch3.attack_phase(env)
        return env.check_death()

class PAD_D(Base_Series):
    def __init__(self, soul1, soul2, tot_trig):
        self.ch1 = PAD_0dragon_full(soul_point=3, soul1=soul1, soul2=soul2, tot_trig=tot_trig, direct_attack=0)
        self.ch2 = PAD_0dragon_full(soul_point=3, soul1=soul1, soul2=soul2, tot_trig=tot_trig, direct_attack=0)
        self.ch3 = PAD_0dragon_full(soul_point=3, soul1=soul1, soul2=soul2, tot_trig=tot_trig, direct_attack=0)
