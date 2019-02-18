from pathlib import Path
import fnmatch
import re

comment = re.compile(r'\s*#.*')
begin_entry = re.compile(r'\s*([\w]+)\s*{\s*')
end_entry = re.compile(r'\s*}\s*')
entry_line = re.compile(r'\s*([\w]+)=([^}]*)')


class Nagios:


    def loads(self, path):
        with Path(path).open() as status:

            self.parsed = {}

            in_entry = False
            current_entry = None
            while True:
                line = status.readline()
                if not line:
                    break
                if in_entry and entry_line.match(line):
                    key, value = entry_line.match(line).groups()
                    self.parsed[current_entry][-1][key] = value.strip()
                elif in_entry and end_entry.match(line):
                    current_entry = None
                    in_entry = False
                elif begin_entry.match(line) and not in_entry:
                    key = begin_entry.match(line).groups()[0]
                    if not key in self.parsed:
                        self.parsed[key] = [{}]
                    else:
                        self.parsed[key].append({})
                    current_entry = key
                    in_entry = True

            self.services = {
                s['host_name'].lower() + ':' + s['service_description'].lower(): s
                for s in self.parsed["servicestatus"]
            }

            self.hosts = [
                s['host_name'] for s in self.parsed["hoststatus"]
            ]

    def get_service(self, s):
        return self.services[s]

    def get_services(self, filterby):
        return ((s, self.services[s]) for s in fnmatch.filter(self.services, filterby))
