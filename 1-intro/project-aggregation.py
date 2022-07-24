# project.py

import flow
import numpy as np
import matplotlib.pyplot as plt


class PiProject(flow.FlowProject):
    pass


@PiProject.label
def points_generated(job):
    return "points" in job.data


# So we know when to generate the overview plot
@PiProject.label
def all_calculated(*jobs):
    return all(job.doc.get("pi_estimate", False) for job in jobs)


@PiProject.operation
@PiProject.post(points_generated) # the name of the label function
def scatter_square(job):
    """Generate job.sp.num_points number
    of xy pairs of points within the [0,1] square 
    and save it to the job data store.
    
    Optionally, initialize the random number
    generator with the seed job.sp.seed"""
    num_points = job.sp.num_points
    
    # Use the seed if our job has one
    seed = job.sp.get("seed", None)
    # We'll add seed to our state point later
    rng = np.random.default_rng(seed)
    
    # defaults to within [0,1] in each dimension
    points = rng.random(size=(int(num_points), 2))
    job.data['points'] = points



@PiProject.operation
@PiProject.pre.after(scatter_square)
# use the 'truthiness' of dictionaries in Python:
@PiProject.post.true('pi_estimate')
def calculate_pi(job):
    """Estimate pi by counting points within the unit circle.
    Points within the unit circle are saved in the job data store. 
    Set the job.doc.pi_estimate to the result.
    
    Input
    =====
    job, a signac job object"""
    with job.data:
        points = job.data.points[:]
        # within the unit circle
        selected = np.linalg.norm(points, axis=1) < 1
        job.data['selected'] = points[selected]
    count = sum(selected)
    num_points = job.sp.num_points
    job.doc.pi_estimate = float(4 * count/num_points)


@PiProject.operation
@PiProject.pre.after(calculate_pi)
@PiProject.post.isfile('preview.png')
def render_image(job):
    f,a = plt.subplots()
    with job.data:
        points = job.data.points[:]
        selected = job.data.selected[:]
    a.plot(*points.T, '.b')
    a.plot(*selected.T, 'or')
    a.set_aspect('equal')
    plt.setp(a,
             title = "Visualizing Pi Estimate",
             )
    plt.savefig(job.fn("preview.png"), format='png', dpi=150)
    plt.close(f)


@PiProject.operation
@flow.aggregator(aggregator_function = None, sort_by="num_points")
@PiProject.pre(all_calculated)
@PiProject.post(lambda *jobs: jobs[0]._project.isfile('convergence.png'))
def convergence_plot(*jobs):
    # get data from each job in the aggregate
    data = [job.doc.pi_estimate for job in jobs]
    num_points = [job.sp.num_points for job in jobs]
    
    # get the project class so we know where to save our plot
    project = jobs[0]._project
    
    # make the plot
    f,a = plt.subplots()
    a.plot(num_points, data, 'o', label="Estimates")
    plt.setp(a,
             xlim = [0,50],
             xlabel = 'Number of points scattered',
             ylabel = 'Estimate of pi',
             title = "Convergence of Estimate Towards the True Value of Pi",
             )
    a.plot([0,1000],[np.pi, np.pi], label="Pi")
    plt.savefig(project.fn("convergence.png"), dpi=200)
    plt.close()



if __name__ == '__main__':
    PiProject().main()
