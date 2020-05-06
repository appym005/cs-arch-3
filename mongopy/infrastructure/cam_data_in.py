import data.dataservice as svc
import data.mongo_setup as mongo_setup

mongo_setup.global_init()


def datain():

    latitude = input()
    longitude = input()

    svc.create_entry(latitude, longitude)


"""s = svc.get_info(1)
print(s)
print(s[0])
print(s[0].latitude)"""
datain()