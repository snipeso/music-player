from config.updateConfig import UpdateConfig

sampleCONF = {
    "task": {
        "name": "sample",
    },
    "instructions": {
        "text": "Give instructions",
        "startPrompt": "Press any key to continue. Press q to quit.",
        "alarm": "horn.wav",
    },
    "stimuli": {
        "backgroundColor": {"versionMain": "black", "versionDemo": "blue", "versionDebug": "gray"},
    },
}

sampleTriggers = {
    "example": 10
}


updateCofig = UpdateConfig()
updateCofig.addContent(sampleCONF)
updateCofig.addTriggers(sampleTriggers)

CONF = updateCofig.getConfig()
