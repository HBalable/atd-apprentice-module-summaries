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
    #print images

    extras = (
        "--highlight-style tango "
        "--number-sections "
        "--table-of-contents "
        "--toc-depth 2 "
        #"-s "
    )

    opt = raw_input("1 md -->md + Shrink Images\n2 md_compiled-->tex  + Run Fixes\n3 tex_compiled-->pdf\n0 Run All\n>>> ")
    if opt=="1" or opt=="0":
        ffmpeg_cmd = 'ffmpeg -y -i ./images_orig/{0} -vf "scale=\'min(600,iw)\':-1" "./images/{1}.png" -sws_flags bilinear'
        for image in images:
            os.popen(ffmpeg_cmd.format(image, image.split(".")[-2]))

        print "Starting pandoc commands:"
        print "{0}\n{1}\n{0}".format("_"*20,"\n".join(units))
        
        # -fmarkdown-implicit_figures
        full_cmd = pandoc_cmd(units, "md", "md", "--wrap=none ")
        print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
        os.popen(full_cmd)
        print "##### SHELL CMD ENDED #####"

    if opt=="2" or opt=="0":
        full_cmd = pandoc_cmd(["out"], "md", "tex", "--wrap=none")
        print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
        os.popen(full_cmd)
        page_breaks("./tex/out.tex")
        print "##### SHELL CMD ENDED #####"

    if opt=="3" or opt=="0":
        # --template ./tex/template.tex
        full_cmd = pandoc_cmd(["out"], "tex", "pdf", extras + '  -V "geometry:margin=2.54cm" -V "fontsize:12pt" ')
        print "##### RUNNING SHELL CMD #####\n{0}\n#####".format(full_cmd)
        os.popen(full_cmd)
        print "##### SHELL CMD ENDED #####"

def page_breaks(path):
    lines = []
    with open(path, "r+") as fp:
        print "Running fix and post-scripts.."
        # preppend titles to tex
        titles = [
            "\\title{ATD Apprentice Modules}",
            "\\author{Hasan Balable}",
            "\\date{March 2018}"
        ]
        lines = fp.readlines()
        lines = titles + lines
        line_enum = ((i, line) for i, line in enumerate(lines))
        # page break before each section
        for i, line in line_enum:
            if line.startswith("\section"):
                print "page break fix from {0}".format(path)
                lines.insert(i-1, "\\pagebreak")
                line_enum.next()
                continue
        line_enum = ((i, line) for i, line in enumerate(lines))
        for i, line in line_enum:
            if line.startswith("\centering"):
                lines[i] = ""
        for match_string, offset in (
            ("\\begin{longtable}", 0),
            (">>> touch example_file", -1),
            (">>> def get_factorial(value):", -1),
            ("~ >>> tree .", -1),
            ("~/my_folder >>> tar -czf", -1),
            (">>> git push origin example", -1),
            ("~ >>> cat Downloads/file1.txt | grep six", -1),
        ):
            lines = preppend_page_break(match_string, lines, offset)

    with open(path, "r+") as fp:
        fp.truncate()
        fp.writelines(lines)

def preppend_page_break(start_of_line, lines, offset=0):
    line_enum = ((i, line) for i, line in enumerate(lines))
    for i, line in line_enum:
        # pagebreak before initial table (cosmetic fix)
        if line.startswith(start_of_line):
            print "adding cosmetic \\pagebreak on line {0} matching pattern \'{1}\'".format(
                i+offset,start_of_line
            )
            lines = lines[:i+offset] + ["\n", "\\pagebreak\n", "\n"] + lines[i+offset:]
            break
    return lines

if __name__=="__main__":
    main()
