# Signac workshop

Corwin Kerr, Brandon Butler, Kelly Wang, Bradley Dice, Sharon Glotzer

special thanks: Ignacio Blanco Varela for early feedback.

## Goals
* Introduce new users to the **signac** framework.


## Assumed background
* Basic familiarity with Python
* Basic familiarity with Jupyter notebooks
* Enjoyment of cat videos


## Contents
* `/1-intro/`, introduces data management with signac
  * `Signac-Example-Pi.ipynb` - introduce data management with signac.
  * `project.py` - introduces a basic workflow
* `/2-cats/`, get started adapting an existing project and workflow by making cat gifs!
  * `Cats.ipynb`, demo of the few steps to follow
  * `init.py`, to make jobs with different ffmpeg settings
  * `project.py`, contains the workflow


# Launching

## To run online
[Open this example in MyBinder](https://mybinder.org/v2/gh/glotzerlab/signac-workshop/HEAD)

* Allow ~5 minutes to build the environment.

* Note that the MyBinder will time out after 10ish minutes --> If it happens, choose `Run --> Run all above selected cell`


## To run locally

1. Create an environment containing signac, signac-flow, signac-dashboard, h5py, numpy, matplotlib, pandas, jupyterlab using your favorite package manager.
You'll need `ffmpeg` for the second part.

If you use conda:

```
conda create --name signac-tutorial python=3.8 signac signac-flow signac-dashboard h5py numpy matplotlib pandas jupyterlab

git clone https://github.com/glotzerlab/signac-workshop
cd signac-workshop
```

2. Launch Juptyer with `jupyter lab` and open the notebook file.
