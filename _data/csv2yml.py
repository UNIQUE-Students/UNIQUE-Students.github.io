import yaml
import pandas as pd
import re
from argparse import ArgumentParser

def parsed_args():
    """
    Parse and returns command-line args

    Returns:
        argparse.Namespace: the parsed arguments
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--input_csv",
        default="bios.csv",
        type=str,
        help="CSV containing the info from the form",
    )
    parser.add_argument(
        "--output_yml",
        default="bios.yml",
        type=str,
        help="Output YAML file",
    )
    parser.add_argument(
        "--output_photos",
        default="./assets/img/team/team-photos",
        type=str,
        help="List of photos URL",
    )

    return parser.parse_args()


if __name__ == "__main__":
    # -----------------------------
    # -----  Parse arguments  -----
    # -----------------------------
    args = parsed_args()
    print("Args:\n" + "\n".join([f"    {k:20}: {v}" for k, v in vars(args).items()]))

    # Read CSV
    df = pd.read_csv(args.input_csv, index_col=False)

    # Rename columns
    df.rename(columns={
        "Name": "fullname",
        "Short bio": "bio",
        "Email": "email",
        "Website": "website",
        "Affiliation": "affiliation",
        "Twitter": "twitter",
        "Pronouns": "pronouns",
        "Photo": "photo",
        "Committee": "committee",
        }, inplace=True)
    
    # Replace Nan with "none"
    df.fillna("none", inplace=True)

    # Edit Photo item and download photo
    f_photos = open(args.output_photos, "w")
    for idx in range(len(df)):
        photo_orig = df.iloc[idx].photo
        if photo_orig != "none":
            name_orig = df.iloc[idx].fullname
            photo_file = name_orig.lower().replace(" ", "_")
            photo_url = re.search('\(([^)]+)', photo_orig).group(1)
            photo_ext = photo_url.split(".")[-1].lower()
            photo_file_orig = "{}_orig.{}".format(photo_file, photo_ext)
            f_photos.write(photo_file_orig + " " + photo_url + "\n")
            df.loc[idx, 'photo'] = photo_file + ".jpg"
        else:
            df.loc[idx, 'photo'] = "none"

    f_photos.close()

    # Write YAML
    df_dict = df.to_dict(orient='records')
    with open(args.output_yml, "w") as f:
        yaml.dump(df_dict, f)

