# project.py

import flow
import numpy as np
import matplotlib.pyplot as plt


class PiProject(flow.FlowProject):
    pass


@PiProject.label
def points_generated(job):
    return "points" in job.data


@PiProject.operation
@PiProject.post(points_generated) # the name of the label function
def scatter_square(job):
    # copy our code here
    pass


@PiProject.operation
@PiProject.pre.after(scatter_square)
# use the 'truthiness' of dictionaries in Python:
@PiProject.post.true('pi_estimated')
def calculate_pi(job):
    # copy our code here
    pass


@PiProject.operation
@PiProject.pre.after(calculate_pi)
@PiProject.post.isfile('preview.png')
def render_image(job):
    # copy our code here
    pass


if __name__ == '__main__':
    PiProject().main()
