import signac

def grid(gridspec):
    """Yields the Cartesian product of a `dict` of iterables.

    The input ``gridspec`` is a dictionary whose keys correspond to
    parameter names. Each key is associated with an iterable of the
    values that parameter could take on. The result is a sequence of
    dictionaries where each dictionary has one of the unique combinations
    of the parameter values.

    """
    for values in itertools.product(*gridspec.values()):
        yield dict(zip(gridspec.keys(), values))


project = signac.init_project("cats")

for input_file in ['cat1.mp4', 'cat2.mp4','cat3.3gp']:
    job = project.open_job({"input_file": input_file,
                            "fps": 10,
                            "scale": "100:-1"})
job.init()


# for statepoint in grid():
#     job = project.open_job(statepoint)
#     job.init()
