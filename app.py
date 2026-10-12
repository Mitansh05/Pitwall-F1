import fastf1
import logging

fastf1.Cache.enable_cache("setup/cache")

print("\nFastF1 version:", fastf1.__version__ + "\n")

logging.getLogger("fastf1").setLevel(logging.WARNING)

## End of the setup for the app ##

## Main Code Aside From The setup.py File ##

session = fastf1.get_session(2021, "Abu Dhabi", "Race")

print("\nSession:", session.event["EventName"],"\nSession Date:", session.date, "\n")

session.load(laps=False, telemetry=False, weather=False, messages=False)

print(session.results.loc[:, [
    'DriverNumber',
    'Abbreviation',
    'TeamName',
    'Position',
    'Points',
    'Laps'
]].to_string(index=False),"\n")

print("\nFinshed Running\n")