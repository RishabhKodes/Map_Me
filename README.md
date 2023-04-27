# mapMe

## About The Project

MapMe is a textual-based navigation service that gives directions on your phone without using the internet. This service doesn’t require the users
to have a smartphone.

The backend service of the project mainly uses Flask, Google Maps API and Twilio API.

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
```sh
git clone git@github.com:RishabhKodes/mapMe.git
```
2. Goto root directory
```sh
cd mapMe
```
3. Create Virtual env for the project (optional)
```
python3 -m venv mapme
source mapme/bin/activate
```
4. Install pip packages
```sh
pip install -r requirements.txt
```
5. Set env variables:
```JS
export key="GCP_PROJECT_KEY"
export user_agent="GCP PROJECT NAME"
export account_sid = "TWILIO ACCOUNT SID"
export account_token = "TWILIO ACCOUNT TOKEN"
export phone = "TWILIO PHONE NUMBER"
```
6. Run the service
```sh
python src/app.py
```
<br>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact Me

**Rishabh Bhandari -** [Website](https://rishabhbhandari.me/)
[LinkedIn](https://www.linkedin.com/in/rishabh-bhandari-ba5778168/)
[Email](rishabhbhandari6@gmail.com)


<p align="center">
Made with :heart: <br>
by e33or_assasin
</p>