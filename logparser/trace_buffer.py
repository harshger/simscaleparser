import time

class trace_buffer:
    traceid_vs_calls = {}
    traceid_vs_servicelist = {}
    traceid_vs_timestamp = {}

    def add_service(self, trace_id, caller_span, service):
        if trace_id not in self.traceid_vs_servicelist:
            self.traceid_vs_servicelist[trace_id] = []
        self.traceid_vs_servicelist[trace_id].append(service)

        if trace_id not in self.traceid_vs_calls:
            self.traceid_vs_calls[trace_id] = {}

        if caller_span not in self.traceid_vs_calls[trace_id]:
            self.traceid_vs_calls[trace_id][caller_span] = []
        self.traceid_vs_calls[trace_id][caller_span].append(service.__dict__)

        self.traceid_vs_timestamp[trace_id] = time.time()

    def get_traceid_vs_calls(self):
        return (self.traceid_vs_calls)

    def get_traceid_vs_servicelist(self):
        return (self.traceid_vs_servicelist)

    def get_traceid_vs_timestamp(self):
        return (self.traceid_vs_timestamp)

    def delete(self, traces):
       for t in traces:
         self.traceid_vs_timestamp.__delitem__(t)
         self.traceid_vs_servicelist.__delitem__(t)
         self.traceid_vs_calls.__delitem__(t)
