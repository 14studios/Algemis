const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
	if (message.content === 'a!help') {
        var args = message.content.split(" ");
        args.pop('a!help');
        console.log(args)
        
        const exampleEmbed = new Discord.MessageEmbed()
	        .setColor('#0099ff')
	        .setTitle('Help Command')
            .setDescription('Help Command Test')
            .addFields(
                { name: '\u200B', value: '\u200B' },
                { name: 'Help: ', value: 'a!help', inline: true },
                { name: 'Encrypt:', value: 'a!encrypt', inline: true },
            )
		message.channel.send(exampleEmbed);
	}
});

client.login("token");