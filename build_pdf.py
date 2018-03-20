#!/usr/bin/env python2.7
def main():
    import os
    fp_iter = os.walk(".")

    images = []
    units = []
    for i in fp_iter:
        if i[0] == ".":
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
    target_type="pdf"
    pandoc_cmd = lambda fp, fn:(
        "../../scripts/pandoc -i {0} -o {2}/{1}.{2}"
        " --webtex -v"
        ).format(fp,fn,target_type)

    print "writing out"
    for unit in units:
        print unit
        os.popen(pandoc_cmd(unit, unit.split(".")[-2]))

def fix_tex(path):
    with open(path, "rw") as fp:
        lines = fp.readlines()
        for line in lines:
            if line.startswith(""):
                pass

if __name__=="__main__":
    main()

# -fmarkdown-implicit_figures