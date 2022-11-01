# -*- coding: utf-8 -*-
from odoo import models


class ThemeCq(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_cq_post_copy(self, mod):
        self.enable_asset("website.ripple_effect_scss")
        self.enable_asset("website.ripple_effect_js")

        self.disable_view('website.template_header_default')
        self.enable_view('theme_cq.cq_template_header')

        self.disable_view('website.footer_custom')
        self.enable_view('theme_cq.cq_template_footer')

        self.enable_header_off_canvas()
