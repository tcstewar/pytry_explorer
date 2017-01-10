from . import swi

import pytry

import mimetypes
import os
import pkgutil

def get_trial(filename):
    with open(filename) as f:
        code = f.read()
    objs = dict(__file__=filename, __name__='__pytry__')
    compiled = compile(code, filename, 'exec')
    exec(compiled, objs)

    trials = []
    for x in objs.values():
        if isinstance(x, type):
            if issubclass(x, pytry.Trial):
                trials.append(x)
    if len(trials) == 0:
        print('Error: no pytry.Trial class found in %s' % filename)
    elif len(trials) > 1:
        print('Error: more than one pytry.Trial class found')
    return trials[0]

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

        trial = get_trial(file)()

        classname = trial.__class__.__name__
        params = []
        for k, desc in trial.param_descriptions.items():
            default = trial.param_defaults[k]
            p = '<li>%s=%r  (%s)</li>' % (k, default, desc)
            params.append(p)
        params = '\n'.join(params)


        return template % locals()

def run():
    Explorer.start(port=8080, browser=True)





