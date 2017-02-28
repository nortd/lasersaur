
import os

version = "v17.03"

conf = {
    "version":version,
    "subsystems": [
        '1.frame-bottom',
        '2.frame-gantry',
        '3.frame-top',
        '4.frame-door',
        '5.y-cart',
        '6.y-drive',
        '7.x-cart',
        '8.x-drive',
        '9.electronics',
        '10.optics-laser',
        '11.air-assist',
        '12.frame-table',
        '13.door-panels',
        '14.frame-panels',
        # '15.extraction',
    ],
    "blocks": ["blocks"],
    "non_subsystems": ["stencils", "extra", "4.frame-door::frame-door-open", "7.x-cart::x-cart-old"],
    "build_apart":['2.frame-gantry', '4.frame-door', '5.y-cart', '6.y-drive', '7.x-cart', '8.x-drive', '12.frame-table'],
    "left_view": "Left",          #
    "right_view": "Right",        #
    "top_view": "Top",            #
    "bottom_view": "Bottom",      # > all are named views
    "front_view": "Front",        #
    "back_view": "Back",          #
    "persp_view": "for manual",  #
    "outputdir": os.path.join("E:\lasersaur_stuff", "manual"),
    "struct_file": "structure.json",
    "step_file_pat": "step_%s.html",              # %s is step numeral, eg: 2.3

    "step_img_persp": "step.%s.persp.png",     # %s is step numeral, eg: 2.3
    "step_img_top": "step.%s.top.png",     # %s is step numeral, eg: 2.3
    "step_img_front": "step.%s.front.png",     # %s is step numeral, eg: 2.3
    "step_img_right": "step.%s.right.png",     # %s is step numeral, eg: 2.3
    "step_img_width": 1600,

    "step_img_persp_low": "step.%s.persp_low.png",     # %s is step numeral, eg: 2.3
    "step_img_top_low": "step.%s.top_low.png",     # %s is step numeral, eg: 2.3
    "step_img_front_low": "step.%s.front_low.png",     # %s is step numeral, eg: 2.3
    "step_img_right_low": "step.%s.right_low.png",     # %s is step numeral, eg: 2.3
    "step_img_width_low": 420,

    "step_img_persp_thumb": "step.%s.persp_thumb.png",     # %s is step numeral, eg: 2.3
    "step_img_top_thumb": "step.%s.top_thumb.png",     # %s is step numeral, eg: 2.3
    "step_img_front_thumb": "step.%s.front_thumb.png",     # %s is step numeral, eg: 2.3
    "step_img_right_thumb": "step.%s.right_thumb.png",     # %s is step numeral, eg: 2.3
    "step_img_width_thumb": 300,

    "part_img_persp": "part.%s_%s.persp.png",  # %s is step numeral and partkind
    "part_img_top": "part.%s_%s.top.png",  # %s is step numeral and partkind
    "part_img_front": "part.%s_%s.front.png",  # %s is step numeral and partkind
    "part_img_right": "part.%s_%s.right.png",  # %s is step numeral and partkind
    "part_img_width": 400,

    "part_img_persp_thumb": "part.%s_%s.persp_thumb.png",  # %s is step numeral and partkind
    "part_img_top_thumb": "part.%s_%s.top_thumb.png",  # %s is step numeral and partkind
    "part_img_front_thumb": "part.%s_%s.front_thumb.png",  # %s is step numeral and partkind
    "part_img_right_thumb": "part.%s_%s.right_thumb.png",  # %s is step numeral and partkind
    "part_img_width_thumb": 100,

    "main_header": "Lasersaur %s Build Instructions" % (version),

}
