from nodes.textnode import TextNode,TextType
import shutil
import os
from functions.md_helper_functions import *

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

def generate_page(from_path: str,template_path: str,dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    abs_from_path = os.path.abspath(from_path)
    abs_template_path = os.path.abspath(template_path)
    abs_dest_path = os.path.abspath(dest_path)
    with open(abs_from_path) as f:
        markdown = f.read()
    f.close()
    with open(abs_template_path) as f:
        template = f.read()
    f.close()
    
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    title_updated = template.replace(r"{{ Title }}",title)
    finalized = title_updated.replace(r"{{ Content }}",html)

    with open(abs_dest_path,"w") as fw:
        fw.write(finalized)
    fw.close()

def main():
    static_to_public("./static","./public")
    generate_page("./content/index.md","template.html","./public/index.html")


main()
