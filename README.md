# Project Name

## Setup Instructions

Before running the project, you need to set up the Gmail and Discord APIs and generate tokens for them. 

1. **Discord Token**: Place the Discord token in the `/token/bottoken` file.
2. **Gmail Token**: Place the Gmail token in the `/token/token.pickle` file. If you run the program manually, a Google prompt will ask for this token.

You also need to provide your admin ID in the `param.json` file, where you can also change some options. Place this file in the `/token` folder.

## Running the Project

To run the project, use the following command:

```bash
python3 main.py