from typing import Any

from tkdesigner.utils import woah


class Node:
    def __init__(self, node: dict[str, Any]):
        self.node = node

    @property
    def id(self) -> str:
        return self.node.get("id", woah('No id?!'))

    @property
    def name(self) -> str:
        return self.node.get("name", woah('No name?!'))

    @property
    def visible(self) -> bool:
        """Whether or not the node is visible on the canvas."""
        return self.node.get("visible", True)

    @property
    def type(self) -> str:
        return self.node.get("type", woah('No type??!'))

    @property
    def plugin_data(self):
        return self.node.get("pluginData")

    @property
    def shared_plugin_data(self):
        return self.node.get("sharedPluginData")

    def get(self, key: str, default: Any | None = None):
        return self.node.get(key, default)


class Document(Node):
    def __init__(self, node: dict[str, Any], root: str = "window"):
        super().__init__(node)
        self.root = root

    @property
    def children(self) -> list[dict[str, Any]]:
        # TODO: Convert nodes to Node objects before returning a list of them.
        return self.node.get("children", woah('No childs :)'))


class Canvas(Node):
    @property
    def children(self):
        # TODO: Convert nodes to Node objects before returning a list of them.
        return self.node.get("children")

    @property
    def background_color(self):
        return self.node.get("backgroundColor")

    @property
    def prototype_start_node_id(self) -> str:
        return self.node.get("prototypeStartNodeID", woah('No `PrototypeStartNodeId`... Whats that'))

    @property
    def export_settings(self):
        return self.node.get("exportSettings")

    def generate(self):
        return ""


class Slice(Node):
    @property
    def export_settings(self):
        # TODO: Native conversion
        return self.node.get("exportSettings")

    @property
    def absolute_bounding_box(self):
        # TODO: Native conversion
        return self.node.get("absoluteBoundingBox")

    @property
    def size(self):
        # TODO: Native conversion
        return self.node.get("size")

    @property
    def relative_transform(self):
        # TODO: Native conversion
        return self.node.get("relativeTransform")
