#!/usr/bin/env python

from lib.core import Powerline
from lib.renderers import SegmentRenderer


class VimSegmentRenderer(SegmentRenderer):
	'''Powerline vim segment renderer.
	'''
	def __init__(self):
		self.hl_groups = {}

	def hl(self, fg=None, bg=None, attr=None):
		'''Highlight a segment.

		If an argument is None, the argument is ignored. If an argument is
		False, the argument is reset to the terminal defaults. If an argument
		is a valid color or attribute, it's added to the vim highlight group.
		'''
		# We don't need to explicitly reset attributes in vim, so skip those calls
		if not attr and not bg and not fg:
			return ''

		if not (fg, bg, attr) in self.hl_groups:
			hl_group = {
				'ctermfg': 'NONE',
				'guifg': 'NONE',
				'ctermbg': 'NONE',
				'guibg': 'NONE',
				'attr': ['NONE'],
				'name': '',
			}

			if fg is not None and fg is not False:
				hl_group['ctermfg'] = fg[0]
				hl_group['guifg'] = fg[1]

			if bg is not None and bg is not False:
				hl_group['ctermbg'] = bg[0]
				hl_group['guibg'] = bg[1]

			if attr:
				hl_group['attr'] = []
				if attr & Powerline.ATTR_BOLD:
					hl_group['attr'].append('bold')
				if attr & Powerline.ATTR_ITALIC:
					hl_group['attr'].append('italic')
				if attr & Powerline.ATTR_UNDERLINE:
					hl_group['attr'].append('underline')

			hl_group['name'] = 'Pl_' + \
				str(hl_group['ctermfg']) + '_' + \
				str(hl_group['guifg']) + '_' + \
				str(hl_group['ctermbg']) + '_' + \
				str(hl_group['guibg']) + '_' + \
				''.join(hl_group['attr'])

			self.hl_groups[(fg, bg, attr)] = hl_group

		return '%#' + self.hl_groups[(fg, bg, attr)]['name'] + '#'
