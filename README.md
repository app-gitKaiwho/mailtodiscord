
ISSUES WITH TOKEN 

# Mail 2 Discord
## Setup Instructions<br>
Before running the project, you need to set up the Gmail and Discord APIs and generate tokens for them.<br>
1. **Discord Token**: Place the Discord token in the `param.json` file.
2. **Gmail Token**: Place the Gmail token.pickle in the `/token` folder.<br>
    If you run the without it, a Google prompt will help you get it.
3. **Discord ID** : Provide your discord ID in the `param.json` file<br>
Then place the 'param.json' file in the `/token` folder.<br>

<details>
  <summary>Clic here for gmail setup details</summary>

1. Go to the [Google Cloud Console](https://console.cloud.google.com/welcome?authuser=5&project=autorecponder) page
2. Click `Select a project`->`NEW PROJECT`
3. Then on the dashboard click `APIs and Services`
4. `ENABLE APIS AND SERVICES`->`Gmail API`->`ENABLE`
5. Then Click `OAuth consent screen`
6. Under User Type select `External` then `CREATE`
7. Fill obligatory information then `SAVE AND CONTINUE`
8. `ADD OR REMOVE SCOPES` and under `Manually add scopes` add the following :

        https://www.googleapis.com/auth/gmail.modify
        https://www.googleapis.com/auth/gmail.readonly
9. Then after clicking save a bunch more time you should be good to go
</details>

<details>
  <summary>Clic here for discord setup details</summary>

1. Go visit the [Discord Developer Applications](https://discord.com/developers/applications) page
2. create a new Application
3. under `Bot` click the `Reset Token` button and copy the api key
4. past it in `param.json` as your `discordtoken`
5. (you might need to invite you bot to a server once via url autorisation)
</details>


## Running the Project<br>
To run the project, use the following command:<br>
```bash
python3 main.py
```

## Runing in Docker

You will need to run the main.py once outside of docker to generate the pickle tocken then run :

```bash
sudo docker build -t mailtodiscord .
```
and once completed
```bash
./mailtodiscord.sh
```

<details>
  <summary></summary>

<div style="text-align:center">
  <img src="./asset/test.jpg" alt="Frog" width="400"/>
</div>
