from pptx import Presentation
from pptx.util import Inches
import os
from typing import List
from controller.setting import Setting


class ImageEmbedPptx:

    PPTX_FILENAME = 'Template_Report.pptx'
    LIST_IMAGE_FILEPATHS: List[str] = Setting.LIST_FIGURE_IMAGES

    def export_figures_to_pptx(self) -> None:
        # check file existence
        if not os.path.exists(self.PPTX_FILENAME):
            print(f'File {self.PPTX_FILENAME} not found.')
            return
        try:
            ppt_output = Presentation(self.PPTX_FILENAME)
        except:
            print(f'Failed to open Template file {self.PPTX_FILENAME} for exporting image to.')
            return

        # Push images to PPT file
        slide_layout = ppt_output.slide_layouts[0]
        max_slides = len(self.ppt_output.slides)
        i = 0
        for img in self.LIST_IMAGE_FILEPATHS:
            current_slide = ppt_output.slides[i]
            plot_img = current_slide.shapes.add_picture(img, Inches(0.40), Inches(4.85), width=Inches(5.30))

            # Send the figures to the back
            ref_element = current_slide.shapes[0]._element
            ref_element.addprevious(plot_img._element)

            # Go to next slide in PPTX file
            if i >= (max_slides - 1):
                max_slides += 1
                # add one more slide

            i += 1

        # Save the PPT
        ppt_output.save('Boxplot Report.pptx')
