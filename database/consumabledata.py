# Effect code
#0 Healing 
#1 Mphealing
#2 Ailemt recovery
#3 Damage
consumables = {
    "0000":
    {
        "name":"testhealingitem",
        "effect":0,
        "multitarget":False,
        "variable":1,
    },
    "0001":
    {
        "name":"testmphealingitem",
        "effect":1,
        "multitarget":False,
        "variable":1,
    },
    "0002":{
        "name":"recoveritem",
        "effect":2,
        "multitarget":False,
        "status":[0000],
    },
    "0003":{
        "name":"testattackitem",
        "effect":3,
        "multitarget":False,
        "variable":1,
    }
}