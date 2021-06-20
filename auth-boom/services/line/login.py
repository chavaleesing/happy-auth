from integrations.line import LineIntegration

class LineLogin:

    def __init__(self) -> None:
        self.line_integration = LineIntegration()

    def login(self, data: dict) -> dict:
        resp = self.line_integration.login(data)
        return resp
