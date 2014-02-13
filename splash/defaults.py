
# timeouts
TIMEOUT = 30
WAIT_TIME = 0.0

MAX_TIMEOUT = 60.0
MAX_WAIT_TIME = 10.0

# png rendering options
VIEWPORT = '1024x768'
VIEWPORT_FALLBACK = VIEWPORT  # do not set it to 'full'
VIEWPORT_MAX_WIDTH = 20000
VIEWPORT_MAX_HEIGTH = 20000
VIEWPORT_MAX_AREA = 4000*4000

MAX_WIDTH = 1920
MAX_HEIGTH = 1080

# defaults for render.json endpoint
DO_HTML = 0
DO_IFRAMES = 0
DO_PNG = 0
SHOW_SCRIPT = 0
SHOW_CONSOLE = 0

# servers
SPLASH_PORT = 8050
PROXY_PORT = 8051
MANHOLE_PORT = 5023
MANHOLE_USERNAME = 'admin'
MANHOLE_PASSWORD = 'admin'

# pool options
SLOTS = 50
CACHE_ENABLED = False
CACHE_SIZE = 50  # MB
CACHE_PATH = '.splash-cache'
