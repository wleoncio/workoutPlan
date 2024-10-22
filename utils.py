import os

class Config:
    def __init__(self, config_path=".config/workoutPlan.conf"):
        self.config_path = os.environ.get("HOME") + "/" + config_path
        if os.path.exists(self.config_path):
            print("Config file found at " + self.config_path)
            self.log_path = open(self.config_path).readline()
            print(self)
        else:
            if self.config_path[-5:] != ".conf":
                raise ValueError("Config file must be a path ending in .conf")
            print("Creating new config file " + self.config_path)
            self.log_path = input("Enter location of log folder: ")
            self.log_path = "LOGPATH=" + self.log_path + "\n"
            self.save()

    def __str__(self):
        return self.log_path

    def save(self):
        stream = open(self.config_path, "wt")
        stream.write(self.log_path)
        stream.close()
        print("Config file created at " + self.config_path)
