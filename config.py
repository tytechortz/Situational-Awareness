import os

appDataPath = "/Users/jamesswank/Python_Projects/Situational_Awareness/appData"
assetsPath = "/Users/jamesswank/Python_Projects/Situational_Awareness/assets"

if os.path.isdir(appDataPath):
    app_data_dir = appDataPath
    assets_dir = assetsPath
    cache_dir = "cache"
else:
    app_data_dir = "appData"
    assets_dir = "assets"
    cache_dir = "/tmp/cache"

config = {
    "app_data_dir": app_data_dir,
    "plotly_config":{
        'Arapahoe': {'center': [39.65, -104.8], 'zoom': 10.4}
    },
}

