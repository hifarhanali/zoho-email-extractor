<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- ABOUT THE PROJECT -->
## About The Project
A simple python package to extract emails of senders from the eml files.

## Built With

## Project Structure
    |-- inputs/
    |   |-- /emails (input eml files)
    |   |-- /restricted_emails.csv (emails to be excluded)
    |-- outputs/
    |   |-- emails.csv (output csv file)
    |-- src/
    |   |-- extractor/
    |   |   |-- __init__.py
    |   |   |-- extractor.py
    |   |   |-- util.py
    |   |-- main.py

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

[![Python 3.6](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Getting Started

1. Clone the repository by running the following command:
    ```
    git clone https://github.com/hifarhanali/zoho-email-extractor.git
    ```

2. Change directory to the root directory of the repository:
    ```
    cd zoho-email-extractor
    ```

3. Install the dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```

4. Run the main.py file by running the following command:
    ```
    python src/main.py -i path/to/eml_files -o path/to/output_dir -output_file_name name_of_output_file --restricted_emails_path path/to/restricted_emails.csv
    ```
    e.g.
    ```
    python src/main.py -i ./inputs/emails -o ./outputs/ -output_file_name emails.csv --restricted_emails_path ./inputs/restricted_emails.csv
    ```



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Farhan Ali - [@hifarhanali](https://twitter.com/hifarhanali) - hifarhanali@example.com

Project Link: [https://github.com/hifarhanali/zoho-email-extractor](https://github.com/hifarhanali/zoho-email-extractor)




