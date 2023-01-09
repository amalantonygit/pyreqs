import argparse
import os

class Pyreqs:
    def generate_requirements(self):
        python_files = self.locate_python_files()

    def locate_python_files(self):
        parser = argparse.ArgumentParser(description="Just an example",
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('source', nargs='?', help="Python project location", default=os.getcwd())
        args = parser.parse_args()
        config = vars(args)
        return [os.path.join(r, fn) for r, ds, fs in os.walk(config["source"]) for fn in fs if fn.endswith((".py",".pyw",".ipynb")) and fn!="pyreqs.py"]

if __name__ == "__main__":
    Pyreqs().generate_requirements()

