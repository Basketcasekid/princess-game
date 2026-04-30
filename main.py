def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    _3.set_position(randint(0, scene.screen_width()),
        randint(0, scene.screen_height()))
    info.start_countdown(5)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

_3: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
    """))
scene.set_background_color(3)
_1 = sprites.create(img("""
        . . . . . f f 4 4 f f . . . . .
        . . . . f 5 4 5 5 4 5 f . . . .
        . . . f e 4 5 5 5 5 4 e f . . .
        . . f b 3 e 4 4 4 4 e 3 b f . .
        . . f 3 3 3 3 3 3 3 3 3 3 f . .
        . f 3 3 e b 3 e e 3 b e 3 3 f .
        . f 3 3 f f e e e e f f 3 3 f .
        . f b b f b f e e f b f b b f .
        . f b b e 1 f 4 4 f 1 e b b f .
        f f b b f 4 4 4 4 4 4 f b b f f
        f b b f f f e e e e f f f b b f
        . f e e f b d d d d b f e e f .
        . . e 4 c d d d d d d c 4 e . .
        . . e f b d b d b d b b f e . .
        . . . f f 1 d 1 d 1 d f f . . .
        . . . . . f f b b f f . . . . .
        """),
    SpriteKind.player)
_3 = sprites.create(img("""
        . . . . . . . . . . b b b . . .
        . . . . . . . . b e e 3 3 b . .
        . . . . . . b b e 3 2 e 3 a . .
        . . . . b b 3 3 e 2 2 e 3 3 a .
        . . b b 3 3 3 3 3 e e 3 3 3 a .
        b b 3 3 3 3 3 3 3 3 3 3 3 3 3 a
        b 3 3 3 d d d d 3 3 3 3 3 d d a
        b b b b b b b 3 d d d d d d 3 a
        b d 5 5 5 5 d b b b a a a a a a
        b 3 d d 5 5 5 5 5 5 5 d d d d a
        b 3 3 3 3 3 3 d 5 5 5 d d d d a
        b 3 d 5 5 5 3 3 3 3 3 3 b b b a
        b b b 3 d 5 5 5 5 5 5 5 d d b a
        . . . b b b 3 d 5 5 5 5 d d 3 a
        . . . . . . b b b b 3 d d d b a
        . . . . . . . . . . b b b a a .
        """),
    SpriteKind.food)
controller.move_sprite(_1)
_2 = sprites.create(img("""
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        """),
    SpriteKind.enemy)
_2.follow(_1, 25)
_1.set_kind(SpriteKind.player)
_2.set_kind(SpriteKind.enemy)
info.set_life(1)
tiles.place_on_tile(_2, tiles.get_tile_location(8, 8))
_1.set_stay_in_screen(True)
_2.set_stay_in_screen(True)
_3.set_stay_in_screen(True)