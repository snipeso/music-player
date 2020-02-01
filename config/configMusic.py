from config.updateConfig import UpdateConfig

musicCONF = {
    "task": {
        "name": "music",
    },
    "instructions": {
        "text": "Just listen to the music.",
        "startPrompt": "Press any key to continue. Press q to quit.",
        "alarm": "horn.wav",
        "questionnaireReminder": "answerQuestionnaire.wav"
    },
    "stimuli": {
        # TODO: counterbalance order of presentation
        "songs": ["Tell.wav", "GOT.wav", ],
        "backgroundColor": "black",
    },
}


updateCofig = UpdateConfig()
updateCofig.addContent(musicCONF)

CONF = updateCofig.getConfig()
