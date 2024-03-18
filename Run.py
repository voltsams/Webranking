from scrapper.CheckPageSpeed import CheckPageSpeed
from scrapper.WordFrequency import WordFrequency
import GlobalsModule

GlobalsModule.Globals.prompt_user_to_enter_url(cls=GlobalsModule)

threadCheckPageSpeed = CheckPageSpeed()
threadCheckPageSpeed.start()
