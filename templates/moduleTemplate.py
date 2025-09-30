






class ModuleClass:

   moduleId = "com.iot-eq.module.template"

   def __init__(self,managerConfig,databaseInstance):
      self.config = managerConfig
      self.database = databaseInstance

      print("Module: ",self.moduleId," Initialized")

   def start(self):
      print("Module: ",self.moduleId," Started")
      return

   def run(self):
      print("Module: ",self.moduleId," Run")
      return

   def stop(self):
      print("Module: ",self.moduleId," Stopped")
      return

   def diagnostics(self):
      return {}

