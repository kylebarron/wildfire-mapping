"""
Download data
"""

import os
import requests

from io import BytesIO
from zipfile import ZipFile
from pathlib import Path

def main():
    data_dir = Path(os.getenv('DATA_DIR', '../data'))
    download(data_dir)


def download(data_dir):
    download_federal_wildland_fire_data(data_dir)


def download_federal_wildland_fire_data(data_dir):
    """Download USGS Federal Wildland Fire Occurrence Data

    https://wildfire.cr.usgs.gov/firehistory/data.html
    """

    nps_url = 'https://wildfire.cr.usgs.gov/firehistory/data/wf_nps_1980_2016.zip'
    r = requests.get(nps_url)
    buffer = BytesIO(r.content)

    dest_dir = data_dir / 'raw' / 'usgs' / 'fwfo' / 'nps'
    dest_dir.mkdir(exist_ok=True, parents=True)

    with ZipFile(buffer) as f:
        f.extractall(dest_dir)


if __name__ == '__main__':
    main()
