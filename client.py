import asyncssh
import json

class Client:
    def __init__(self, username, password, serverpy_path):
      self.host = 'portal.cs.virginia.edu'
      self.username = username
      self.password = password
      self.execute_path = serverpy_path
      self.command_creator = lambda api_method, query: f'python3 {self.execute_path} {api_method} "{query}"'
    
    async def get_query(self, query):
      command = self.command_creator("query",query)
      return await self.__handle_ssh(command)
    
    async def get_recent(self, num_articles):
      command = self.command_creator("recent",num_articles)
      return await self.__handle_ssh(command)
    
    async def update(self, url):
      command = self.command_creator("update",url)
      return await self.__handle_ssh(command)
    
    async def get_by_author(self, author):
      command = self.command_creator("author",author)
      return await self.__handle_ssh(command)
     
    async def get_by_url(self, url):
      command = self.command_creator("url",url)
      return await self.__handle_ssh(command)
    
    async def get_by_name(self, name):
      command = self.command_creator("name",name)
      return await self.__handle_ssh(command)
    
    async def __handle_ssh(self,command):
      stdout, stderr = await self.__execute_ssh(command)
      if not stderr == '':
          raise Exception(f"Exception occured on server side:\n{stderr}\nStdin:\n{command}")
      return json.loads(stdout) if not stdout == None else None 
    
    async def __execute_ssh(self, command):
      async with asyncssh.connect(self.host, username=self.username, password=self.password) as conn:
        result = await conn.run(command)
        stdout = result.stdout
        stderr = result.stderr
      return stdout, stderr