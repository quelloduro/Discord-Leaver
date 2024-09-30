# 10 star = new tool!
# use at ur own risk token can be locked cuz its proxyless leaver

import pystyle
from pystyle import Colorate, Colors
import time
import os
import requests
import colorama
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor, as_completed
r = Fore.RED 
y = Fore.YELLOW
rr = Fore.RESET
greennn = Fore.GREEN 
class DiscordLeaver:
    def __init__(self):
        self.base_url = "https://discord.com/api/v9"

    def headers(self, token):
        return {
            "Authorization": token, # made by
            "Content-Type": "application/json"
        }

    def get_guild_name(self, guild, token):
        response = requests.get(f"{self.base_url}/guilds/{guild}", headers=self.headers(token))
        if response.status_code == 200:
            return response.json().get("name", guild) 
        return guild
# durooooooooo
    def leave_guild(self, token, guild):
        try:
            guild_name = self.get_guild_name(guild, token)

            payload = {
                "lurking": False
            }

            while True:
                response = requests.delete(f"{self.base_url}/users/@me/guilds/{guild}",
                                           headers=self.headers(token), json=payload)

                if response.status_code == 204:
                    print(f"{greennn}[+]{rr} Left: {token[:25]} from {guild_name}")
                    break
                elif response.status_code == 429:
                    retry_after = response.json().get("retry_after", 1)
                    print(f"{y}[-]{rr} RATE LIMITED: sleeping for {retry_after} seconds...")
                    time.sleep(retry_after)
                else:
                    error_message = response.json().get("message", "Unknown error")
                    print(f"{r}[-]{rr} FAILED to leave guild: {error_message}")
                    break
        except Exception as e:
            print(f"EXCEPTION: {e}")

def read_tokens(file_path):
    try:
        with open(file_path, "r") as file:
            tokens = [line.strip() for line in file.readlines()]
        return tokens
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def leave_guilds_for_all_tokens(tokens, guild_id):
    leaver = DiscordLeaver()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(leaver.leave_guild, token, guild_id): token for token in tokens}

        for future in as_completed(futures):
            token = futures[future]
            try:
                future.result()  
            except Exception as e:
                print(f"EXCEPTION for token {token[:25]}: {e}")

if __name__ == "__main__":
    tokens = read_tokens("tokens.txt")
    
    if not tokens:
        print("No tokens in tokens.txt.")
    else:
        os.system('cls')
        os.system("title Leaver pls give credit and leave a star ")
        print(Colors.purple,'''
╦  ┌─┐┌─┐┬  ┬┌─┐┬─┐
║  ├┤ ├─┤└┐┌┘├┤ ├┬┘
╩═╝└─┘┴ ┴ └┘ └─┘┴└─

        ''')
        print(f'{greennn}put a star or i fuck you nigga{rr}')
        guild_id = input("Guild id?: ")

        leave_guilds_for_all_tokens(tokens, guild_id)
