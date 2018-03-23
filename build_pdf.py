#!/usr/bin/env python2.7

def pandoc_cmd(sources, source_type, target_type="tex", extra=""):
    get_path = lambda name, tp: "./{1}/{0}.{1}".format(name,tp)
    sources = [get_path(src, source_type) for src in sources]
    return (
    "../../scripts/pandoc -i {0} --katex -o {1} {2}"
    ).format(" ".join(sources),get_path("out", target_type),extra)


def main():
    import os
    fp_iter = os.walk(".")

    images = []
    
    units = [
        "unit_1_pipeline",
        "unit_2_data_management",
        "unit_3_render_management",
        "unit_4_databases",
        "unit_5_project_organisation",
        "unit_6_maths",
        "unit_7_software_design",
        "unit_8_scripting",
        "unit_9_computing",
        "unit_10_vfx_craft",
        "unit_11_linux"
    ]

    for i in fp_iter:
        if i[0] == "./images_orig":
            images = i[2]
    print images

    extras = (
        "--highlight-style tango "
        "--number-sections "
        "--table-of-contents "
        "--toc-depth 2 "
        "-s "
    )

    opt = raw_input("1 md -->md\n2 md_compiled-->tex\n3 tex_compiled-->pdf\nall=0\n>>>")
    if opt=="1" or opt=="0":
        ffmpeg_cmd = 'ffmpeg -y -i ./images_orig/{0} -vf "scale=\'min(500,iw)\':-1" "./images/{1}.png" -sws_flags bilinear'
        for image in images:
            os.popen(ffmpeg_cmd.format(image, image.split(".")[-2]))

        print "writing out"
        print "_________________________________ \n" + "\n".join(units)
        
        # -fmarkdown-implicit_figures
        full_cmd = pandoc_cmd(units, "md", "md", "--wrap=none -fmarkdown-implicit_figures")
        print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
        os.popen(full_cmd)
        print "##########"

    if opt=="2" or opt=="0":
        full_cmd = pandoc_cmd(["out"], "md", "tex", "--wrap=none")
        print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
        os.popen(full_cmd)
        print "##########"

    if opt=="3" or opt=="0":
        full_cmd = pandoc_cmd(["out"], "tex", "pdf", extras)
        print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
        os.popen(full_cmd)
        print "##########"

    # full_cmd = pandoc_cmd(unit_name, "md", "tex", extras)
    # print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
    # os.popen(full_cmd)
    # print "##########"

    # fix_tex("tex/{0}.tex".format(unit_name))
    
    # full_cmd = pandoc_cmd(unit_name, "pdf", "tex")
    # print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
    # os.popen(full_cmd)
    # print "##########"

def fix_tex(path):
    lines = []
    with open(path, "r+") as fp:
        print "running fix"
        lines = fp.readlines()
        line_enum = ((i, line) for i, line in enumerate(lines))
        for i, line in line_enum:
            if line.startswith("\includegraphics"):
                print "fixing image from {0}".format(path)
                lines[i] = "    " + line
                lines.insert(i-1, "\\begin{center}")
                lines.insert(i+2, "\\end{center}")
                line_enum.next()
                continue
    with open(path, "r+") as fp:
        fp.truncate()
        fp.writelines(lines)

if __name__=="__main__":
    main()
    #fix_tex("tex/unit_10_vfx_craft.tex")

# -fmarkdown-implicit_figures

"""
unit_1_pipeline
unit_2_data_management
unit_3_render_management
unit_4_databases
unit_5_project_organisation
unit_6_maths
unit_7_software_design
unit_8_scripting
unit_9_computing
unit_10_vfx_craft
unit_11_linux
"""