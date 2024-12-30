from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode, text_node_to_html_node
from enum import Enum

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalide markdown, formatted section not closed")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue

            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
            
        new_nodes.extend(split_nodes)
    return new_nodes