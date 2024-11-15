# circular-cv
check for circular import 


## Error Example
```commandline
  File "depth_and_gsam.py", line 9, in <module>
    import cv2
  File "/usr/local/lib/python3.8/dist-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
  File "/usr/local/lib/python3.8/dist-packages/cv2/__init__.py", line 175, in bootstrap
    if __load_extra_py_code_for_module("cv2", submodule, DEBUG):
  File "/usr/local/lib/python3.8/dist-packages/cv2/__init__.py", line 28, in __load_extra_py_code_for_module
    py_module = importlib.import_module(module_name)
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/usr/local/lib/python3.8/dist-packages/cv2/mat_wrapper/__init__.py", line 40, in <module>
    cv._registerMatType(Mat)
AttributeError: partially initialized module 'cv2' has no attribute '_registerMatType' (most likely due to a circular import)

```

#### troubleshooting
```commandline
python3 -m pip uninstall --yes opencv-python-headless opencv-contrib-python opencv-python
python3 -m pip install opencv-python==3.4.18.65

```
