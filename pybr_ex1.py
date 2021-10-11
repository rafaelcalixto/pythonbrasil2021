import carla
from random import choice
from time import sleep

client = carla.Client("localhost", 2000)
client.set_timeout(2.0)
world = client.load_world("Town02")

# Escolhendo a posição onde ele será colocado
spawn_point = choice(world.get_map().get_spawn_points())

blueprint_library = world.get_blueprint_library()

# Escolhendo o veículo
while True:
    vehicle = choice(blueprint_library.filter("vehicle"))
    if int(vehicle.get_attribute("number_of_wheels")) == 4:
        break
        
vehicle.set_attribute("role_name", "autopilot")
if vehicle.has_attribute("color"):
    vehicle.set_attribute("color", choice(vehicle.get_attribute("color").recommended_values))

env = carla.command.SpawnActor(vehicle, spawn_point).then(carla.command.SetAutopilot(carla.command.FutureActor, True))

actor_id = client.apply_batch_sync([env])[0].actor_id

actor = world.get_actors([actor_id])[0]
sleep(20)
actor.destroy()
