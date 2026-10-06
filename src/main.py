from nodes.textnode import TextNode,TextType
import shutil
import os

def static_to_public(src_dir: str, dest_dir: str):
    abs_src_dir = os.path.abspath(src_dir)
    abs_dest_dir = os.path.abspath(dest_dir)
    if os.path.exists(abs_dest_dir):
        print(f"Deleting directory: {abs_dest_dir}")
        shutil.rmtree(abs_dest_dir)
    os.mkdir(abs_dest_dir) 
    copytree(abs_src_dir,abs_dest_dir)

def copytree(abs_src: str,abs_dst: str):
    src = os.listdir(abs_src)
    for path in src:
        full_src_path = os.path.join(abs_src,path)
        full_dst_path = os.path.join(abs_dst,path)
        if os.path.isfile(full_src_path):
            shutil.copy(full_src_path,full_dst_path)
        elif os.path.isdir(full_src_path):
            os.mkdir(full_dst_path)
            copytree(full_src_path,full_dst_path)

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    static_to_public("./static","./public")


main()
