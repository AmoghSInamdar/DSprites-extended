"""
Author: Amogh Inamdar
Creation Date: 15 April 2022
"""

import itertools
import os
from PIL import Image, ImageDraw
import numpy as np


transform_ranges = {
    "color": ["white", "red", "blue", "green"],
    "shape": ["ellipse", "square", "triangle"],
    "scale": np.linspace(0.5, 1., num=6),
    "rotate": list(map(int, list(np.linspace(0, 360, 20, endpoint=False)))),
    "xpos": np.linspace(0., 1., 16),
    "ypos": np.linspace(0., 1., 16)
}


transform_idxs = {k: {l: i for i, l in enumerate(v)} for k, v in transform_ranges.items()}


def create_shape(image_size, base_len, params):
    img = Image.new(mode="RGB", size=image_size, color="black")
    base_len *= params["scale"]
    border = base_len // 2   # 0.55*base_size border accommodates 1.414*base_size rotation change
    vary_len = (image_size[0]-2*base_len, image_size[1]-2*base_len)  # extra base_len to allow for object size
    x_start, y_start = border + (params["xpos"] * vary_len[0]), border + (params["ypos"] * vary_len[1])
    draw = ImageDraw.Draw(img)
    if params["shape"] == "ellipse":
        newimg = Image.new(mode="RGB", size=image_size, color="black")
        draw.ellipse([x_start, y_start, x_start+base_len, y_start+(base_len//2)], fill=params["color"])
        img = img.rotate(params["rotate"], center=(x_start+base_len//2, y_start+base_len//4), fillcolor=0,
                         resample=Image.Resampling.BICUBIC)
        newimg.paste(img, (0, 0))
        return newimg
    elif params["shape"] == "square":
        draw.regular_polygon([x_start+base_len//2, y_start+base_len//2, base_len//2], n_sides=4, fill=params["color"],
                             rotation=params["rotate"])
    elif params["shape"] == "triangle":
        draw.regular_polygon([x_start+base_len//2, y_start+base_len//2, base_len//2], n_sides=3, fill=params["color"],
                             rotation=params["rotate"])
    return img


def generate_images(image_dir):
    for i, params in enumerate(itertools.product(*(transform_ranges.values()))):
        params = {k: params[i] for i, k in enumerate(transform_ranges.keys())}
        img = create_shape((64, 64), 24, params)
        img.save(os.path.join(image_dir, f"{i}.png"))


def create_dsprites_npz(image_size=(64, 64), base_len=24):
    param_code = "".join([k[:2]+str(len(v)) for k, v in transform_ranges.items()])
    save_file = f"dsprites_ndarray_{param_code}_im{image_size[0]}x{image_size[1]}_bb{base_len}.npz"
    save_params = {
        "imgs": [],
        "latents_values": [],
        "latents_classes": [],
        "metadata": np.array([
            {"attributes": transform_ranges},
            {"author": "Amogh Inamdar"}
        ], dtype=object)
    }
    for i, params in enumerate(itertools.product(*(transform_ranges.values()))):
        params = {k: params[i] for i, k in enumerate(transform_ranges.keys())}
        img = np.array(create_shape(image_size, base_len, params), dtype=np.uint8)
        save_params["imgs"].append(img)
        save_params["latents_values"].append(np.array(list(params.values()), dtype="object"))
        param_idxs = [transform_idxs[k][v] for k, v in params.items()]
        save_params["latents_classes"].append(np.array(param_idxs))
    np.savez_compressed(save_file, **{k: np.array(v) for k, v in save_params.items()})


def load_dsprites_npz(savefile):
    data = np.load(savefile, allow_pickle=True)
    return data


if __name__ == "__main__":
    # generate_images("images")
    # create_dsprites_npz()
    load_dsprites_npz("dsprites_ndarray_co4sh3sc6ro20xp16yp16_im64x64_bb24.npz")
