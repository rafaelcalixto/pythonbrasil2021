import carla
from random import choice
from time import sleep

client = carla.Client("localhost", 2000)
client.set_timeout(2.0)
world = client.get_world()

# Escolhendo a posição onde ele será colocado
spawn_point = choice(world.get_map().get_spawn_points())

blueprint_library = world.get_blueprint_library()

# Escolhendo o veículo
vehicle = choice(blueprint_library.filter("vehicle"))
vehicle.set_attribute("role_name", "autopilot")
if vehicle.has_attribute("color"):
    vehicle.set_attribute("color", choice(vehicle.get_attribute("color").recommended_values))

actor = carla.command.SpawnActor(vehicle, spawn_point).then(carla.command.SetAutopilot(carla.command.FutureActor, True))

client.apply_batch_sync([actor])
