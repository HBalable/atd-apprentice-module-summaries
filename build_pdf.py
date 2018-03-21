#!/usr/bin/env python2.7
def main():
    import os
    fp_iter = os.walk(".")

    images = []
    units = []
    for i in fp_iter:
        if i[0] == "./md":
            units = [f for f in i[2] if f.startswith("unit_") and f.endswith("md")]
            continue
        if i[0] == "./images_orig":
            images = i[2]
    print units
    print images

    ffmpeg_cmd = 'ffmpeg -y -i ./images_orig/{0} -vf "scale=\'min(500,iw)\':-1" "./images/{1}.png" -sws_flags bilinear'
    for image in images:
        os.popen(ffmpeg_cmd.format(image, image.split(".")[-2]))

    # pandoc_cmd = "pandoc -i {0} -o pdf/{1}.pdf"
    target_type="tex"
    pandoc_cmd = lambda fp, fn:(
        "../../scripts/pandoc -i ./md/{0} -o {2}/{1}.{2}"
        " --webtex"
        ).format(fp,fn,target_type)

    print "writing out"
    for unit in units:
        unit_name =  unit.split(".")[-2]
        full_cmd = pandoc_cmd(unit, unit_name)
        print full_cmd
        os.popen(full_cmd)
        fix_tex("tex/{0}.tex".format(unit_name))

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