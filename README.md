# Steam Game Predictor

A Simple algorithm made in Python. Based on the games you have played before, it generates a personalized score for a specific game/application, which tries to predict if you will enjoy the game or not before purchasing. 

## ⚠️ Disclaimer 

- **Accuracy:** Due to insufficent data received from Steam API endpoints, the produced result may not always be accurate. Use it as a guidance rather than conclusion.

- **Steam API Usage:** According to [Steam Web API Terms of Use](https://steamcommunity.com/dev/apiterms), Valve has rights to revoke your access at any time without any notice if it detects improper use of APIs. **It is highly recommended to wait a few minutes between each submission to avoid any issue.**


## ⚙️ Installation & Run

You need to install [Python 3.14](https://www.python.org/downloads/) or newer version.

1. Obtain an API key using the following link:

https://steamcommunity.com/dev/apikey

2. Download the project as ZIP or clone the repositionary: 
```bash
  git clone https://github.com/Artan-Jafarnejad/steam-game-predictor.git
  cd steam-game-predictor
```


3. Create a virtual environment:

```bash
  python -m venv steam-project
```

4. Activate the virtual environment:
```bash
  steam-project\Scripts\activate
```

5. Download and install contents inside the "requirements.txt" using following command:
```bash
  pip install -r requirements.txt
```

6. Run "main.py":
```bash
  python main.py
```

7. Open your browser and go to the following IP address:

http://127.0.0.1:5000

8. Fill the fields.

❗️**NOTE**: YOUR STEAM PROFILE MUST BE VISIBLE TO PUBLIC! YOU CAN CHANGE IT [HERE](https://steamcommunity.com/my/edit/settings?snr=100601___)❗️




## ‼️ Known Issues

- As described earlier, tags (or known as genres) retrieved from Steam API Endpoints are so different from what it's shown on the store page. As an example, only two tags "Free to Play" and "Action" are retrieved from the API for Counter-Strike, while the store page shows multiple tags such as "FPS", "Competitive", "Multiplayer" and etc. This results in a more inaccurate, or sometimes 0% score. More factors will be added in the future to prevent this issue.

- Application will not alert user if they enter a wrong URL.

- If a user has played many games, it may take much time to retrieve all the datas, let alone sometimes can cause rate limitation. 
