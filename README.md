
<!-- ABOUT THE PROJECT -->
## About The Project
A simple python package to extract sender emails from a list of eml files.

## Motivation
Recently, I found myself in a situation where I have to prepare a spreadsheet for all the emails in the inbox of the company Gmail account.
I was provided with eml files of inbox emails. Instead of manually extracting thousands of emails, I have decided to write a python script to automate the process.


## Built With
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />


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
    python src/main.py -i path/to/eml_files -o path/to/output_dir --output_filename name_of_output_file --restricted_emails_path path/to/restricted_emails.csv
    ```
    e.g.
    ```
    python src/main.py -i ./inputs/emails -o ./outputs/ --output_filename emails.csv --restricted_emails_path ./inputs/restricted_emails.csv
    ```



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Farhan Ali - [@hifarhanali](https://twitter.com/hifarhanali) - hifarhanali@example.com

Project Link: [https://github.com/hifarhanali/zoho-email-extractor](https://github.com/hifarhanali/zoho-email-extractor)

