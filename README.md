vauxoo_applicant
================

Este repositorio servirá para que los aspirantes a colaborar con vauxoo suban aquí el resultado de su evaluación técnica, por medio de pull request (PR)

Hacer un fork de este repositorio, con tu usuario y empezar a resolver los problemas de la prueba técnica.

[Prueba técnica](https://docs.google.com/forms/d/1yK7JNVM7kUchQrfU5hMEs3pqurvvR92VeXb-hUR7OP8/viewform?usp=send_form)

NOTE: Your PR will test it by travis using python unittest, flake8 and pylint.

You can install with next commands:

```bash
# apt-get install pylint python-flake8
```
You can execute test locally with next commands:
```bash
cd vauxoo-applicant/
flake8 . --exclude=__init__.py && echo $?
pylint --rcfile=.pylint.cfg *.py && echo $?
python .all_unittest.py && echo $?
```
If exit with 0 (zero) each command your code is very good!
