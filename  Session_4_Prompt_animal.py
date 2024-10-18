

class Animal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length        # Length of the arms (float)
        self.leg_length = leg_length        # length of the legs (float)
        self.num_eyes = num_eyes            # Number of eyes (int)
        self.has_tail = has_tail            # Does it have a tail? (bool)
        self.is_furry = is_furry            # Is it furry? (bool)

    def describe(self):
        print(f"Animal Characteristics:")
        print(f"Arm length: {self.arm_length} units")
        print(f"Leg length {self.leg_length} units") 
        print(f"Number of Eyes {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry: {'Yes' if self.is_furry else 'No'}")

def main():
    my_animal = Animal(10, 10, 2, True, True)

    #Describe the animal
    my_animal.describe()

if __name__ == "__main__":
    main()


