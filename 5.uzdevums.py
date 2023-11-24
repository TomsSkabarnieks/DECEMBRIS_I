import datetime

def laiks():
    stunda = datetime.datetime.now().hour
    if 5 <= stunda < 12:
        return "Labrīt"
    elif 12 <= stunda < 18:
        return "Labdien"
    elif 18 <= stunda < 24:
        return "Labvakar"
     else:
          return "Arlabunakti"
print(laiks())