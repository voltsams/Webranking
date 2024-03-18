from scrapper.CheckPageSpeed import CheckPageSpeed
import GlobalsModule

GlobalsModule.Globals.prompt_user_to_enter_url(cls=GlobalsModule)

threadCheckPageSpeed = CheckPageSpeed()
threadCheckPageSpeed.start()
