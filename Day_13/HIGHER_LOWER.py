from game_data import data
import random

# Take the two data from game_data

class Profile:
    def __init__(self, name, follower_count, description, country):
        self.name = name
        self.follower_count = follower_count
        self.description = description
        self.country = country

    def display_info(self):
        """Returns a formatted string that the user can view"""
        return f"[Name]: {self.name} [Description]: {self.description} [Country]: {self.country}"

class Game:

    def __init__(self):
        self.profiles = [Profile(**x) for x in data]
        self.left_account = None
        self.right_account = None
        self.score = 0

    def get_random_profiles(self):
        p1 = random.choice(self.profiles)
        p2 = random.choice(self.profiles)
        while p1 == p2:
            p2 = random.choice(self.profiles)
        return p1, p2

    def comparison(self, profile_1, profile_2):
        if profile_1.follower_count > profile_2.follower_count:
            return profile_1
        else:
            return profile_2

    def user_input(self):
        while True:

            player_choice = input("'A' or 'B'?: ")

            if player_choice == 'A':
                return 'A'
            elif player_choice == 'B':
                return  'B'
            else:
                print("Invalid, try again.")


    def Play(self):
        """Starts and plays the game"""
        print("Welcome to Higher / Lower")

        self.left_account, self.right_account = self.get_random_profiles()
        game_should_continue = True

        while game_should_continue:
            print(f"\nCompare A: {self.left_account.display_info()}")
            print("VS")
            print(f"Compare B: {self.right_account.display_info()}")

            # Take a guess
            choice = self.user_input()
            winner = self.comparison(self.left_account, self.right_account)
            user_chosen_object = self.left_account if choice == 'A' else self.right_account

            if user_chosen_object == winner:
                self.score += 1
                print(f"Correct! Current Score: {self.score}")

                self.left_account = winner

                new_profile = random.choice(self.profiles)

                while new_profile == self.left_account:
                    new_profile = random.choice(self.profiles)

                self.right_account = new_profile
            else:
                print(f"Sorry, that's wrong. Final score: {self.score}")
                game_should_continue = False


if __name__ == "__main__":
    game = Game()
    game.Play()