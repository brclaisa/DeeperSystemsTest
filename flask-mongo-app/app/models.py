from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    active: bool = True
    created_ts: float = datetime.utcnow().timestamp()

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "roles": self.roles,
            "preferences": self.preferences.__dict__,
            "active": self.active,
            "created_ts": self.created_ts
        }