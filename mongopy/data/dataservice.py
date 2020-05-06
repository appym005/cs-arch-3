from .camera import Camera
from pymongo import read_preferences


def create_entry(latitude: str, longitude: str) -> Camera:
    camera = Camera()
    if len(Camera.objects()) != 0:
        camera.cam_id = Camera.objects.order_by('-cam_id').first().cam_id + 1
    camera.latitude = latitude
    camera.longitude = longitude

    camera.save()

    return camera

def get_info(cam_id):
    camera = Camera()
    print(cam_id)
    cam = Camera.objects(cam_id=cam_id)
    print(cam)
    if len(cam) > 0:

        print(cam)
        return cam
    else:
        return []



