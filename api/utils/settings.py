import os

from pydantic import BaseModel


from dotenv import load_dotenv
load_dotenv()



class Settings(BaseModel):
    _db_name_user : str = os.getenv('DB_NAME_USER')
    db_user : str = os.getenv('DB_USER')
    db_pass : str = os.getenv('DB_PASS')
    db_host : str = os.getenv('DB_HOST')
    db_port : str = os.getenv('DB_PORT')
    
    def __str__(self) -> str:
        return f"_db: {self._db_name_user} user: {self.db_user} pass: {self.db_pass} port: {self.db_port} \n db: {self.db_name_user}"
    
    
    
    secret_key:str = os.getenv('SECRET_KEY')
    token_expire:int = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
    
    @property
    def db_name_user(self):
        if os.getenv('RUN_ENV') == 'test':
            return 'test_' + self._db_name_user
        else:
            return self._db_name_user

