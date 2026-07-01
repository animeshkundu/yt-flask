import json

from flask import Flask

from flask_ask import Ask, question


def test_launch_request_returns_alexa_response():
    app = Flask(__name__)
    app.config["ASK_VERIFY_REQUESTS"] = False

    ask = Ask(app, "/alexa")

    @ask.launch
    def launched():
        return question("Welcome to Flask-Ask")

    payload = {
        "version": "1.0",
        "session": {
            "new": True,
            "sessionId": "SessionId.test",
            "application": {"applicationId": "amzn1.ask.skill.test"},
            "user": {"userId": "amzn1.ask.account.test"},
            "attributes": {},
        },
        "context": {
            "System": {
                "application": {"applicationId": "amzn1.ask.skill.test"},
                "user": {"userId": "amzn1.ask.account.test"},
                "device": {"deviceId": "test-device"},
            }
        },
        "request": {
            "type": "LaunchRequest",
            "requestId": "EdwRequestId.test",
            "timestamp": "2020-01-01T00:00:00Z",
            "locale": "en-US",
        },
    }

    response = app.test_client().post(
        "/alexa",
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert response.status_code == 200

    body = json.loads(response.get_data(as_text=True))
    assert body["version"] == "1.0"
    assert body["response"]["outputSpeech"]["type"] == "PlainText"
    assert body["response"]["outputSpeech"]["text"] == "Welcome to Flask-Ask"
    assert body["response"]["shouldEndSession"] is False
