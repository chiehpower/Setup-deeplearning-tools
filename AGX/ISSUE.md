# Install OpenCV

```
$ pip3 install opencv-python opencv-python-headless
Collecting opencv-python
  Using cached https://files.pythonhosted.org/packages/bb/08/9dbc183a3ac6baa95fabf749ddb531bd26256edfff5b6c2195eca26258e9/opencv-python-4.5.1.48.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-build-lj14vll6/opencv-python/setup.py", line 10, in <module>
        import skbuild
    ModuleNotFoundError: No module named 'skbuild'
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-lj14vll6/opencv-python/
```
No `skbuild` then trying to install this module, but it cannot find.
```
$ pip3 install skbuild
Collecting skbuild
Exception:
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/usr/lib/python3/dist-packages/pip/commands/install.py", line 353, in run
    wb.build(autobuilding=True)
  File "/usr/lib/python3/dist-packages/pip/wheel.py", line 749, in build
    self.requirement_set.prepare_files(self.finder)
  File "/usr/lib/python3/dist-packages/pip/req/req_set.py", line 380, in prepare_files
    ignore_dependencies=self.ignore_dependencies))
  File "/usr/lib/python3/dist-packages/pip/req/req_set.py", line 554, in _prepare_file
    require_hashes
  File "/usr/lib/python3/dist-packages/pip/req/req_install.py", line 278, in populate_link
    self.link = finder.find_requirement(self, upgrade)
  File "/usr/lib/python3/dist-packages/pip/index.py", line 465, in find_requirement
    all_candidates = self.find_all_candidates(req.name)
  File "/usr/lib/python3/dist-packages/pip/index.py", line 423, in find_all_candidates
    for page in self._get_pages(url_locations, project_name):
  File "/usr/lib/python3/dist-packages/pip/index.py", line 568, in _get_pages
    page = self._get_page(location)
  File "/usr/lib/python3/dist-packages/pip/index.py", line 683, in _get_page
    return HTMLPage.get_page(link, session=self.session)
  File "/usr/lib/python3/dist-packages/pip/index.py", line 795, in get_page
    resp.raise_for_status()
  File "/usr/share/python-wheels/requests-2.18.4-py2.py3-none-any.whl/requests/models.py", line 935, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://pypi.org/simple/skbuild/
```

Hence, we tried to upgrade the `pip` tool.
```
$ python3 -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/fe/ef/60d7ba03b5c442309ef42e7d69959f73aacccd0d86008362a681c4698e83/pip-21.0.1-py3-none-any.whl (1.5MB)
    100% |################################| 1.5MB 705kB/s 
Installing collected packages: pip
  Found existing installation: pip 9.0.1
    Not uninstalling pip at /usr/lib/python3/dist-packages, outside environment /usr
Successfully installed pip-21.0.1
```
Then tried again. But it cannot find.
```
$ pip3 install skbuild
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
ERROR: Could not find a version that satisfies the requirement skbuild
ERROR: No matching distribution found for skbuild
```
Hence, we changed to inst`.
```
$ pip3 install scikit-build
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Collecting scikit-build
  Downloading scikit_build-0.11.1-py2.py3-none-any.whl (72 kB)
     |################################| 72 kB 537 kB/s 
Requirement already satisfied: wheel>=0.29.0 in /usr/local/lib/python3.6/dist-packages (from scikit-build) (0.35.1)
Requirement already satisfied: packaging in /usr/local/lib/python3.6/dist-packages (from scikit-build) (20.4)
Collecting distro
  Downloading distro-1.5.0-py2.py3-none-any.whl (18 kB)
Requirement already satisfied: setuptools>=28.0.0 in /usr/local/lib/python3.6/dist-packages (from scikit-build) (50.3.2)
Requirement already satisfied: pyparsing>=2.0.2 in /usr/lib/python3/dist-packages (from packaging->scikit-build) (2.2.0)
Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from packaging->scikit-build) (1.15.0)
Installing collected packages: distro, scikit-build
Successfully installed distro-1.5.0 scikit-build-0.11.1
```
Installed again:
```
$ pip3 install opencv-python==4.3.0.38 
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Collecting opencv-python==4.3.0.38
  Using cached opencv-python-4.3.0.38.tar.gz (88.0 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
```
Done.

---
# Illegal instruction (core dumped) because of VERSION

When we imported the numpy, it encountered the `Illegal instruction (core dumped)` issue. 
```
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
`Illegal instruction (core dumped)`
```

Check the version, the numpy version is `1.19.5` which this one is quite new. 
Hence, we uninstall it, and install `1.16.0` version again.
```
python3 -m pip uninstall numpy && python3 -m pip install numpy==1.16.0
```
Test:
```
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> exit()
```