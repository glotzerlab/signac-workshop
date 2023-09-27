# Signac workshop at CECAM

Corwin Kerr, Brandon Butler


**Goals**
* Introduce new users to the **signac** framework in ~1 hour.
* Allow database developers to explore how **signac** handles metadata.

**Assumed background**
* Basic familiarity with Python
* Basic familiarity with Jupyter notebooks



# Launching

## To run online
[Open this example in MyBinder](https://mybinder.org/v2/gh/glotzerlab/signac-workshop/HEAD)

* Allow ~5 minutes to build the environment.

* Note that the MyBinder will time out after about 10 minutes --> If it happens, choose `Run --> Run all above selected cell`


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


# Tutorial Outline
Part 1:
1. Explore a non-signac project in a jupyter notebook.
2. Import the non-signac project into signac.
3. Work with old workflow code in a Jupyter notebook.
4. Convert Jupyter code into `FlowProject` operations in the template `project-1.py` script.

Part 2:
1. Build up a project from scratch.
2. Build operations in a notebook.
3. Move operations to a `project.py` file.
   
    


