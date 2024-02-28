from pptx import Presentation
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE_TYPE
import os
from typing import List
from controller.setting import Setting


class ImageEmbedPptx:

    PPTX_TEMPLATE = 'Template_Report.pptx'
    PPTX_OUTPUT_NAME = 'Report'
    FIXED_TEXT_BOX_SHAPE_HEIGHT = 0.5
    LIST_IMAGE_FILEPATHS: List[str] = Setting.LIST_FIGURE_IMAGES

    def __init__(self):
        # check file existence
        self.pptx: Presentation = None
        if not os.path.exists(self.PPTX_TEMPLATE):
            # print(f'File {self.PPTX_FILENAME} not found.')
            return
        try:
            self.pptx = Presentation(self.PPTX_TEMPLATE)
        except:
            print(f'Failed to open Template file {self.PPTX_TEMPLATE} for exporting image to.')
            return

    def clearAllShapes(self) -> None:
        if self.pptx is None:
            return
        
        for slide in self.pptx.slides:
            # Remove the old figures
            shapes = slide.shapes
            for shape in shapes:
                match shape.shape_type:
                    case MSO_SHAPE_TYPE.GROUP | MSO_SHAPE_TYPE.PICTURE | MSO_SHAPE_TYPE.TABLE:
                        shapes.element.remove(shape.element)


    def exportFigures2PPTX(self) -> None:
        if len(self.LIST_IMAGE_FILEPATHS) == 0:
            return

        # Push images to PPT file
        max_slides = len(self.ppt_output.slides)
        i = 0

        for img in self.LIST_IMAGE_FILEPATHS:
            if i >= max_slides:
                self.pptx.slides.add_slide(self.pptx.layouts[0])
            
            slide_current = self.pptx.slides[i]
            plot_img = slide_current.shapes.add_picture(img, Inches(0.40), Inches(4.85), width=Inches(5.30))

            # Send the figures to the back
            ref_element = slide_current.shapes[0]._element
            ref_element.addprevious(plot_img._element)

            i += 1

        # Save the PPT
        self.pptx.save(self.PPTX_OUTPUT_NAME)
