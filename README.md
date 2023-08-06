# Flight API

Repository with common documents (and GitHub community docs) used in the Project SRC.

## Dependencies

- Python 3.10.12
- FastAPI 0.101.0
- uvicorn 0.23.2
- Environs 9.5.0
- Pydantic 2.1.1
- SQLAlchemy 2.0.19

## Configuration

The Flight API configuration is through operating system environment variables. Therefore the configuration must be done in host or must be passed to the container environment.

The available settings are:

- `HOST`: To indicates if the running version works with mocking data.
- `PORT`: To indicates if the running version is used for testing purposes.
- `VERSION`: Version of the API (service).

If you have questions about how to set environment variables check these links:

- [Environment Variables - Linux](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps)

## Development

### Installing VirtualEnvWrapper

We recommend using a virtual environment created by the **virtualenvwrapper** module. There is a virtual site with English instructions for installation that can be accessed [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html). But you can also follow these steps below for installing the environment:

```shell
sudo python3 -m pip install -U pip             # Update pip
sudo python3 -m pip install virtualenvwrapper  # Install virtualenvwrapper module
```

**Observation**: If you do not have administrator access on the machine remove `sudo` from the beginning of the command and add the flag `--user` to the end of the command.

Now configure your shell to use **virtualenvwrapper** by adding these two lines to your shell initialization file (e.g. `.bashrc`,`.profile`, etc.)

```shell
export WORKON_HOME=\$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

If you want to add a specific project location (will automatically go to the project folder when the virtual environment is activated) just add a third line with the following `export`:

```shell
export PROJECT_HOME=/path/to/project
```

Run the shell startup file for the changes to take effect, for example:

```shell
source ~/.bashrc
```

Now create a virtual environment with the following command (entering the name you want for the environment), in this example I will use the name **flight**:

```shell
mkvirtualenv -p $(which python3) flight
```

To use it:

```shell
workon flight
sudo python3 -m pip install pipenv # Or
sudo apt install pipenv # On Debian based distributions
pipenv install # Will install all of the project dependencies
```

In case you don't have pipenv installed, replace the last command with:

```shell
pip install -r requirements.txt
```

**Observaion**: Again, if necessary, add the flag `--user` to make the pipenv package installation for the local user.

### Local Execution

For local system execution, run the following command in the project root folder (assuming  your _virtualenv_ is already active):

```shell
export PYTHONPATH=$(pwd)
python src/main.py
```

This will run the system on _localhost_ and will be available on the `PORT` port configured for the system. This way you can test new implementations.

An example payload looks like:

```json
{
  "code": "BSB",
  "latitude": "-15.8622",
  "longitude": "-47.9122",
  "name": "Juscelino Kubitschek International Airport",
  "city": "Lago Sul",
  "state": "Distrito Federal",
  "country": "Brazil",
  "woeid": "12511058",
  "tz": "America/Sao_Paulo",
  "phone": "",
  "type": "Airports",
  "email": "",
  "url": "http://www.infraero.gov.br/",
  "runway_length": "10499",
  "elevation": "3473",
  "icao": "SBBR",
  "direct_flights": "32",
  "carriers": "10"
}
```

Other example data can be found in the following gist: [Airport Data](https://gist.github.com/tdreyno/4278655)

## Tests

To run the Flight API tests follow the script below:

1. Enable _virtualenv_ **flight**;
2. Ensure that the dependencies are installed, especially:

        pytest
        pytest-coverage
        flake8

3. Run the commands below:

```shell
export PYTHONPATH=$(pwd)               # Set the python path as the project folder
pipenv install --dev                   # Install dev dependencies
pytest src/                            # Performs the tests
pytest --cov=. src/                    # Performs tests evaluating coverage
pytest --cov=. --cov-report xml src/   # Generate the XML report of coverage
flake8 src/                            # Run PEP8 linter
bandit .                               # Run bandit security checks
unset PYTHONPATH                       # Unset PYTHONPATH variable
```

During the tests the terminal will display a output with the test report (failures, skips and successes) and the system test coverage. For other configurations and supplemental documentation go to [pytest](https://pytest.org/en/latest/) and [coverage](https://pytest-cov.readthedocs.io/en/latest/).

During the lint process the terminal will report a bug report and warnings from the PEP8 style guide, for more configurations and additional documentation go to [flake8](http://flake8.pycqa.org/en/latest/index.html#quickstart) and [PEP8](https://www.python.org/dev/peps/pep-0008/)
