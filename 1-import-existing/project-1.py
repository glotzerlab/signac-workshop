#!/usr/bin/env python3
"""Define the operations for the 2D Gaussian Random Walk project."""

import flow
import matplotlib.pyplot as plt
import numpy as np


class RandomWalkProject(flow.FlowProject):
    """Create a workflow for simulating 2D Gaussian random walks."""
    pass



# These labels help determine the status of the project:

@RandomWalkProject.label
def simulated(job):
    """Return whether the job simulated."""
    return "positions" in job.data

def all_simulated(*jobs):
    """Return whether all jobs simulated."""
    return all(simulated(job) for job in jobs)




# Operations on individual jobs

@RandomWalkProject.post(simulated)
@RandomWalkProject.operation
def simulate(job):
    """Simulate a 2D random walk."""
    # Copy in signacified workflow code and uncomment below:
    #
    #


    #
    # uncomment below:
    # job.data["positions"] = positions
    pass


@RandomWalkProject.pre.after(simulate)
@RandomWalkProject.post(lambda job: "squared_displacement" in job.data)
@RandomWalkProject.operation
def compute_squared_displacement(job):
    """Compute the squared displacement for a random walk."""
    
    #with job.data:
    #    positions = job.data["positions"][:]
    
        # Copy in workflow code and uncomment the above
    pass





# Create aggregator that combines all replicas with a single standard deviation
std_aggregator = flow.aggregator.groupby("standard_deviation", sort_by="replica")

def generate_stores(jobs, store_name):
    """Yield a data store for each job in jobs."""
    for job in jobs:
        with job.data:
            yield job.data[store_name]


@RandomWalkProject.pre(all_simulated)
@RandomWalkProject.pre(lambda *jobs: "squared_displacement" in jobs[0].data)
@RandomWalkProject.post(lambda *jobs: jobs[0].doc.get("msd_analyzed"))
@RandomWalkProject.operation(aggregator=std_aggregator)
def compute_mean_squared_displacement(*jobs):
    """Compute and store the mean squared displacement for all std."""
    msd = np.zeros(jobs[0].doc.run_steps + 1)
    for squared_displacement in generate_stores(jobs, "squared_displacement"):
        msd += squared_displacement
    msd /= len(jobs)
    # Store msd in only first replica (job.sp.replica == 0)
    jobs[0].data["msd"] = msd
    jobs[0].doc.msd_analyzed = True


# This operation happens after computing the msd so it isn't in base.
# Also we use pre as a filter for jobs ensuring this job only ever runs on the zeroth
# replica for a given standard deviation.
@RandomWalkProject.pre.true("msd_analyzed")
@RandomWalkProject.pre(lambda job: job.sp.replica == 0)
@RandomWalkProject.post.isfile("msd.png")
@RandomWalkProject.operation
def plot_mean_squared_displacement(job):
    """Plot the MSD for all standard deviations."""
    with job.data:
        msd = job.data.msd[:]
    fig, ax = plt.subplots()
    ax.plot(msd)
    ax.set_title(f"MSD for standard deviation {job.sp.standard_deviation}")
    ax.set_xlabel("x")
    ax.set_ylabel("MSD")
    # Only save figure to the first replica
    fig.savefig(job.fn("msd.png"))
    plt.close()



if __name__ == "__main__":
    RandomWalkProject().main()
