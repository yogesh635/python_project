import random
subject = [
    "sharukh khan",
    "virat kohli",
    " A group of meditating squirrels",
    "🤖 A robot barista with a caffeine addiction",
    "🎩 A time-traveling goat in a top hat"]


actions = ["lanches","cancels",
        "📚 accidentally unlocked the secrets of the universe while trying to crack open a walnut",
        "🎨 was caught tagging murals of its favorite mangoes on city walls",
        "☕ staged a protest demanding triple espresso breaks and a raise in Bitcoin",
        "🐘 An elephant with a paintbrush"]



places_or_things = [
    "at red fort",
    "in mumbai places",
    "🌳 in a secluded yoga retreat in Himachal Pradesh",
    "🏙️ outside a trendy café in Bangalore",
    "🏞️ throughout the streets of Jaipur"
]

while True:
    subject = random.choice(subject)
    actions = random.choice(actions)
    places_or_things = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {actions} {places_or_things}"
    print("\n" + headline)

    user_input = input("\n Do you want to another headline? (yes/no)" ).strip()

    if user_input == "no":
        break

    print("\n thank  for using the fake news headline generator")    