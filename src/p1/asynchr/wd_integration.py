import asyncio
import hashlib
from asyncache import cached
from dataclasses import dataclass, fields
from cachetools import TTLCache

import aiohttp


@dataclass
class WdToken:
    studentid: int
    wdauth: str
    expiry_epoch_s: int

@dataclass
class User:
    studentid: int
    album: str
    imie: str
    nazwisko: str

    @staticmethod
    def from_dict(d: dict) -> 'User':
        pola = []
        for field in fields(User):
            pola.append(field.name)
        return User(**{ a: b for a, b in d.items() if a in pola })


class UnauthorizedError(BaseException):
    def __str__(self) -> str:
        return 'Wrong username or password :/'


class UnknownError(BaseException):
    pass


async def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@cached(TTLCache(100, 180))
async def get_user(wdauth: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://wdauth.wsi.edu.pl/user?wdauth={wdauth}') as res:
            received_data = await res.json()
            return User.from_dict(received_data)

class UserService:
    async def login_user(album: str, password: str) -> WdToken:
        _hash = await hash_password(password)
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://wdauth.wsi.edu.pl/authenticate?album={album}&pass={_hash}') as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return WdToken(studentid=data['token']['studentid'],
                                   wdauth=data['token']['wdauth'],
                                   expiry_epoch_s=data['token']['expiry_epoch_s'])
                elif resp.status == 401:
                    raise UnauthorizedError
                else:
                    raise UnknownError


async def main():
    # token = await login_user('kurs01', '...') #f6b22d5e-a9df-4a36-8ae4-f347657faaf6
    # print(token)

    print(await get_user('f6b22d5e-a9df-4a36-8ae4-f347657faaf6'))

if __name__ == '__main__':
    asyncio.run(main())