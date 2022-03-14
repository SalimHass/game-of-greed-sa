import random
from collections import Counter
from abc import ABC, abstractclassmethod
from turtle import clear




class GameLogic:

    def __init__(self) -> None:
        pass


    @staticmethod
    def roll_dice(length):
        rolls = tuple([random.randint(1, 6) for _ in range(length)])
        return rolls

    @staticmethod
    def calculate_score(roll_dice):
        pass


class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self,points):
        self.shelved = points

    def bank(self):
        self.balance = self.balance + self.shelved
        point_added = self.shelved
        self.shelved = 0
        return point_added

    def clear(self):
        self.shelved = 0

