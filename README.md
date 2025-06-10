C:\Users\Phillip.Donley\PDF_RoundUp>python pdf_roundup.py
Exception in thread Thread-1 (run_process):
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\Phillip.Donley\PDF_RoundUp\pdf_roundup.py", line 138, in run_process
    api_key = self.get_api_key()
              ^^^^^^^^^^^^^^^^^^
  File "C:\Users\Phillip.Donley\PDF_RoundUp\pdf_roundup.py", line 220, in get_api_key
    key = tk.simpledialog.askstring("API Key", "Enter your PDF API Key:")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 411, in askstring
    d = _QueryString(title, prompt, **kw)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 388, in __init__
    _QueryDialog.__init__(self, *args, **kw)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 283, in __init__
    Dialog.__init__(self, parent, title)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 143, in __init__
    self.wait_visibility()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 752, in wait_visibility
    self.tk.call('tkwait', 'visibility', window._w)
_tkinter.TclError: window ".!_querystring" was deleted before its visibility changed
Exception in thread Thread-2 (run_process):
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\Phillip.Donley\PDF_RoundUp\pdf_roundup.py", line 138, in run_process
    api_key = self.get_api_key()
              ^^^^^^^^^^^^^^^^^^
  File "C:\Users\Phillip.Donley\PDF_RoundUp\pdf_roundup.py", line 220, in get_api_key
    key = tk.simpledialog.askstring("API Key", "Enter your PDF API Key:")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 411, in askstring
    d = _QueryString(title, prompt, **kw)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 388, in __init__
    _QueryDialog.__init__(self, *args, **kw)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 283, in __init__
    Dialog.__init__(self, parent, title)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 143, in __init__
    self.wait_visibility()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 752, in wait_visibility
    self.tk.call('tkwait', 'visibility', window._w)
_tkinter.TclError: window ".!_querystring2" was deleted before its visibility changed
Exception in thread Thread-3 (run_process):
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 1045, in _bootstrap_inner
    self.run()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 982, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\Phillip.Donley\PDF_RoundUp\pdf_roundup.py", line 138, in run_process
    api_key = self.get_api_key()
              ^^^^^^^^^^^^^^^^^^
  File "C:\Users\Phillip.Donley\PDF_RoundUp\pdf_roundup.py", line 220, in get_api_key
    key = tk.simpledialog.askstring("API Key", "Enter your PDF API Key:")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 411, in askstring
    d = _QueryString(title, prompt, **kw)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 388, in __init__
    _QueryDialog.__init__(self, *args, **kw)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 283, in __init__
    Dialog.__init__(self, parent, title)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\simpledialog.py", line 143, in __init__
    self.wait_visibility()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 752, in wait_visibility
    self.tk.call('tkwait', 'visibility', window._w)
_tkinter.TclError: window ".!_querystring3" was deleted before its visibility changed
