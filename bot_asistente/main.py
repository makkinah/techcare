import discord
client = discord.Client(intents=discord.Intents.all())
@client.event
async def on_message(message):
  if message.content == "!help":
    # Create a list of questions in Spanish
    questions = ["¿Cómo puedo instalar un nuevo sistema operativo?",
                  "¿Cómo puedo solucionar un problema con mi conexión a Internet?",
                  "¿Cómo puedo recuperar un archivo borrado?"]
    # Create a drop-down menu with the questions
    embed = discord.Embed(title="Ayuda",
                          description="Aquí tienes una lista de preguntas que puedo responder:",
                          color=0x00ff00)
    embed.add_field(name="Preguntas", value="\n".join(questions), inline=False)
    # Add a select menu to the embed
    embed.add_field(name="Seleccione una pregunta", value="\n".join([
        "1. ¿Cómo puedo instalar un nuevo sistema operativo?",
        "2. ¿Cómo puedo solucionar un problema con mi conexión a Internet?",
        "3. ¿Cómo puedo recuperar un archivo borrado?"
    ]), inline=False)
    # Send the embed to the user
    await message.channel.send(embed=embed)
client.run("MTEyMTQzNTEwNDY1MzM0NDgyOQ.G6IQFw.xcSFIBHnqeYKTnbvVWNEPc5qqEhPdFzqk3mUH8")

