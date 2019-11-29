import os
import errno


class MockGenerator:
    _base_dir = 'static/mocks/'

    def __init__(self, endpoints):
        self.endpoints = endpoints

    def create_mock(self):
        """crete mock folders and files"""
        for key in self.endpoints:
            for method in self.endpoints[key]:
                file = '%s/%s[%s].json' % (self._base_dir, key, method)

                if not os.path.exists(os.path.dirname(file)):
                    try:
                        os.makedirs(os.path.dirname(file))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                with open(file, "w") as f:
                    f.write("{}")

