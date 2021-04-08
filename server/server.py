import os
import random
from typing import *

import numpy as np
from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont

from model_utils import generate_img_from_prompt
from data_utils import get_word_list, get_word_info

app = Flask(__name__)


@app.route("/generate_img_from_promt")
def run_generate_img_from_prompt():
    prompt = request.args.get('prompt')

    print("Arguments received:")
    print(f"prompt: {prompt}")

    _ = generate_img_from_prompt(prompt=prompt)

    return jsonify(success=True)


@app.route(
    "/generate_img_from_times",
    methods=[
        "GET",
    ],
)
def generate_img_from_times():
    elapsed_times = request.args.get('elapsedTimes')
    elapsed_time_list = [float(t) for t in elapsed_times.split(",")]
    print("Elapsed Times", elapsed_time_list)

    word_list = get_word_list()

    max_word_idx_list = np.array(elapsed_time_list).argsort()[::-1]

    num_words_prompt = min(3, len(max_word_idx_list))
    max_word_idx_list = max_word_idx_list[:num_words_prompt]

    prompt = ""
    for max_word_idx in max_word_idx_list:
        selected_word = word_list[max_word_idx]

        word_info_dict = get_word_info(word_list[max_word_idx])

        selected_pre = random.choice(
            word_info_dict["pre"]) if random.random() > 0.5 else ""
        selected_post = random.choice(
            word_info_dict["post"]) if random.random() < 0.5 else ""

        prompt += f"{selected_pre} {selected_word} {selected_post} "

    print("PROMTP", prompt)

    _ = generate_img_from_prompt(
        prompt=prompt,
        output_path="public/environments/img/{prompt}.png",
    )

    response = jsonify(
        success=True,
        prompt=prompt,
    )

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route(
    "/generate_environments",
    methods=[
        "GET",
    ],
)
def generate_environments():
    font_path = "server/Montserrat-Regular.ttf"
    try:
        print("Obtaining word list...")
        word_list = get_word_list()

        img_size = (1080, 1080)

        print("Generating image environments...")
        for word_idx, word in enumerate(word_list):
            img = Image.new(
                'RGB',
                img_size,
                color=(256, 256, 256),
            )

            img_draw = ImageDraw.Draw(img, )

            font_size = 100
            font = ImageFont.truetype(
                font_path,
                size=font_size,
            )
            text_w, text_h = img_draw.textsize(
                word,
                font=font,
            )

            img_draw.text(
                ((img_size[0] - text_w) / 2, (img_size[1] - text_h) / 2),
                word,
                fill="black",
                font=font,
            )

            img.save(f'public/environments/img/{word_idx}.png')

        response = jsonify(
            numWords=len(word_list),
            success=True,
        )
        response.headers.add('Access-Control-Allow-Origin', '*')

    except Exception as e:
        response = jsonify(
            success=False,
            error=repr(e),
        )

    return response


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000,
    )
