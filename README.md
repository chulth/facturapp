
# Getting started

To get you started quickly, we have created some bootstrapping scripts to make things easier.

In plain language all you need to do is create a virtualenv[^1] and run the bootstrap target with make.

A detailed step by step description is:

```
virtualenv venv
source venv/bin/activate
make bootstrap
make run
```

The development server should have started now. You can visit the API by navigating in a browser to : `http://localhost:8010/api/v1/productdata/`.

---

[^1]:
Virtualenv is a python utility to make development simple.

A guide on how to install virtualenv for Linux, Mac and Windows is available here (no need to do the django part):
http://pythoncentral.io/how-to-install-python-django-windows-mac-linux/

Disclaimer: this instructions were tested using a linux OS, for windows we suggest that you install bash for windows: https://itsfoss.com/install-bash-on-windows/

We used python 3.8 for developing and testing this challenge.
