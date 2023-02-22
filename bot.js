const mineflayer = require('mineflayer');

// Set the server IP and port
const server_ip = 'play.hypixel.net';
const server_port = 25565;

// Set the Minecraft username and password
const username = 'testing@gmail.com';
const password = 'lmao123';

// Create a new bot instance and connect to the server
const bot = mineflayer.createBot({
  host: server_ip,
  port: server_port,
  username: username,
  password: password,
  auth: 'microsoft',
});

// Once the bot has connected, join the server
bot.once('spawn', () => {
  bot.chat('/join hypixel');
});
