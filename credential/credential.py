import json
import subprocess
import sys

tool_input = {
    "message": "Please enter your Hubspot private app token.",
    "fields": "token",
}
command = ["gptscript", "--quiet=true", "--disable-cache", "sys.prompt", json.dumps(tool_input)]
result = subprocess.run(command, stdin=None, stdout=subprocess.PIPE, text=True)
if result.returncode != 0:
    print("Failed to run sys.prompt.", file=sys.stderr)
    sys.exit(1)

try:
    resp = json.loads(result.stdout.strip())
    token = resp["token"].lower()

except json.JSONDecodeError:
    print("Failed to decode JSON.", file=sys.stderr)
    sys.exit(1)

output = {
    "env": {
        "HUBSPOT_ACCESS_TOKEN": token,
    }
}

print(json.dumps(output))
