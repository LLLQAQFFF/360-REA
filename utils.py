import json
import time

from openai import OpenAI


def requestLLM(role_prompt, task):
    time.sleep(3)
    client = OpenAI()
    # time.sleep(5)
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": role_prompt},
            {"role": "user", "content": task}
        ]
    )
    return completion.choices[0].message


def extract_content(text, headings):
    content_dict = {}
    current_heading = None
    for line in text.split('\n'):
        # Check if the line is a heading
        if any(heading in line for heading in headings):
            current_heading = line.split(':')[0].strip()
            content_dict[current_heading] = ""
        elif current_heading:
            # Add the line to the current heading content
            content_dict[current_heading] += line.strip() + "\n"
    return content_dict
