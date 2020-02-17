from logparser import trace_buffer as bf
from logparser import trace as tr
from logparser import service as sm
import json
import time

class log_parser:
    def __init__(self):
        self.buffer = bf.trace_buffer()

    def process_log_entry(self, log_entry, force):
        output = []
        error = []
        trace_id, caller_span, service = self.parse_log_entry(log_entry)
        if not trace_id:
            error.append("Malformed Input: " + log_entry)
        else:
            self.buffer.add_service(trace_id, caller_span, service)

        self.process_buffer(output, error, force)
        return output, error

    def parse_log_entry(self, log_entry):
        split_log = log_entry.split()
        if len(split_log) == 5:
            span = split_log[4].split('->')
            if len(span) == 2:
                trace_id = split_log[2]
                caller_span = span[0]
                service = sm.service(split_log[0], split_log[1], split_log[3], span[1], [])
                return trace_id, caller_span, service
        return None, None, None

    def process_buffer(self, output, error, force):
        now = time.time()
        traces = []
        trace_dict = self.buffer.get_traceid_vs_calls()
        for k, v in self.buffer.get_traceid_vs_timestamp().items():
            if force or int(now - v) > 20:
                trace_id = k
                for s in self.buffer.get_traceid_vs_servicelist()[trace_id]:
                    if s.span in trace_dict[trace_id]:
                        s.calls = trace_dict[trace_id][s.span]

                if "null" not in trace_dict[trace_id]:
                    error.append("Discarding Trace: "+trace_id)
                else:
                    root = trace_dict[trace_id]["null"][0]
                    t = tr.Trace(trace_id, root)
                    output.append(json.dumps(t.__dict__, indent=4))

                traces.append(trace_id)

        self.buffer.delete(traces)
        return output, error


