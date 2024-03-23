class Node:
    __slots__ = '_data', '_value', '_left_tree', '_right_tree', '_black', '_parent_tree', '_is_left_child'

    def __init__(self, value, black=False, left_tree=None, right_tree=None,
                 parent_tree=None, is_left_child=False):
        self._data = value.author
        self._value = value
        self._black = black
        self._left_tree = left_tree
        self._right_tree = right_tree
        self._parent_tree = parent_tree
        self._is_left_child = is_left_child

    def __repr__(self):
        return f'Node with key = {self._value}, _left_tree = {self._left_tree}, ' \
               f'_right_tree = {self._right_tree}, _color = {self._black}'

    @property
    def node_data(self):
        return self._data

    @node_data.setter
    def node_data(self, new_data):
        self._data = new_data

    @property
    def node_left_tree(self):
        return self._left_tree

    @node_left_tree.setter
    def node_left_tree(self, new_ptr):
        self._left_tree = new_ptr

    @property
    def node_right_tree(self):
        return self._right_tree

    @node_right_tree.setter
    def node_right_tree(self, new_ptr):
        self._right_tree = new_ptr

    @property
    def node_black_color(self):
        return self._black

    @node_black_color.setter
    def node_black_color(self, new_color):
        self._black = new_color

    @property
    def node_value(self):
        return self._value

    @node_value.setter
    def node_value(self, new_value):
        self._value = new_value

    @property
    def node_parent(self):
        return self._parent_tree

    @node_parent.setter
    def node_parent(self, new_val):
        self._parent_tree = new_val

    @property
    def is_left_child(self):
        return self._is_left_child

    @is_left_child.setter
    def is_left_child(self, new_value):
        self._is_left_child = new_value


class RedBlackTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        self.black_node_count = 0

    def biuld_from_list(self, list_of_data):
        for i in list_of_data:
            self.create_tree(self.root, i)

    def create_tree(self, ptr, e):
        node = Node(e)
        if self.root is None:
            self.root = node
            self.root.node_black_color = True
            self.size += 1
            return self.root
        else:
            if e == ptr.node_value:
                print(f'Element {e} is already in the tree!')
                return
            if e > ptr.node_value:
                if ptr.node_right_tree is None:
                    ptr.node_right_tree = node
                    node.node_parent = ptr
                    node.is_left_child = False
                    self.check_color(node)
                    self.size += 1
                    return node
                else:
                    while ptr.node_right_tree is not None:
                        ptr = ptr.node_right_tree
                    ptr.node_right_tree = node
                    node.node_parent = ptr
                    node.is_left_child = False
                    self.check_color(node)
                    self.size += 1
                    return node
            else:
                if ptr.node_left_tree is None:
                    ptr.node_left_tree = node
                    node.node_parent = ptr
                    node.is_left_child = True
                    self.check_color(node)
                    self.size += 1
                    return node
                else:
                    while ptr.node_left_tree is not None:
                        ptr = ptr.node_left_tree
                    ptr.node_left_tree = node
                    node.node_parent = ptr
                    node.is_left_child = True
                    self.check_color(node)
                    self.size += 1
                    return node

    def check_color(self, ptr) -> 'ptr is node':
        if ptr is self.root:
            self.root.node_black_color = True
            return
        else:
            if ptr.node_black_color is False and ptr.node_parent.node_black_color is False:
                # print(f'{ptr.node_value} is Red and its parent {ptr.node_parent.node_value} is Red')
                # print(f'correcting the tree...')
                self.correct_tree(ptr)
        self.check_color(ptr.node_parent)

    def correct_tree(self, ptr):
        if ptr.node_parent.is_left_child:
            if ptr.node_parent.node_parent.node_right_tree is None \
                    or ptr.node_parent.node_parent.node_right_tree.node_black_color is True:
                # print('parent_parent_right_tree is None or parent_parent_right_tree_color is Black')
                # print('doing rotation...')
                return self.rotate(ptr)
            if ptr.node_parent.node_parent.node_right_tree is not None:
                # print('doing recoloring')
                ptr.node_parent.node_parent.node_right_tree.node_black_color = True
            ptr.node_parent.node_parent.node_black_color = False
            ptr.node_parent.node_black_color = True
            return
        else:
            if ptr.node_parent.node_parent.node_left_tree is None \
                    or ptr.node_parent.node_parent.node_left_tree.node_black_color is True:
                # print('parent_parent_left_tree is None or parent_parent_left_tree_color is Black')
                # print('doing rotation...')
                return self.rotate(ptr)
            if ptr.node_parent.node_parent.node_left_tree is not None:
                # print('doing recoloring')
                ptr.node_parent.node_parent.node_left_tree.node_black_color = True
            ptr.node_parent.node_parent.node_black_color = False
            ptr.node_parent.node_black_color = True
            return

    def rotate(self, ptr):
        if ptr.is_left_child:
            if ptr.node_parent.is_left_child:
                self.left_rotation(ptr.node_parent.node_parent)
                ptr.node_black_color = False
                ptr.node_parent.node_black_color = True
                if ptr.node_parent.node_right_tree is not None:
                    ptr.node_parent.node_right_tree.node_black_color = False
                return
            else:
                self.right_left_rotation(ptr.node_parent.node_parent)
                ptr.node_black_color = True
                ptr.node_right_tree.node_black_color = False
                ptr.node_left_tree.node_black_color = False
                return
        else:
            if ptr.is_left_child is False:
                if ptr.node_parent.is_left_child is False:
                    self.right_rotation(ptr.node_parent.node_parent)
                    ptr.node_black_color = False
                    ptr.node_parent.node_black_color = True
                    if ptr.node_parent.node_left_tree is not None:
                        ptr.node_parent.node_left_tree.node_black_color = False
                    return
                else:
                    self.left_right_rotation(ptr.node_parent.node_parent)
                    ptr.node_black_color = True
                    ptr.node_left_tree.node_black_color = False
                    ptr.node_right_tree.node_black_color = False
                    return

    def left_rotation(self, ptr):
        # print('doing left rotation')
        temp = ptr.node_left_tree
        ptr.node_left_tree = temp.node_right_tree
        if temp.node_right_tree is None:
            temp.node_right_tree = ptr
        else:
            ptr.node_left_tree.node_parent = ptr
            temp.node_right_tree = ptr
            ptr.node_left_tree.is_left_child = True
        if ptr.node_parent is None:
            temp.node_parent = None
            ptr.node_parent = temp
            temp.is_left_child = False
            self.root = temp
            return temp
        else:
            if ptr.is_left_child:
                temp.node_parent = ptr.node_parent
                temp.node_parent.node_left_tree = temp
                temp.is_left_child = True
                ptr.is_left_child = False
                ptr.node_parent = temp
                return temp
            else:
                temp.node_parent = ptr.node_parent
                temp.node_parent.node_right_tree = temp
                temp.is_left_child = False
                ptr.is_left_child = False
                ptr.node_parent = temp
                return temp

    def right_rotation(self, ptr):
        # print('doing right rotation')
        temp = ptr.node_right_tree
        ptr.node_right_tree = temp.node_left_tree
        if temp.node_left_tree is None:
            temp.node_left_tree = ptr
        else:
            ptr.node_right_tree.node_parent = ptr
            temp.node_left_tree = ptr
            ptr.node_right_tree.is_left_child = False
        if ptr.node_parent is None:
            temp.node_parent = None
            ptr.node_parent = temp
            temp.is_left_child = False
            self.root = temp
            ptr.is_left_child = True
            return temp
        else:
            if ptr.is_left_child:
                temp.node_parent = ptr.node_parent
                temp.node_parent.node_left_tree = temp
                temp.is_left_child = True
                ptr.is_left_child = True
                ptr.node_parent = temp
                return temp
            else:
                temp.node_parent = ptr.node_parent
                temp.node_parent.node_right_tree = temp
                temp.is_left_child = False
                ptr.is_left_child = True
                ptr.node_parent = temp
                return temp

    def left_right_rotation(self, ptr):
        # print('doing left-right rotation')
        temp_p = ptr.node_left_tree
        temp_c = temp_p.node_right_tree
        ptr.node_left_tree = temp_c.node_right_tree
        temp_p.node_right_tree = temp_c.node_left_tree
        if ptr.node_left_tree is None:
            temp_c.node_right_tree = ptr
        else:
            ptr.node_left_tree.node_parent = ptr
            temp_c.node_right_tree = ptr
            ptr.node_left_tree.is_left_child = True
        if temp_p.node_right_tree is None:
            temp_c.node_left_tree = temp_p
            temp_p.node_parent = temp_c
        else:
            temp_p.node_right_tree.node_parent = temp_p
            temp_c.node_left_tree = temp_p
            temp_p.node_parent = temp_c
            temp_p.is_left_child = True
            temp_p.node_right_tree.is_left_child = False
        if ptr.node_parent is None:
            ptr.node_parent = temp_c
            self.root = temp_c
            temp_c.node_parent = None
            ptr.is_left_child = False
            return temp_c
        else:
            if ptr.is_left_child:
                temp_c.node_parent = ptr.node_parent
                temp_c.node_parent.node_left_tree = temp_c
                temp_c.is_left_child = True
                ptr.node_parent = temp_c
                ptr.is_left_child = False
                return temp_c
            else:
                temp_c.node_parent = ptr.node_parent
                temp_c.node_parent.node_right_tree = temp_c
                temp_c.is_left_child = False
                ptr.node_parent = temp_c
                ptr.is_left_child = False
                return temp_c

    def right_left_rotation(self, ptr):
        # print('doing right-left rotation')
        temp_p = ptr.node_right_tree
        temp_c = temp_p.node_left_tree
        ptr.node_right_tree = temp_c.node_left_tree
        temp_p.node_left_tree = temp_c.node_right_tree
        if ptr.node_right_tree is None:
            temp_c.node_left_tree = ptr
        else:
            ptr.node_right_tree.node_parent = ptr
            temp_c.node_left_tree = ptr
            ptr.node_right_tree.is_left_child = False
            temp_c.node_left_tree.is_left_child = True
        if temp_p.node_left_tree is None:
            temp_c.node_right_tree = temp_p
            temp_p.node_parent = temp_c
        else:
            temp_p.node_left_tree.node_parent = temp_p
            temp_c.node_right_tree = temp_p
            temp_p.node_parent = temp_c
            temp_p.is_left_child = False
            temp_p.node_left_tree.is_left_child = True
        if ptr.node_parent is None:
            ptr.node_parent = temp_c
            self.root = temp_c
            ptr.is_left_child = True
            temp_c.is_left_child = False
            temp_c.node_parent = None
            return temp_c
        else:
            if ptr.is_left_child:
                temp_c.node_parent = ptr.node_parent
                temp_c.node_parent.node_left_tree = temp_c
                temp_c.is_left_child = True
                ptr.node_parent = temp_c
                ptr.is_left_child = True
                return temp_c
            else:
                temp_c.node_parent = ptr.node_parent
                temp_c.node_parent.node_right_tree = temp_c
                temp_c.is_left_child = False
                ptr.node_parent = temp_c
                ptr.is_left_child = True
                return temp_c

    def find_element(self, ptr, e):
        if ptr is not None:
            if e == ptr.node_value:
                return ptr.node_data
            elif e < ptr.node_value:
                self.find_element(ptr.node_left_tree, e)
            else:
                self.find_element(ptr.node_right_tree, e)
        else:
            print()
            print(f"""Element {e} is {'not found'.upper()} in the tree""")
            return False

    def remove_element(self, ptr, e):
        if ptr is None:
            # print(f"""Element {e} is {'not'.upper()} found in the tree""")
            return ptr
        else:
            if ptr.node_left_tree is not None:
                ptr.node_left_tree = self.remove_element(ptr.node_left_tree, e)
            if ptr.node_value == e:
                temp = ptr.node_parent
                if ptr.node_left_tree is None and ptr.node_right_tree is None:
                    ptr.node_parent = None
                    if temp is None:
                        ptr = temp
                        self.root = ptr
                        print(f"""Element {e} was deleted from the tree""")
                        return ptr
                    else:
                        if ptr.is_left_child:
                            temp.node_left_tree = None
                            print(f"""Element {e} was deleted from the tree""")
                            ptr = temp.node_left_tree
                            self.check_color(temp)
                            return ptr
                        else:
                            temp.node_right_tree = None
                            print(f"""Element {e} was deleted from the tree""")
                            ptr = temp.node_right_tree
                            self.check_color(temp)
                            return ptr
                elif ptr.node_left_tree is not None and ptr.node_right_tree is None:
                    ptr.node_left_tree.node_parent = temp
                    if temp is None:
                        temp_root = ptr.node_left_tree
                        ptr.node_left_tree = None
                        self.root = temp_root
                        print(f"""Element {e} was deleted from the tree""")
                        self.check_color(temp_root)
                        return temp_root
                    else:
                        if ptr.is_left_child:
                            ptr.node_parent = None
                            temp.node_left_tree = ptr.node_left_tree
                            ptr.node_left_tree = None
                            print(f"""Element {e} was deleted from the tree""")
                            self.check_color(temp.node_left_tree)
                            return temp.node_left_tree
                        else:
                            ptr.node_parent = None
                            temp.node_right_tree = ptr.node_left_tree
                            ptr.node_left_tree = None
                            print(f"""Element {e} was deleted from the tree""")
                            self.check_color(temp.node_right_tree)
                            return temp.node_right_tree
                elif ptr.node_left_tree is None and ptr.node_right_tree is not None:
                    ptr.node_right_tree.node_parent = temp
                    if temp is None:
                        temp_root = ptr.node_right_tree
                        ptr.node_right_tree = None
                        self.root = temp_root
                        print(f"""Element {e} was deleted from the tree""")
                        self.check_color(temp_root)
                        return temp_root
                    else:
                        if ptr.is_left_child:
                            ptr.node_parent = None
                            temp.node_left_tree = ptr.node_right_tree
                            ptr.node_right_tree = None
                            print(f"""Element {e} was deleted from the tree""")
                            self.check_color(temp.node_left_tree)
                            return temp.node_left_tree
                        else:
                            ptr.node_parent = None
                            temp.node_right_tree = ptr.node_right_tree
                            ptr.node_right_tree = None
                            print(f"""Element {e} was deleted from the tree""")
                            self.check_color(temp.node_right_tree)
                            return temp.node_right_tree
                elif ptr.node_left_tree is not None and ptr.node_right_tree is not None:
                    temp = self.find_greatest(ptr.node_left_tree)
                    ptr.node_value, temp.node_value = temp.node_value, ptr.node_value
                    ptr.node_left_tree = self.remove_element(ptr.node_left_tree, e)
            if ptr.node_right_tree is not None:
                ptr.node_right_tree = self.remove_element(ptr.node_right_tree, e)
        return ptr

    def find_greatest(self, ptr):
        if ptr is None:
            return None
        else:
            if ptr.node_right_tree is not None:
                return self.find_greatest(ptr.node_right_tree)
        return ptr

    def height_of_tree(self, ptr):
        if ptr is None:
            return 0
        else:
            height_left_tree = 1 + self.height_of_tree(ptr.node_left_tree)
            height_right_tree = 1 + self.height_of_tree(ptr.node_right_tree)
            return max(height_left_tree, height_right_tree)

    def final_height(self):
        if self.root is None:
            return 0
        height = (self.height_of_tree(self.root)) - 1
        print('The height of the tree is', height)
        return height

    def number_of_black_nodes(self, ptr):
        if ptr is None:
            return 1
        self.number_of_black_nodes(ptr.node_left_tree)
        self.number_of_black_nodes(ptr.node_right_tree)
        if ptr.node_black_color:
            self.black_node_count += 1
        return self.black_node_count

    def number_of_nodes_in_tree(self):
        if self.root is None:
            return 0
        else:
            print(f'Size of tree is {self.size}')
            return self.size

    def display_in_order(self, ptr):
        if ptr is not None:
            self.display_in_order(ptr.node_left_tree)
            print(ptr.node_value, ptr.node_black_color, end='\n')
            self.display_in_order(ptr.node_right_tree)

    def insert(self, obj):
        pass

    def search(self, key):
        pass