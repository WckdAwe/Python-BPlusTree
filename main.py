"""
The following program is an assignment for the subject Databases II.

Educational use only.

Developed by:
 - Vasileios Dimitriadis (WICKEÐ || https://github.com/wckdawe)
 - Taxiarchis Kouskouras (TheNotoriousCS || https://github.com/TheNotoriousCS)

INFS255, Computer Science, University of Thessaly, Greece.
"""
import sys
import os
from bplustree_for_uni import BPlusTree, LeafNode

BRANCHING_FACTOR = 5


def create_index(input_file: str, index_file: str):
    read_count, insert_count = 0, 0
    if len(input_file) > 256:
        print('Input file name is too big (must be less than 256 chars)')
        return False

    if os.path.dirname(input_file) != os.path.dirname(index_file):
        print('Input and Index file must be saved into the same directory')
        return False

    bplustree = BPlusTree(order=BRANCHING_FACTOR)
    try:
        print('Reading file', input_file)
        with open(input_file) as file:
            offset = int(file.tell())
            line = file.readline()
            while line:
                key, value = line.split(" ", 1)
                key = int(key)
                bplustree.insert(key, offset)
                read_count += 1

                offset = file.tell()
                line = file.readline()

        print('Creating file', index_file)
        with open(index_file, 'wb+') as file:
            node = bplustree.get_leftmost_leaf()
            if not node:
                return None
            input_file = os.path.basename(input_file)
            encoded_file = input_file.ljust(256).encode('ascii')

            file.write(encoded_file)
            while node:
                for i in range(len(node.keys)):
                    key = int(node.keys[i])
                    for value in node.values[i]:
                        value = int(value)
                        file.write(key.to_bytes(8, byteorder='big'))
                        file.write(value.to_bytes(8, byteorder='big'))
                        insert_count += 1

                node = node.next_leaf
        print('Records read:', read_count)
        print('Records inserted:', insert_count)

        print('INDEX FILE CREATED.')
    except FileNotFoundError:
        print('Input file \'{}\' not found.'.format(input_file))
    except TypeError:
        raise


def find_by_reconstructing(index_file: str, index_id: int):
    bplustree = BPlusTree(order=BRANCHING_FACTOR)
    try:
        print('Reading index file:', index_file)
        with open(index_file, 'rb') as file:

            if not os.path.dirname(index_file):
                input_file_chk = str(file.read(256).decode('utf-8')).rstrip()
            else:
                input_file_chk = os.path.dirname(index_file) + '/' + str(file.read(256).decode('utf-8')).rstrip()

            print('Index belongs to:', input_file_chk)
            print('Index exists:', os.path.isfile(input_file_chk))
            print('Reconstructing B+ Tree')  # This method is bad speed-wise, but will do the job for this exercise.

            while True:
                key = int.from_bytes(file.read(8), byteorder='big')
                value = int.from_bytes(file.read(8), byteorder='big')

                if not key:
                    break
                bplustree.insert(key, value)

        offsets = bplustree.retrieve(index_id)
        if not offsets:
            print('Index "', index_id, '" NOT FOUND.')
            return bplustree, None, input_file_chk
        else:
            print('Index FOUND at offsets: ', offsets)
            with open(input_file_chk, 'r') as file:
                for offset in offsets:
                    file.seek(offset)
                    print(file.readline(), end='')
            print()
            return bplustree, offsets, input_file_chk
    except FileNotFoundError as error:
        print(error)
        exit(0)
    except TypeError:
        raise
        exit(0)


def insert(index_file: str, data: str):
    try:
        key, value = data.split(" ", 1)
        if not value or len(key) > 14:
            raise ValueError
        key = int(key)
    except ValueError:
        print('Data must be like "index_id <data>", where index_id is an integer <= 14 length')
        exit(0)

    bplustree, offsets, input_file = find_by_reconstructing(index_file, key)
    if offsets is not None:
        print('INSERT FAILED (Index already exists)')
        return
    else:
        print('Inserting data,', str(key).zfill(14) + ' ' + value)

        with open(input_file, 'a') as file:
            file.write('\n')
            offset = file.tell()
            file.write(str(key).zfill(14) + ' ' + value)
            bplustree.insert(key, offset)

        with open(index_file, 'wb+') as file:
            node = bplustree.get_leftmost_leaf()
            if not node:
                return None
            input_file = os.path.basename(input_file)
            encoded_file = input_file.ljust(256).encode('ascii')

            file.write(encoded_file)
            while node:
                for i in range(len(node.keys)):
                    key = int(node.keys[i])
                    for value in node.values[i]:
                        value = int(value)
                        file.write(key.to_bytes(8, byteorder='big'))
                        file.write(value.to_bytes(8, byteorder='big'))

                node = node.next_leaf
            print('INSERT SUCCESS')


def list_func(index_file: str, search_key: int, count: int):
    bplustree = BPlusTree(order=BRANCHING_FACTOR)
    if count <= 0:
        print('count must be greater than 0!')
        exit(0)
    try:
        print('Reading index file:', index_file)
        with open(index_file, 'rb') as file:

            if not os.path.dirname(index_file):
                input_file_chk = str(file.read(256).decode('utf-8')).rstrip()
            else:
                input_file_chk = os.path.dirname(index_file) + '/' + str(file.read(256).decode('utf-8')).rstrip()

            print('Index belongs to:', input_file_chk)
            print('Index exists:', os.path.isfile(input_file_chk))
            print('Reconstructing B+ Tree')  # This method is bad speed-wise, but will do the job for this exercise.

            while True:
                key = int.from_bytes(file.read(8), byteorder='big')
                value = int.from_bytes(file.read(8), byteorder='big')

                if not key:
                    break
                bplustree.insert(key, value)

        node = bplustree.root

        while not isinstance(node, LeafNode):
            node, index = bplustree._find(node, search_key)

        if search_key in node.keys:
            print('Search key not found. Searching for next greater!')

        start = 0
        for i, item in enumerate(node.keys):
            if item >= search_key:
                start = i

        offsets = []
        while count >= 0:
            if start == len(node.keys):
                start = 0
                node = node.next_leaf
                if not node:
                    print('Reached the end of the tree. Printing available results.')
                    break
            for offset in node.values[start]:
                offsets.append(offset)
                count -= 1
                if count < 0:
                    break

            start += 1
        with open(input_file_chk, 'r') as file:
            for offset in offsets:
                file.seek(offset)
                print('('+str(offset)+') | ' + file.readline().rstrip('\n'), end='\n')
            print()
    except FileNotFoundError as error:
        print(error)
        exit(0)
    except TypeError:
        raise
        exit


def delete_func(index_file: str, search_key: int):
    bplustree = BPlusTree(order=BRANCHING_FACTOR)
    bplustree_new = BPlusTree(order=BRANCHING_FACTOR)

    try:
        print('Reading index file:', index_file)
        with open(index_file, 'rb') as file:

            if not os.path.dirname(index_file):
                input_file = str(file.read(256).decode('utf-8')).rstrip()
            else:
                input_file = os.path.dirname(index_file) + '/' + str(file.read(256).decode('utf-8')).rstrip()

            print('Index belongs to:', input_file)
            print('Input exists:', os.path.isfile(input_file))
            print('Reconstructing B+ Tree')  # This method is bad speed-wise, but will do the job for this exercise.

            while True:
                key = int.from_bytes(file.read(8), byteorder='big')
                value = int.from_bytes(file.read(8), byteorder='big')

                if not key:
                    break
                bplustree.insert(key, value)
        offsets = bplustree.retrieve(search_key)
        if not offsets:
            print('This key doesn\'t exist.')
        else:
            offset = int(offsets[0])
            with open(input_file, "r") as f:
                lines = f.readlines()
            count = 0
            with open(input_file, "w") as f:
                deleted = False
                for i, line in enumerate(lines):
                    if count == offset and not deleted:
                        deleted = True
                        print('Deleting:', line.rstrip('\n'), end='\n')
                        continue
                    bplustree_new.insert(line.split(" ", 1)[0], count)
                    if i == len(lines) - 2 and not deleted:
                        count += f.write(line.rstrip('\n'))  # Special case...
                        offset = offset-1
                    else:
                        count += f.write(line)
            bplustree.delete(search_key)  # This contributes only to show the deletion.
            # In practice we create a new B+ Tree.
            # That's because when we delete an element, all the offsets associated
            # after the deleted element need to change.
            # We haven't specified such a function... so... improvise.
            # Plus such a function would be costly. Probably there is a better
            # solution for this problem.
            print('DATA DELETED FROM INPUT FILE')

            with open(index_file, 'wb+') as file:
                node = bplustree_new.get_leftmost_leaf()
                if not node:
                    return None
                input_file = os.path.basename(input_file)
                encoded_file = input_file.ljust(256).encode('ascii')

                file.write(encoded_file)
                while node:
                    for i in range(len(node.keys)):
                        key = int(node.keys[i])
                        for value in node.values[i]:
                            value = int(value)
                            file.write(key.to_bytes(8, byteorder='big'))
                            file.write(value.to_bytes(8, byteorder='big'))

                    node = node.next_leaf
            print('INDEX FILE RE-CREATED')
    except FileNotFoundError as error:
        print(error)
        exit(0)
    except TypeError:
        raise
        exit(0)


def graph(index_file: str):
    bplustree = BPlusTree(order=BRANCHING_FACTOR)
    try:
        print('Reading index file:', index_file)
        with open(index_file, 'rb') as file:
            if not os.path.dirname(index_file):
                input_file_chk = str(file.read(256).decode('utf-8')).rstrip()
            else:
                input_file_chk = os.path.dirname(index_file) + '/' + str(file.read(256).decode('utf-8')).rstrip()

            while True:
                key = int.from_bytes(file.read(8), byteorder='big')
                value = int.from_bytes(file.read(8), byteorder='big')

                if not key:
                    break
                bplustree.insert(key, value)
        bplustree.view_graph(index_file)
    except FileNotFoundError as error:
        print(error)
        exit(0)
    except TypeError:
        raise
        exit(0)


if __name__ == '__main__':
    #  main_menu()
    if len(sys.argv) <= 1:
        print('-create')
        print('-find')
        print('-insert')
        print('-list')
        print('-delete')
        print('-graph')
        exit(0)

    action = sys.argv[1].lower()
    if action == '-create':
        if len(sys.argv) != 4:
            print(sys.argv[0], '-create <input.txt> <index.indx>')
            exit(0)
        create_index(sys.argv[2], sys.argv[3])
    elif action == '-find':
        if len(sys.argv) != 4:
            print(sys.argv[0], '-find <index.indx> index_id')
            exit(0)
        find_by_reconstructing(sys.argv[2], int(sys.argv[3]))
    elif action == '-insert':
        if len(sys.argv) != 4:
            print(sys.argv[0], '-insert <index.indx> "data .."')
            exit(0)
        insert(sys.argv[2], sys.argv[3])
    elif action == '-list':
        if len(sys.argv) != 5:
            print(sys.argv[0], '-list <index.indx> index_id count')
            exit(0)
        list_func(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif action == '-delete':
        if len(sys.argv) != 4:
            print(sys.argv[0], '-delete <index.indx> index_id')
            exit(0)
        delete_func(sys.argv[2], int(sys.argv[3]))
    elif action == '-graph':
        if len(sys.argv) != 3:
            print(sys.argv[0], '-graph <index.indx>')
            exit(0)
        graph(sys.argv[2])
    else:
        print('-create')
        print('-find')
        print('-insert')
        print('-list')
        print('-delete')
        print('-graph')
        exit(0)

