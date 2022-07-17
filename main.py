import requests

class Syrup:
    """
    A nice and sweet API wrapper made for Maple
    https://maple.io/
    """
    API_URL = 'http://localhost:8000'
    ENDPOINTS = {
        'zen': '/api/zen',
        'login': '/api/login',
        'myself': '/api/me',
        'all_users': '/api/user',
        'user_detail': '/api/user/',
        'follow': '/api/follow/',
        'following': '/api/following/',
        'followers': '/api/followers/',
        'create_feed': '/api/feed/create/',
        'all_feeds': '/api/feed/all',
        'explore': '/api/feed/explore',
        'user_feeds': '/api/feed/user/',
        'detail_feed': '/api/feed/id/',
        'like_feed': '/api/feed/like/',
    }
    AUTHORIZATION_KEY: str = None
    PARAM_NAME: str = 'X-API-KEY'

    def __init__(self):
        pass


    def zen(self):
        """
        The Zen of Python, by Tim Peters.
        """
        res = requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('zen')}")
        print(res.json())

    def login(self, username:str, password:str, log_success:bool=True, debug_log=False):
        """
        Login the user with username and password
        """
        CREDENTIALS = {'username':username, 'password':password}
        res = requests.post(url=f"{self.API_URL}{self.ENDPOINTS.get('login')}", data=CREDENTIALS)
        data = res.json()
        self.AUTHORIZATION_KEY = data.get('token')
        if log_success:
            print("Logged in successfully")
        if debug_log:
            print(data)

    def myself(self):
        """
        Get the info about the authenticated user.
        """
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('myself')}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        }).json()
    
    def all_users(self, limit:int=30, offset:int=0):
        """
        Get all the users with paginated value.
        """
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('all_users')}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        },
        data={
            'limit': limit,
            'offset':offset
        }).json()
    
    def user_detail(self, username:str):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('user_detail')}{username}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        }).json()

    def follow(self, username:str):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('follow')}{username}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        }).json()

    def followers(self, username:str, limit:int=30, offset:int=0):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('followers')}{username}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        },
        data={
            'limit': limit,
            'offset':offset
        }).json()

    def following(self, username:str, limit:int=30, offset:int=0):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('following')}{username}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        },
        data={
            'limit': limit,
            'offset':offset
        }).json()
    
    def create_feed(self, body:str):
        return requests.post(url=f"{self.API_URL}{self.ENDPOINTS.get('create_feed')}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        },
        data={
            'body':body
        }).json()

    def all_feeds(self, limit:int=30, offset:int=0):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('all_feeds')}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        },
        data={
            'limit': limit,
            'offset':offset
        }).json()

    def user_feeds(self, username:str, limit:int=30, offset:int=0):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('user_feeds')}{username}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        },
        data={
            'limit': limit,
            'offset':offset
        }).json()
    
    def feed_detail(self, id:int):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('detail_feed')}{id}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        }).json()


    def like_feed(self, id:int):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('like_feed')}{id}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        }).json()

    def explore(self, limit:int=30, offset:int=0):
        return requests.get(url=f"{self.API_URL}{self.ENDPOINTS.get('explore')}", headers={
            f"{self.PARAM_NAME}": self.AUTHORIZATION_KEY
        },
        data={
            'limit': limit,
            'offset':offset
        }).json()
    