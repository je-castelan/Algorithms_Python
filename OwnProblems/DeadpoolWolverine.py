
import random
import time

# Challenge proposed by Mouredev in the following URL
# https://www.linkedin.com/posts/braismoure_nuevo-reto-de-programaci%C3%B3n-publicado-activity-7226317415150743552-WeMm?utm_source=share&utm_medium=member_desktop


class RandomGenerator:
    @staticmethod
    def getAttackPower(min: int, max: int) -> int :
        return random.choice([i for i in range(min, max, 10)])
    
    @staticmethod
    def isEvasived(percentage_evasiveness: int) -> bool :
        evasiness_random = random.randint(0, 100)
        return percentage_evasiveness > evasiness_random

class Figther:

    def __init__(self, name: str, health_points: int, min_damage: int, max_damage: int, evasiveness: int) -> None:
        self.name = name
        self.health_points = health_points
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.is_regenerating = False
        self.evasiveness = evasiveness
        validator = FighterValidator()
        validator.validate(self)

    def attack(self, fighter: 'Figther') -> None:
        if self.is_regenerating:
            print(f"{self.name} is regenerating")
            self.is_regenerating = False
        else:
            damage = RandomGenerator.getAttackPower(self.min_damage, self.max_damage)
            print(f"{self.name} attacks to {fighter.name} - impact of {damage}")
            fighter.impact(self, damage)

    def impact(self, fighter: 'Figther', damage: int) -> None:
        is_evasived = RandomGenerator.isEvasived(self.evasiveness)
        if not (is_evasived):
            self.health_points -= damage
            print("PUNCH")
            if (fighter.max_damage == damage):
                self.is_regenerating = True
                print("Critical hit")
        else:
            print(f"Attack from {fighter.name} was missed")

    def isDefeated(self):
        return self.health_points <= 0


class FighterValidator:

    def validate(self, fighter: Figther) -> None :
        if (fighter.min_damage >= fighter.max_damage) :
            raise Exception(f"Min damage value cannot be higher or equal to the max damage value")

        if (fighter.evasiveness < 0):
            raise Exception(f"Evasiveness must be highter than zero")

        if (fighter.evasiveness > 100):
            raise Exception(f"Evasiveness must be lower than 100")


class Battle:

    def __init__(self, wolverine_health_points: int, deadpool_health_points: int) -> None:
        self.wolverine = Figther("Wolverine", wolverine_health_points, 10, 120, 20)
        self.deadpool = Figther("Deadpool", deadpool_health_points, 10, 100, 25)
        self.display = BattleDisplay()
        self.pause = 5
    
    def isFinished(self) -> bool:
        return self.wolverine.isDefeated() or self.deadpool.isDefeated()
    
    def fight(self) -> None:
        self.display.showStatus(self.deadpool, self.wolverine, True)
        while (not self.isFinished()) :
            self.turn(self.wolverine, self.deadpool)
            self.turn(self.deadpool, self.wolverine)
        winner = self.deadpool if self.wolverine.isDefeated() else self.wolverine
        self.display.showWinner(winner)
    
    def turn(self, attacker: Figther, impacted: Figther) -> None:
        if (not attacker.isDefeated()):
            attacker.attack(impacted)
            self.display.showStatus(self.deadpool, self.wolverine)
            time.sleep(self.pause)

class BattleDisplay:

    def showStatus(self, fighter_1: Figther, fighter_2: Figther, is_initializing: bool = False) -> None:
        if (is_initializing):
            print("Let's begin the fight")
        print(f"{fighter_1.name}: {fighter_1.health_points} - {fighter_2.name} {fighter_2.health_points}")
        print("--------------------------------------------")

    def showWinner(self, figther: Figther) -> None:
        print(f"Figther {figther.name} is the winner")

    


if __name__ == "__main__":
    battle = Battle(500, 550)
    battle.fight()