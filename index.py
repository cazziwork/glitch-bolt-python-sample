from slack_bolt import App

app = App()

@app.command("/hello-bolt-python")
async def command(ack, body, respond):
    await ack()
    await respond(f"Hi <@{body['user_id']}>!")

if __name__ == '__main__':
    app.start(3000)
