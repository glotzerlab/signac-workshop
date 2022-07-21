import flow
import signac

project = signac.get_project()

class GifProject(flow.FlowProject):
    pass

def get_input(file):
    return project.fn(f'cats/{file}')


@GifProject.operation
@GifProject.post.isfile("cat.gif")
@flow.cmd
def make_gif(job):
    return f'ffmpeg -i {get_input(job.sp.input_file)} -vf "fps = {job.sp.fps},scale = {job.sp.scale}" {job.fn("cat.gif")}'


@GifProject.operation
@GifProject.post.isfile("palette.png")
@flow.cmd
def preview_palette(job):
    return f'ffmpeg -i {get_input(job.sp.input_file)} -vf palettegen {job.fn("palette.png")}'


if __name__ == '__main__':
    GifProject().main()
    
    
