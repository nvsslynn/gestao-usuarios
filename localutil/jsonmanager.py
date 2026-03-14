import json, os, time

class JSONManager:
    def __init__(self, path):
        if os.path.exists(path):
            self.path = path
        else:
            with open(path, "w+") as f:
                f.write(json.dumps({}))
            self.path = path
    
    def get(self) -> dict:
        with open(self.path, "r") as f:
            return json.loads(f.read())

    def save(self, data:dict):
        with open(self.path, "w") as f:
            f.write(json.dumps(data))
    
    def deleteF(self):
        try:
            os.remove(self.path)
            return 0
        except:
            return 1

    def __repr__(self):
        return f"<JSON Controller for '{self.path}'>"

if __name__ == "__main__":
    test = JSONManager("./testing.json")
    time.sleep(3)
    assert test.deleteF() == 0