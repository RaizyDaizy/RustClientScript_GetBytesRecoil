import uniref
from uniref import WinUniRef

def GetRecoilPropertiesAddress():
    ref = WinUniRef("RustClient.exe")
    game = ref.injector.get_module_base("GameAssembly.dll")
    vvv = ref.find_class_in_image("Assembly-CSharp.dll", "RecoilProperties")
    get_recoil_offset = vvv.find_field("recoil")
    recoil = ref.injector.mem_read_bytes(game + 0x8DDD40, 150) # if you have raise MemoryError(f"Address {hex(address)} not readable"), Please Make Sure you get Module Base of GameAssembly.dll
    with open('Rust.txt', 'w') as x:
        x.write(str(recoil))
if __name__ == "__main__":
    GetRecoilPropertiesAddress()