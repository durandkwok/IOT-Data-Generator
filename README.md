# IOT-Data-Generator

Python script to generate IOT sample data.

Creates sample data of the following:
sensor101 is to measuretemp.
sensor102 measures pressure
sensor103 measures level
sensor104 measures voltage

sensrec['sendatetime'] = jmsg.get("timestamp")+jmsg.get("millis")
sensrec['timezone'] = jmsg.get("timezone")
sensrec['sensor'] = jmsg.get("sensor")
sensrec['type'] = jmsg.get("senstype")
sensrec['metric'] = jmsg.get("metric")

Output of the script to stdout
currentTemp', 'currentPresure', 'currentLevel', 'currentVoltage

Example of output:
{"sendatetime": "2020-01-15T14:29:56235", "timezone": "-0500", "sensor": "sensor102", "type": "currentPresure", "metric": 1000.0}
{"sendatetime": "2020-01-15T14:29:56236", "timezone": "-0500", "sensor": "sensor103", "type": "currentLevel", "metric": 10.08414709848079}
{"sendatetime": "2020-01-15T14:29:56238", "timezone": "-0500", "sensor": "sensor102", "type": "currentPresure", "metric": 1009.0929742682569}
{"sendatetime": "2020-01-15T14:29:56239", "timezone": "-0500", "sensor": "sensor104", "type": "currentVoltage", "metric": 220.2116800120898}
{"sendatetime": "2020-01-15T14:29:56240", "timezone": "-0500", "sensor": "sensor103", "type": "currentLevel", "metric": 10.008466848949997}
{"sendatetime": "2020-01-15T14:29:56241", "timezone": "-0500", "sensor": "sensor104", "type": "currentVoltage", "metric": 218.7732936000951}
{"sendatetime": "2020-01-15T14:29:56242", "timezone": "-0500", "sensor": "sensor101", "type": "currentTemp", "metric": 31.720584501801074}
{"sendatetime": "2020-01-15T14:29:56244", "timezone": "-0500", "sensor": "sensor102", "type": "currentPresure", "metric": 1015.6628402554447}
{"sendatetime": "2020-01-15T14:29:56245", "timezone": "-0500", "sensor": "sensor101", "type": "currentTemp", "metric": 32.70994274842445}
