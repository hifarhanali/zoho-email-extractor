import argparse
from extractor import EmailExtractor

def main():
    parser = argparse.ArgumentParser("Email Extractor For EML Files")
    parser.add_argument("-i", "--input_dir", default="./inputs", type=str, help="Path to the directory that contain eml files")
    parser.add_argument("-o", "--output_dir", default="./outputs", type=str, help="Path to the directory that contain eml files")
    parser.add_argument("--output_filename", default="emails.csv", type=str, help="Filename to save the extracted emails")
    parser.add_argument("--restricted_emails_path", default=None, type=str, help="Path to the file that contain restricted emails")

    args = parser.parse_args()

    EmailExtractor.extract(args.input_dir, args.output_dir, args.output_filename, args.restricted_emails_path)

if __name__ == "__main__":
    main()