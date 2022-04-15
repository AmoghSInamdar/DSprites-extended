# DSprites-extended
An extension of the Deepmind dSprites Dataset

This dataset extends the dSprites dataset of synthetic objects varying along set attributes, originally [here](https://github.com/deepmind/dsprites-dataset).

## Differences with dSprite

- This code produces RGB (3-channel) images, varying along the same attributes as dSprites. 
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
