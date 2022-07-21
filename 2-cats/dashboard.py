from signac_dashboard import Dashboard
from signac_dashboard.modules import StatepointList, ImageViewer

class CatDashboard(Dashboard):
    def job_title(self, job):
        return ""


if __name__ == '__main__':
    modules = []
    modules.append(StatepointList())
    modules.append(ImageViewer(context='JobContext',
                               img_globs = ['cat.gif']))
    Cats(modules = modules).main()
                   
    
