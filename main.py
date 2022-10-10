import os
import random
import uuid

BASE_DIR = "themes"

def generate_theme():
    theme = f"""
    {{
      "manifest_version": 3,
      "version": "2.6",
      "name": "camo theme",
      "theme": {{
        "images" : {{
        }},
        "colors" : {{
          "frame" : [{str(random.randint(0, 255))}, {str(random.randint(0, 255))}, {str(random.randint(0, 255))}],
          "toolbar" : [{str(random.randint(0, 255))}, {str(random.randint(0, 255))}, {str(random.randint(0, 255))}],
          "ntp_text" : [{str(random.randint(0, 255))}, {str(random.randint(0, 255))}, {str(random.randint(0, 255))}],
          "ntp_link" : [{str(random.randint(0, 255))},{str(random.randint(0, 255))},{str(random.randint(0, 255))}],
          "ntp_section" : [{str(random.randint(0, 255))}, {str(random.randint(0, 255))},{str(random.randint(0, 255))}],
          "button_background" : [{str(random.randint(0, 255))}, {str(random.randint(0, 255))}, {str(random.randint(0, 255))}]
        }},
        "tints" : {{
          "buttons" : [{str(random.randint(0, 255))}, {str(random.randint(0, 255))}, {str(random.randint(0, 255))}]
        }},
        "properties" : {{
          "ntp_background_alignment" : "bottom"
        }}
      }}
    }}
    """

    return theme

for th in range(5):
    name = f"theme_{uuid.uuid4()}"
    os.mkdir(f"{BASE_DIR}/{name}")

    with open(f"{BASE_DIR}/{name}/manifest.json","w") as theme_file:
        theme_file.write(generate_theme())
