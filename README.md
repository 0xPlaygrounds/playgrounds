# playgrounds
Numerical simulation and learning environment for Olympus-style protocols

## Local Development with Docker

To run a local development environment using Docker, follow these steps.

1. `docker run -v $PWD:/usr/local/src -it -p 8050:8050 -w /usr/local/src python:3.9 bash`
2. `pip install -r requirements.txt`
3. `python index.py`

You should now be able to access your local development version of the site at
`http://localhost:8050`

_NOTE: since your local copy of the code is mounted in the container,_
_any changes will be automatically reflected when you reload the page._

## Repo Structure

Since all Olympus-style protocols share mostly the same fundamental mechanics,
we are designing Playgrouds around a core set of common components with a standard,
layout, but with a YAML-formatted configuration

Built in the Dash frame, the Playgrounds application supports customization via:

- templated string values
- function references for injecting custom components in predefined locations

### Configuration Format

Configuration values are stored in the YAML format, which can be loaded
using the standard function `load_config` in `utils.py`, which returns a
dictionary object representing the loaded YAML contents.

Since the config only varies between deployments, this function caches the
loaded config, and thus can be called in each file that requires referencing
values from the configuration without actually re-reading the file from disk.

So in each file that needs to access config values, there should be a snippet like this:

```python
from utils import load_config

config = load_config()
```

Then you can reference config values using standard Python dictionary access syntax:
```python
protocol = config['protocol']
```

### Dash Multipage Application

Since the Playgrounds application contains multiple pages, we leverage Dash's
support for multipage applications.

The "main" app is instantiated with `app.py` and invoked within `index.py`
to create the top-level layout.

Each "subapp" has its layout defined in a separate Python file within the `apps`
folder. Then in the `index.py` file we import the corresponding file and map
it to a specific URL. The corresponding URL must be linked from somewhere within
the app, for instance within the `navbar.py` component to bring users to that
page from the navigation bar.

### Component Library

In order to reduce repetition, keep all code for each component in a single file,
and keep file sizes reasonable, we separate out the layout and callbacks for each
component into files within the `components` folder.

Each component should be generated within a function prefixed with `gen_`
that accepts any necessary arguments.

To include that component on a page, simply import the `gen_` function from
that component file and invoke it within the layout at the desired location.
