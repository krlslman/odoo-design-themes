/** @odoo-module */

/* burası henüz eklemiyor */
import wTourUtils from 'website.tour_utils';

wTourUtils.registerThemeHomepageTour("codequarters_tour", [
    wTourUtils.assertCssVariable('--color-palettes-name', '"codequarters-1"'),
    wTourUtils.dragNDrop(snippets[0], 'top'),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1], 'top'),
    wTourUtils.dragNDrop(snippets[2], 'top'),
    wTourUtils.dragNDrop(snippets[3], 'top'),
    wTourUtils.dragNDrop(snippets[4], 'top'),
    wTourUtils.dragNDrop(snippets[5], 'top'),
]);











