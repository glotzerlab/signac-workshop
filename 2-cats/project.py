import flow
import signac

project = signac.get_project()

class GifProject(flow.FlowProject):
    pass


@GifProject.operation
@GifProject.post.isfile("cat.gif")
@flow.cmd
def convert(job):
    return f'ffmpeg -i {project.fn(job.sp.input_file)} -vf "fps = {job.sp.fps},scale = {job.sp.scale}" {job.fn("cat.gif")}'


if __name__ == '__main__':
    GifProject().main()
    
    
