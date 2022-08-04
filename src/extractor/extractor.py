
import json
from .util import Util
import os
from email import policy
from email.parser import BytesParser

class EmailExtractor:
    @staticmethod
    def __read_file_data__(filename: str):
        assert len(filename) > 5

        with open(filename, 'rb') as reader:
            msg = BytesParser(policy=policy.default).parse(reader)
            return msg

    @staticmethod
    def __extract__(filename: str):
        msg = EmailExtractor.__read_file_data__(filename)
        sender_info = msg["from"]
        sender_email = sender_info.split(" ")[-1].replace("<", "").replace(">", "")
        return sender_email


    @staticmethod
    def __read_restricted_emails__(restricted_emails_path: str):
        restricted_emails = []
        if restricted_emails_path is not None:
            restricted_emails_df = Util.read_from_csv(restricted_emails_path)
            if restricted_emails_df is not None:
                restricted_emails = restricted_emails_df["emails"].tolist()    
        return restricted_emails


    @staticmethod
    def extract(input_directory="./inputs", output_directory: str = "./outputs", output_filename: str = "emails.csv", restricted_emails_path: str = None):
        assert input_directory != ""

        print("[+] Extracting emails from {}".format(input_directory))

        restricted_emails = EmailExtractor.__read_restricted_emails__(restricted_emails_path)
        filenames = Util.get_all_files_in_dir(input_directory)

        emails = set()
        for filename in filenames:
            file_path = os.path.join(input_directory, filename)
            sender_email = EmailExtractor.__extract__(file_path)
            if sender_email not in restricted_emails:
                emails.add(sender_email)

        # Write to csv
        Util.write_to_csv(dict(emails=list(emails)), output_directory, output_filename)

