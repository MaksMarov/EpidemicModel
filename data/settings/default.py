# Main simulation parameters

# Height of the game window
SIM_WINDOW_HEIGHT = 1000
# Width of the game window
SIM_WINDOW_WIDTH = 1500
# Simulation speed (Frames per second - FPS)
SIM_SPEED = 30
# Number of simulation steps (ticks)
SIM_STEPS = 2000
# Background color of the simulation screen
SCREEN_COLOR = "white"
# Initial number of pawns in the simulation
SIM_START_PAWN_COUNT = 1000

# Main parameters for the location's boundary (walls)

# Offset of the boundary from the edge of the screen (distance from the border to the screen's edge)
BORDER_OFFSET = 2.5
# Thickness of the boundary (wall thickness)
BORDER_THICKNESS = 5
# Color of the boundary
BORDER_COLOR = "black"

# Main parameters for the pawn

# Size (radius) of the pawn
PAWN_RADIUS = 2.5
# Base color of the pawn (default color when healthy)
PAWN_BASE_COLOR = "yellow"
# Maximum movement speed of the pawn
PAWN_MAX_SPEED = 5
# Maximum initial immunity level of the pawn (randomized at spawn between 0 and this value)
PAWN_MAX_START_IMMUNITY = 0.1
# Probability of a pawn randomly getting sick without external interaction
PAWN_SICK_ACCIDENTALLY = 0.005

# Main parameters for the virus (initial strain)

# Contagiousness (probability of spreading the virus when a pawn comes into contact with another)
VIRUS_CONTAGIOUSNESS = 0.7
# Severity (increases disease progression and affects health deterioration)
VIRUS_SEVERITY = 0.02
# Lethality (probability that the infection will result in death)
VIRUS_LETHALITY = 0
# Ability of the virus to mutate (probability of mutation)
VIRUS_MUTABLE = 0.1
# Mutation intensity (how drastically the virus changes during mutations)
VIRUS_MUTATE_INTENSITY = 0.1
# Name of the virus
VIRUS_NAME = "Curse"
# Strain of the virus (can be updated as the virus mutates)
VIRUS_STRAIN = ""

# Main parameters for the pawn states

# Healthy

# Color representing the healthy state
HEALTHY_STATE_COLOR = "green"

# Dead

# Color representing the dead state
DEAD_STATE_COLOR = "gray"

# Infected

# Color representing the infected state
INFECTED_STATE_COLOR = "red"
# Disease progression speed (determines how quickly the infection worsens)
INFECTED_STATE_DISEASE_COEF = 0.15
# Immunity growth speed (determines how quickly the pawn builds immunity while infected)
INFECTED_STATE_IMMUNITY_COEF = 0.2
