import pymunk

# Game engine related
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
GAME_TIME = 20
FRAMERATE = 60

# Game physics related
GRAVITY_FORCE = -0

# Plane object related
PLANE_VERTICES = [(0, 0), (15, 0), (30, 5), (15, 10), (0, 10)]
PLANE_GRAVITY_CENTER = (15, 5)
PLANE_ROTATION_SPEED = 0.02
PLANE_MASS = 1
PLANE_STARTING_SPEED = 3
PLANE_MAX_SPEED = 10
PLANE_MIN_SPEED = 1
PLANE_SPEED_CHANGE_RATE = 0.02
PLANE_1_COLLISION_TYPE = 1
PLANE_2_COLLISION_TYPE = 2
PLANE_INERTIA = pymunk.inf

# Ammo related
PLANE_STARTING_AMMO = 10.
PLANE_HP = 10
AMMO_INCREASE_RATE = 0.1

# Bullet object related
BULLET_SPEED = 7
BULLET_MASS = 0.1
BULLET_INERTIA = pymunk.inf
BULLET_COLLISION_TYPE = 3

# HP Stripes related
HP_STRIPE_COLLISION_TYPE = 9
HP_STRIPE_VERTICES = [(0, 0), (2, 0), (2, 5), (0, 5)]

# Wall object related
WALL_COLLISION_TYPE = 5
WALL_COLOR = (150, 150, 150)  # Cool light gray
WALL_MASS = 1
WALL_INERTIA = pymunk.inf
