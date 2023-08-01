"use strict";
import SSH2Promise from 'ssh2-promise';
const host = 'portal.cs.virginia.edu';
const serverpy_path = 'test/server.py'; // bad practice

const commandCreator = (apiMethod, query) => `python3 ${serverpy_path} ${apiMethod} "${query}"`;

export async function getQuery(username, password, query) {
  const command = commandCreator('query', query);
  return await handleSSH(username, password, command);
}

export async function getRecent(username, password, numArticles) {
  const command = commandCreator('recent', numArticles);
  return await handleSSH(username, password, command);
}

export async function update(username, password, url) {
  const command = commandCreator('update', url);
  return await handleSSH(username, password, command);
}

export async function getByAuthor(username, password, author) {
  const command = commandCreator('author', author);
  return await handleSSH(username, password, command);
}

export async function getByURL(username, password, url) {
  const command = commandCreator('url', url);
  return await handleSSH(username, password, command);
}

export async function getByName(username, password, name) {
  const command = commandCreator('name', name);
  return await handleSSH(username, password, command);
}

async function handleSSH(username, password, command) {
  const sshconfig = {
    host: host,
    username: username,
    password: password,
  }
  const conn = new SSH2Promise(sshconfig);
  try {
    const result = await conn.exec(command);
    const parseResult = result ? JSON.parse(result) : null
    conn.close()
    return parseResult;
    
  } catch (error) {
    conn.close()
    throw error;
  } 
}
