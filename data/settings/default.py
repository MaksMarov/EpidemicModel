# Main simulation parameters

# Height of the game window
SIM_WINDOW_HEIGHT = 1000
# Width of the game window 
SIM_WINDOW_WIDTH = 1500
# Simulation speed (Frames per second - FPS) (optional)
SIM_SPEED = 30
# Number of simulation steps (ticks) (optional)
SIM_STEPS = 1000
# Background color of the simulation screen
SCREEN_COLOR = "white"
# Initial number of pawns in the simulation (optional)
SIM_START_PAWN_COUNT = 1000

# Main parameters for the location's boundary (walls)

# Offset of the boundary from the edge of the screen (distance from the border to the screen's edge)
BORDER_OFFSET = 2.5
# Thickness of the boundary (wall thickness)
BORDER_THICKNESS = 5
# Color of the boundary
BORDER_COLOR = "black"

# Main parameters for the pawn

# Size (radius) of the pawn (optional)
PAWN_RADIUS = 10
# Base color of the pawn (default color when healthy)
PAWN_BASE_COLOR = "yellow"
# Maximum movement speed of the pawn
PAWN_MAX_SPEED = 5
# Maximum initial immunity level of the pawn (randomized at spawn between 0 and this value) (optional)
PAWN_MAX_START_IMMUNITY = 0.1
# Probability of a pawn randomly getting sick without external interaction (optional)
PAWN_SICK_ACCIDENTALLY = 0.005

# Main parameters for the virus (initial strain)

# Contagiousness (probability of spreading the virus when a pawn comes into contact with another) (optional)
VIRUS_CONTAGIOUSNESS = 1
# Contagioness mutation intensity (optional)
VIRUS_CONTAGIOUSNESS_MUTATE_INTESITY = 0.2
# Severity (increases disease progression and affects health deterioration) (optional)
VIRUS_SEVERITY = 0.02
# Severity mutation intensity (optional)
VIRUS_SEVERITY_MUTATE_INTENSITY = 0.2
# Lethality (probability that the infection will result in death) (optional)
VIRUS_LETHALITY = 0
# Lethalyti mutation intensity (optional)
VIRUS_LETHALITY_MUTATE_INTESITY = 0.2
# Ability of the virus to mutate (probability of mutation) (optional)
VIRUS_MUTABLE = 0.1
# Mutation intensity (how drastically the virus changes during mutations) (optional)
VIRUS_MUTATE_INTENSITY = 0.1
# Params range % (optional)
VIRUS_PARAMS_RANGE = 0.05
# Name of the virus (optional)
VIRUS_NAME = "Curse"
# Strain of the virus (can be updated as the virus mutates) (optional)
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
# Disease progression speed (determines how quickly the infection worsens) (optional)
INFECTED_STATE_DISEASE_COEF = 0.15
# Immunity growth speed (determines how quickly the pawn builds immunity while infected) (optional)
INFECTED_STATE_IMMUNITY_COEF = 0.2