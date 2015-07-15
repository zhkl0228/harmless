from common import *

import pygame

def choose_chess_image(src_img, color):
    src_rect = src_img.get_rect()
    dst_rect = pygame.Rect(0, 0, src_rect.width/2, src_rect.height)
    dst_img = pygame.Surface((dst_rect.width, dst_rect.height), pygame.SRCALPHA, 32).convert_alpha()
    if color == RED:
        dst_img.blit(src_img, (0, 0), dst_rect)
    else:
        dst_img.blit(src_img, (0, 0), dst_rect.move(dst_rect.width, 0))
    return dst_img

class chesssprite(pygame.sprite.DirtySprite):
    def __init__(self, surface, layer=0):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = surface
        self.rect = surface.get_rect()
        self._layer = layer

    def _set_visible(self, val):
        """set the visible value (0 or 1) and makes the sprite dirty"""
        if self._visible != val:
            self._visible = val
            if self.dirty < 2:
                self.dirty = 1

    def set_position(self, x, y):
        if self.rect.topleft != (x, y):
            self.rect.topleft = (x, y)
            self.dirty = 1
        return self

class chesssprite_piece(chesssprite):
    def __init__(self, surface):
        super(chesssprite_piece, self).__init__(surface)
        #self.visible = 0
