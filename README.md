# Caspal

A simple interpreter for a subset of Pascal written in Python, purely
for education and pleasure.

## Installing Dependencies

```
$ pip install -r requirements.txt
```

If you use Emacs with Elpy, add the following packages as well:
```
autopep8==1.2.4
flake8==2.5.4
importmagic==0.1.7
jedi==0.9.0
mccabe==0.4.0
pep8==1.7.0
pyflakes==1.0.0
yapf==0.8.2
```

## Setup

```
$ chmod +x cpl
```

## Running

Start the REPL by running:
```
$ ./cpl
```

## Testing

Run tests using nose:

```
$ env/bin/nosetests
```

## License

Caspal is licensed under GNU General Public License v3 (GPL-3). Refer the
LICENSE file for further details.
