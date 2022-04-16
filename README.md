# DSprites-extended
An extension of the Deepmind dSprites Dataset

This dataset extends the [dSprites](https://github.com/deepmind/dsprites-dataset) dataset of RGB images of synthetic objects varying along a set of attributes. In this Python implementation, shapes are generated using [pillow](https://pillow.readthedocs.io/en/stable/index.html) and saved as a compressed [numpy](https://numpy.org/) .npz archive.

## Differences with dSprite

- This code produces RGB (3-channel) images (as opposed to binary), varying along the same attributes as dSprites. 
- Latents values are stored as object arrays with their true values (not float64 encoded arrays).
- Metadata is currently absent.
- Indexing will differ slightly, but images are still in order of the latents (top to bottom as described below).

## Latent Variables

- "color": \["white", "red", "blue", "green"],
- "shape": \["ellipse", "square", "triangle"],
- "scale": 6 values in \[0.5, 1],
- "rotate": 20 values in \[0, 360),
- "xpos": 16 values in \[0, 1],
- "ypos": 16 values in \[0, 1]

## Note to users

Since pillow applies most transforms while the shapes are being rendered, this code does not provide a convenient interface for extensions. To extend the dataset to include more attributes, you will likely need to modify the code for the generation of each shape.
