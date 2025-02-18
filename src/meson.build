pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'eraser'

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
            input: 'eraser.in',
           output: 'eraser',
    configuration: conf,
          install: true,
      install_dir: get_option('bindir'),
     install_mode: 'r-xr-xr-x'
)

eraser_sources = [
    '__init__.py',
    'main.py'
]

install_data(eraser_sources, install_dir: moduledir)
