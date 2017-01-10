from . import swi

import pytry
import pytry.cmdline

import mimetypes
import os
import pkgutil


class Explorer(swi.SimpleWebInterface):
    def swi_static(self, *dirs):
        fn = os.path.join(dirs)
        mimetype, encoding = mimetypes.guess_type(fn)
        data = pkgutil.get_data('pytry_explorer', fn)
        return data, mimetype

    def swi(self):
        template = pkgutil.get_data('pytry_explorer', 'templates/index.html')

        files = []
        for f in os.listdir('.'):
            files.append('<li><a href="view?file=%s">%s</a></li>' % (f, f))
        files = '\n'.join(files)

        return template % dict(files=files)

    def swi_view(self, file):
        template = pkgutil.get_data('pytry_explorer', 'templates/view.html')

        trial = pytry.cmdline.get_trial_class(file)()

        classname = trial.__class__.__name__
        params = []
        for k, desc in trial.param_descriptions.items():
            if k not in trial.system_params:
                default = trial.param_defaults[k]
                p = '<li>%s=%r  (%s)</li>' % (k, default, desc)
                params.append(p)
        params = '\n'.join(params)

        return template % locals()

def run():
    Explorer.start(port=8080, browser=True)





