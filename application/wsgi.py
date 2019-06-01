from whitenoise import WhiteNoise

import app

application = WhiteNoise(app)
application.add_files('static/', prefix='static/')
