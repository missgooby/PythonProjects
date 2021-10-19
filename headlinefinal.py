# Tahlil Darwish
# Sunshine Calderon
# Devin Hall
import csv
import json
import random

# set up constants
OBJECT_PRONOUNS = ['Her', 'Him', 'Them', 'It']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their', "It's"]
PERSONAL_PRONOUNS = ['She', 'He', 'They', 'It']
STATES = ['California', 'Texas', 'Oregon', 'Oklahoma', 'Hawaii', 'Florida', 'New York', 'Wisconsin', 'Washington',
          'Washington D.C.', 'South Korea', 'North Korea', 'China', 'Germany', 'Australia', 'Russia']
NOUNS = ['Vaccine', 'Donald Trump', 'CDC', 'Joe Biden', 'TikTok', 'Year Up', 'Devin Hall', 'Professor Fly', 'Man',
         'Woman', 'James Bond', 'Jeff Bezos', 'Grimes', 'Elon Musk', 'Clown', 'Scranton Killer', 'Axolotl',
         'Baby Yoda', 'Plastic Bag', 'Global Warming', 'Worm', 'Shrimp', 'Kim Kardashian', 'Kylie Jenner', 'Booty',
         'Weight Loss', 'Coffee', "Egg", "Skinny Tea"]
PLACES = ['Starbucks', 'Your Backyard', "Dunkin' Donuts", "Madison Square Garden", "Outer Space", "Clinic", "Insane Asylum",
          "Lady Gaga's House", "Bunker", "North Pole", "Haunted House", "White House", "David Dobrik's House",
          "Zoo", "DCCCD", "Air plane", "Airport", "YouTube", "facebook Headquarters"]
WHEN = ["Soon", "7 Years From Now", "Later Tonight", "RIGHT NOW", "Later This Month", "One Day", "In A Lil Bit"]


# Following are the headline prompts:

class Headlines:

    def generateAreKardashianKillingHeadline(self):
        noun = random.choice(NOUNS)
        return 'Are The Kardashians Killing the {} Industry?'.format(noun)

    def generateWhatYouDontKNowHeadline(self):
        noun = random.choice(NOUNS)
        noun2 = random.choice(NOUNS) + 's'
        when = random.choice(WHEN)
        return 'Living Without This {} could have {} Hunt You Down {}!'.format(noun, noun2, when)

    def generateTechCompaniesHateHerHeadline(self):
        pronoun = random.choice(OBJECT_PRONOUNS)
        state = random.choice(STATES)
        noun1 = random.choice(NOUNS)
        noun2 = random.choice(NOUNS)
        return 'Tech Companies Hate {}! See How This {} {} Made a Cheaper {}'.format(pronoun, state, noun1, noun2)

    def generateYouWontBelieveHeadline(self):
        state = random.choice(STATES)
        noun = random.choice(NOUNS)
        pronoun = random.choice(POSSESSIVE_PRONOUNS)
        place = random.choice(PLACES)
        return "You Won't Believe What This {} {} Cooked in {} {}".format(state, noun, pronoun, place)

    def generateDontWantYouToKnowHeadline(self):
        pluralNoun1 = random.choice(NOUNS) + 's'
        pluralNoun2 = random.choice(NOUNS) + 's'
        return "What {} Don't Want You To Know About {}".format(pluralNoun1, pluralNoun2)

    def generateGiftIdeaHeadline(self):
        number = random.randint(7, 15)
        noun = random.choice(NOUNS)
        state = random.choice(STATES)
        return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)

    def generateReasonsWhyHeadline(self):
        number1 = random.randint(1, 15)
        pluralNoun = random.choice(NOUNS) + 's'
        # number2 should be no longer than number1:
        number2 = random.randint(1, number1)
        return '{} Reasons Why {} Are Slept On(Number {} Will SHOCK YOU!)'.format(number1, pluralNoun, number2)

    def generateJobAutomatedHeadline(self):
        state = random.choice(STATES)
        noun = random.choice(NOUNS)

        i = random.randint(0, 2)
        pronoun1 = POSSESSIVE_PRONOUNS[i]
        pronoun2 = PERSONAL_PRONOUNS[i]
        if pronoun1 == 'Their':
            return "This {} {} Didn't Think Robots Would Take {} Job. {} Were Wrong.".format(state, noun, pronoun1, pronoun2)
        else:
            return "This {} {} Didn't Think Robots Would Take {} Job. {} Was Wrong.".format(state, noun, pronoun1, pronoun2)


def main():
    users = {}
    try:
        with open('users.json') as jsonfile:
            users = json.load(jsonfile)
    except FileNotFoundError:
        pass
    user = input('Enter your name: ')
    if user in users:
        last = users[user]
        print('Welcome back,', user + '. Last time you requested', last, 'headlines.')
    headline = Headlines()
    print('The Clickbait Headline Machine')
    print('By Sunshine Calderon, Tahlil Darwish, Devin Hall')
    print()
    print("Our program brings viewer traffic to YOUR content!")
    while True:
        print('Enter the amount of headlines desired: ')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a valid number. ')
        else:
            numberOfHeadlines = int(response)
            break
    users[user] = numberOfHeadlines
    with open('users.json', 'w') as jsonfile:
        json.dump(users, jsonfile)
    for i in range(numberOfHeadlines):
        clickbaitPrompt = random.randint(1, 8)  # program generates prompt number at random
        # Random number assigned to prompt:

        if clickbaitPrompt == 1:
            hl = headline.generateAreKardashianKillingHeadline()
        if clickbaitPrompt == 2:
            hl = headline.generateWhatYouDontKNowHeadline()
        if clickbaitPrompt == 3:
            hl = headline.generateTechCompaniesHateHerHeadline()
        if clickbaitPrompt == 4:
            hl = headline.generateYouWontBelieveHeadline()
        if clickbaitPrompt == 5:
            hl = headline.generateDontWantYouToKnowHeadline()
        if clickbaitPrompt == 6:
            hl = headline.generateGiftIdeaHeadline()
        if clickbaitPrompt == 7:
            hl = headline.generateReasonsWhyHeadline()
        if clickbaitPrompt == 8:
            hl = headline.generateJobAutomatedHeadline()
        print(hl)
    print()

    website = random.choice(['Tender', 'TikTak', 'Twater', 'Yoohoo', 'BMail', 'Finsta', 'Read-it', 'Feetbook',
                             'Snapsnap'])
    when = random.choice(WHEN).lower()
    print("Post these to your", website, when, "or you're fired!")


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
