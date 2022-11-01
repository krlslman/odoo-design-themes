# -*- coding: utf-8 -*-
#############################################################################
#
#    KOD MERKEZİ Yazılım ve İnternet Hizmetleri Eğitim Danışmanlık LTD. Şti.
#
#    Copyright (C) 2021-TODAY Code Quarters(<https://www.codequarters.com>)
#    Author: Cybrosys Techno Solutions(<https://www.quarters.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'CQ Theme',
    'description': 'CQ Theme for website',
    'summary': 'CQ-Theme',
    'version': '14.0.1',
    'author': 'Codequarters',
    'company': 'Codequarters',
    'maintainer': 'Codequarters',
    'website': 'https://www.codequarters.com',
    'category': 'Theme/website',
    'depends': [
        'theme_common', "website", "muk_website_grid",
    ],
    'data': [
        'data/ir_asset.xml',
        # 'views/images.xml',
        'views/snippets/header.xml',
        'views/snippets/footer.xml',
        'views/customizations.xml',
        'views/home_page.xml'

    ],
    'images': [
    ],
    'assets': {

        'website.assets_editor': [
            'theme_cq/static/src/js/tour.js',
        ],
        'web.assets_frontend': [
            'theme_cq/static/src/scss/style.scss',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
}
