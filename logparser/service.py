
class service:
    def __init__(self, start_time, end_time, service_name, span, calls):
        self.start = start_time
        self.end = end_time
        self.service = service_name
        self.span = span
        self.calls = calls

    def get_span(self):
        return (self.span)

    def get_start(self):
        return (self.start)
