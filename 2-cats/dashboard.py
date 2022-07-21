from signac_dashboard import Dashboard
from signac_dashboard.modules import StatepointList, ImageViewer

class CatDashboard(Dashboard):

    def job_title(self, job):
        return f"fps: {job.sp.fps}, scale: {job.sp.scale}"

if __name__ == '__main__':
    modules = []
    modules.append(StatepointList())
    modules.append(ImageViewer(context='JobContext',
                               img_globs = ['cat.gif'],
                               name = "GIF"))
    CatDashboard(modules = modules).main()
                   
    
