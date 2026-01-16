import uuid
import json
import time
from utils.config_utils import load_config
from utils.file_utils import load_json
from utils.prompt_utils import load_prompt
from utils.api_utils import send_request, print_response

# -------------------------------------------------------
# LOAD CONFIG
# -------------------------------------------------------
config = load_config()

API_KEY = config["api"]["api_key"]
API_URL = config["api"]["api_url"]

REASONING = config["model"]["reasoning"]
MAX_TOKENS = config["model"]["max_new_tokens"]
TEMPERATURE = config["model"]["temperature"]
REPETITION_PENALTY = config["model"]["repetition_penalty"]

# -------------------------------------------------------
# LOAD PROMPTS
# -------------------------------------------------------
SYSTEM_PROMPT = load_prompt("prompts/system_prompt.txt")
DEVELOPER_PROMPT = load_prompt("prompts/developer_prompt.txt")
USER_PROMPT = load_prompt("prompts/user_prompt.txt")


# -------------------------------------------------------
# BUILD PAYLOAD
# -------------------------------------------------------

question_id = f"q-{uuid.uuid4()}"
payload = {
    "messages": [
        {
            "role": "user",
            "content": USER_PROMPT,
            "system": SYSTEM_PROMPT,
            "developer": DEVELOPER_PROMPT,
            "question_id": question_id
        }
    ],
    "reasoning": REASONING,
    "max_new_tokens": MAX_TOKENS,
    "temperature": TEMPERATURE
    # "repetition_penalty": REPETITION_PENALTY
}

# -------------------------------------------------------
# SEND REQUEST
# -------------------------------------------------------
start_time = time.time()
resp = send_request(API_URL, API_KEY, payload)
end_time = time.time()
print_response(resp, (end_time - start_time))


