# Washington Math Organization (WAMO) Website
We are a dedicated group of students working to foster a love for mathematics and expand mathematical opportunities throughout Washington State and beyond. Our mission is to increase engagement with competitive math and create a community where students can grow and excel.


## Project Internals
This project is written using plain HTML, CSS, and JS. To prevent code duplication, Flask/Jinja is used. The code is translated into a static website through the [Frozen Flask](https://frozen-flask.readthedocs.io/en/latest/) library.

* Pages can be found in the `templates` folder.
* New pages must also be added to
* Due to how Flask works, all static files must go in the `static` folder

## Turning this code into an actual website
This website was not designed to be run by anyone other than us, so we don't advise trying to host htis yourself. However, here are installation instructions

> Requirements: Python 3.8+, Pip

```py
# Clone the repo from GitHub and enter into the directory
git clone https://github.com/actiniumn404/WAMO.git
cd WAMO

# Optional: create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Convert everything into static HTML
python3 main.py
```

The static website will then be generated in a file named `build`.

## TODO
- [ ] Contact/Join us page
- [ ] Add instagram to page
- [x] Add upcoming contests
- [ ] Change favicon to actually display by being 48n x 48n (n is an integer)