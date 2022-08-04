# Input Format

The `inputs/` folder has the following files:
```
|-- README.md
|-- emails/ (folder with eml files to be parsed)
|   |-- sample_eml_file.eml
|-- restricted_emails.csv (csv file with emails to be ignored)
```


>**NOTE**: The `/inputs/emails` folder should contain valid eml files. A sample `sample_eml_file.eml` is provided in the `inputs/emails` folder.

## Format of the *restricted_emails.csv* file
```
emails
sample1@gmail.com
sample2.@gmail.com
...
samplen.@gmail.com
```
The extractor will ignore all the emails in the `restricted_emails.csv` file.

>**NOTE**: The default path to the restricted emails file is `None` (No email to be ignored). You can add the path to the restricted emails csv file by providing `--restricted_emails_file` argument.