class SceneNode:
    def __init__(self, name: str, handle: bool) -> None:
        self.__name: str = name
        self.__handle: bool = handle
        self.__childrens: list[SceneNode] = list()

    def update(self, event: str) -> bool:
        self.__childrens.reverse()
        if self.__handle:
            print(f"the {event} is handled correctly by {self.__name}", self.__handle, )
            return True
        else:
            for children in self.__childrens:
                is_consumed: bool = children.update(event)
                if is_consumed:
                    return True
        return False

    def add_children(self, scene_node: 'SceneNode') -> None:
        self.__childrens.append(scene_node)

    def propagate(self, event: str) -> None:
        is_handled = self.update(event)
        if is_handled:
            print("the event is consumed by the child")
        else:
            print("the event is not handled by any childrens")

if __name__ == "__main__":
    print("hello")
    global_scene: SceneNode = SceneNode("Menu", False)
    settings_button: SceneNode = SceneNode("Settings", False)
    global_scene.add_children(settings_button)
    play_button: SceneNode = SceneNode("play", True)
    global_scene.add_children(play_button)
    global_scene.propagate("CLICK")
