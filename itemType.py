# encoding: utf-8
from enum import Enum


class ItemType(Enum):
    """
    The enumeration of item types.
    物品枚举类。
    """
    UNKNOWN = 0
    CLOTHING = 1
    DEPRECATED_DIRT_BLOCK = 2
    FLINT = 3
    STICK = 4
    DEPRECATED_WOOD_BLOCK = 5
    FLINT_AXE = 6
    FIINT_SPEAR = 7
    FLINT_PICKAXE = 8
    DOUBLE_TIME = 9
    DEPRECATED_WORKBENCH = 10
    TIME_CRYSTAL = 11
    BASKET = 12
    EMBER = 13
    CHARCOAL = 14
    CAMPFIRE = 15
    FLINT_SPADE = 16
    TORCH = 17
    DEPRECATED_SAND = 18
    BLOCKHEAD = 19
    FOOD = 20
    APPLE = 21
    MANGO = 22
    MAPLE_SEED = 23
    PRICKLY_PEAR = 24
    FLINT_MACHETE = 25
    DEPRECATED_STONE_WORKBENCH = 26
    PINECONE = 27
    CLAY = 28
    DODO_MEAT = 29
    DODO_FEATHER = 30
    COPPER_ORE = 31
    IRON_ORE = 32
    STONE_AXE = 33
    STONE_PICKAXE = 34
    COPPER_INGOT = 35
    TIN_ORE = 36
    TIN_INGOT = 37
    BRONZE_INGOT = 38
    COPPER_SPEAR = 39
    TIN_SPADE = 40
    COPPER_ARROW = 41
    COPPER_BOW_AND_ARROWS = 42
    BRONZE_PICKAXE = 43
    STRING = 44
    CLAY_JUG = 45
    COCONUT = 46
    OIL_LANTERN = 47
    OIL = 48
    BRONZE_MACHETE = 49
    BRONZE_SWORD = 50
    COAL = 51
    DOOR = 52
    LADDER = 53
    FLAX_SEED = 54
    FLAX = 55
    INDIAN_YELLOW = 56
    RED_OCHRE = 57
    WINDOW = 58
    COOKED_DODO_MEAT = 59
    ORANGE = 60
    SUNFLOWER_SEED = 61
    CORN = 62
    BED = 63
    STONE_SPADE = 64
    IRON_INGOT = 65
    IRON_PICKAXE = 66
    IRON_MACHETE = 67
    IRON_SWORD = 68
    TRAPDOOR = 69
    IRON_PICKAXE = 70
    CARROT = 71
    GOLD_INGOT = 72
    GOLD_NUGGET = 73
    CARROT_ON_A_STICK = 74
    RUBY = 75
    EMERALD = 76
    CHERRY = 77
    COFFEE_CHERRY = 78
    GREEN_COFFEE_BEAN = 79
    CUP = 80
    COFFEE = 81
    ROASTED_COFFEE_BEAN = 82
    LINEN = 83
    LINEN_PANTS = 84
    LINEN_SHIRT = 85
    SAPPHIRE = 86
    AMETHYST = 87
    DIAMOND = 88
    GOLD_SPADE = 89
    GOLD_PICKAXE = 90
    DODO_EGG = 91
    STEEL_INGOT = 92
    STEEL_PICKAXE = 93
    AMETHYST_PICKAXE = 94
    SAPPHIRE_PICKAXE = 95
    EMERALD_PICKAXE = 96
    RUBY_PICKAXE = 97
    DIAMOND_PICKAXE = 98
    ULTRAMARINE_BLUE = 99
    CARBON_BLACK = 100
    MARBLE_WHITE = 101
    TIN_BUCKET = 102
    PAINT = 103
    PAINT_STRIPPER = 104
    BUCKET_OF_WATER = 105
    PIGMENT = 106
    RAINBOW_PAINT_CAP = 107
    INVALID_PIGMENT = 108
    EMERALD_GREEN = 109
    TYRIAN_PURPLE = 110
    BOAT = 111
    CHILLI = 112
    RAINBOW_LINEN_PANTS = 113
    RAINBOW_SHIRT = 114
    LINEN_CAP = 115
    RAINBOW_CAP = 116
    LINEN_BRIMMED_HAT = 117
    RAINBOW_BRIMMED_HAT = 118
    COPPER_BLUE = 119
    LEATHER = 120
    FUR = 121
    LEATHER_JACKET = 122
    RAINBOW_JACKET = 123
    LEATHER_BOOTS = 124
    RAINBOW_LEATHER_BOOTS = 125
    FUR_COAT = 126
    FUR_BOOTS = 127
    RAINBOW_COAT = 128
    RAINBOW_FUR_BOOTS = 129
    LEATHER_PANTS = 130
    RAINBOW_LEATHER_PANTS = 131
    UPGRADE = 132
    CAMERA = 133
    PORTAL = 134
    AMETHYST_PORTAL = 135
    SAPPHIRE_PORTAL = 136
    EMERALD_PORTAL = 137
    RUBY_PORTAL = 138
    DIAMOND_PORTAL = 139
    SUNRISE_HAT_OF_FULLNESS = 140
    SUNSET_SKIRT_OF_HAPPINESS = 141
    NORTH_POLE_HAT_OF_WARMTH = 142
    SOUTH_POLE_BOOTS_OF_SPEED = 143
    KELP = 144
    AMETHYST_CHANDELIER = 145
    SAPPHIRE_CHANDELIER = 146
    EMERALD_CHANDELIER = 147
    RUBY_CHANDELIER = 148
    DIAMOND_CHANDELIER = 149
    STEEL_LANTERN = 150
    RAW_FISH = 151
    COOKED_FISH = 152
    TIN_FOIL = 153
    TIN_FOIL_HAT = 154
    WORM = 155
    FISHING_ROD = 156
    SHARK_JAW = 157
    FISH_BUCKET = 158
    SHARK_BUCKET = 159
    LIME = 160
    SHELF = 161
    TELEPORT_HERE = 162
    SIGN = 163
    IRON_DOOR = 164
    IRON_TRAPDOOR = 165
    COPPER_COIN = 166
    GOLD_COIN = 167
    SHOP = 168
    SOFT_BED = 169
    GOLDEN_BED = 170
    BED_BLANKET = 171
    RAINBOW_SOFT_BED = 172
    RAINBOW_GOLDEN_BED = 173
    BLACK_WINDOW = 174
    MAGNET = 175
    COPPER_BOILER = 176
    ELECTRONIC_MOTOR = 177
    COPPER_WIRE = 178
    STEAM_ENGINE = 179
    IRON_POT = 180
    FISH_CURRY = 181
    DODO_STEW = 182
    ICE_TORCH = 183
    SILICON_INGOT = 184
    SILICON_CRYSTAL = 185
    SILICON_WAFER = 186
    TIN_ARMOR_LEGGINGS = 187
    TIN_CHEST_PLATE = 188
    TIN_HELMET = 189
    TIN_BOOTS = 190
    IRON_ARMOR_LEGGINGS = 191
    IRON_CHEST_PLATE = 192
    IRON_HELMET = 193
    IRON_BOOTS = 194
    ICE_ARMOR_LEGGINGS = 195
    ICE_CHEST_PLATE = 196
    ICE_HELMET = 197
    ICE_BOOTS = 198
    RAIL = 199
    TRAIN_STATION = 200
    PIG_IRON = 201
    CRUSHED_LIMESTONE = 202
    TRAIN_WHEEL = 203
    RAIL_HANDCAR = 204
    STEAM_LOCOMOTIVE = 205
    FREIGHT_CAR = 206
    DISPLAY_CABINET = 207
    PASSENGER_CAR = 208
    CROWBAR = 209
    TRADE_PORTAL = 210
    DEPRECATED_GOLD_CHEST = 211
    LARGE_SQUARE_PAINTING = 212
    LARGE_LANDSCAPE_PAINTING = 213
    LARGE_PORTRAIT_PAINTING = 214
    MED_SQUARE_PAINTING = 215
    MED_LANDSCAPE_PAINTING = 216
    MED_PORTRAIT_PAINTING = 217
    SMALL_SQUARE_PAINTING = 218
    SMALL_LANDSCAPE_PAINTING = 219
    SMALL_PORTRAIT_PAINTING = 220
    EASEL = 221
    STONE_COLUMN = 222
    LIMESTONE_COLUMN = 223
    MARBLE_COLUMN = 224
    SANDSTONE_COLUMN = 225
    RED_MARBLE_COLUMN = 226
    LAPIS_LAZULI_COLUMN = 227
    BASALT_COLUMN = 228
    STONE_STAIRS = 229
    LIMESTONE_STAIRS = 230
    MARBLE_STAIRS = 231
    SANDSTONE_STAIRS = 232
    RED_MARBLE_STAIRS = 233
    LAPIS_LAZULI_STAIRS = 234
    BASALT_STAIRS = 235
    COPPER_COLUMN = 236
    TIN_COLUMN = 237
    BRONZE_COLUMN = 238
    IRON_COLUMN = 239
    STEEL_COLUMN = 240
    GOLD_COLUMN = 241
    WOOD_COLUMN = 242
    BRICK_COLUMN = 243
    ICE_COLUMN = 244
    COPPER_STAIRS = 245
    TIN_STAIRS = 246
    BRONZE_STAIRS = 247
    IRON_STAIRS = 248
    STEEL_STAIRS = 249
    GOLD_STAIRS = 250
    WOOD_STAIRS = 251
    BRICK_STAIRS = 252
    ICE_STAIRS = 253
    STEEL_DOWNLIGHT = 254
    POISON = 255
    POISON_ARROW = 256
    GOLD_BOW_AND_POISON_ARROWS = 257
    STEEL_UPLIGHT = 258
    WORLD_CREDIT = 259
    PLATIUM_COIN = 260
    PLATIUM_NUGGET = 261
    PLATIUM_INGOT = 262
    PLATIUM_STAIRS = 263
    PLATIUM_COLUMN = 264
    GLASS_STAIRS = 265
    GLASS_COLUMN = 266
    BLACK_GLASS_STAIRS = 267
    BLACK_GLASS_COLUMN = 268
    FUEL = 269
    REFINERY = 270
    EPOXY = 271
    RAW_RESIN = 272
    CARBON_FIBERS = 273
    CARBON_FIBER_SHEET = 274
    CARBON_FIBER_WING = 275
    JETPACK_CHASSIS = 276
    JET_ENGINE = 277
    JETPACK = 278
    TITANIUM_ORE = 279
    TITANIUM_INGOT = 280
    TITANIUM_STAIRS = 281
    TITANIUM_COLUMN = 282
    CARBON_FIBER_STAIRS = 283
    CARBON_FIBER_COLUMN = 284
    TITANIUM_PICKAXE = 285
    TITANIUM_SWORD = 286
    TITANIUM_LEGGINGS = 287
    TITANIUM_CHEST_PLATE = 288
    TITANIUM_HELMET = 289
    TITANIUM_BOOTS = 290
    CARBON_FIBER_LEGGINGS = 291
    CARBON_FIBER_CHEST_PLATE = 292
    CARBON_FIBER_HELMET = 293
    CARBON_FIBER_BOOTS = 294
    VINE = 295
    TULIP_BULB = 296
    TULIP_SEED = 297
    COINS = 298
    RANDOM_ORE = 299
    ELECTRIC_SLUICE = 300
    OWNERSHIP_SIGN = 301
    CAGE = 302
    CAGED_DODO = 303
    WOODEN_GATE = 304
    AMETHYST_SHARD = 305
    SAPPHIRE_SHARD = 306
    EMERALD_SHARD = 307
    RUBY_SHARD = 308
    DIAMOND_SHARD = 309
    WHEAT = 310
    FLOUR = 311
    YEAST = 312
    SALT = 313
    DOUGH = 314
    BREAD = 315
    TOMATO = 316
    PIZZA = 317
    FLATBREAD = 318
    MILK = 319
    MOZZARELLA = 320
    YAK_HORN = 321
    RAZOR = 322
    YAK_SHAVINGS = 323
    CAGED_DONKEY = 324
    CAGED_YAK = 325
    CAGED_DROPBEAR = 326
    CAGED_SCORPION = 327
    RAINBOW_CAKE = 328
    RAINBOW_ESSENCE = 329
    CAGED_UNICORN = 330
    MIRROR = 331
    PLASTER_COLUMN = 332
    PLASTER_STAIRS = 333
    AMETHYST_COLUMN = 334
    SAPPHIRE_COLUMN = 335
    EMERALD_COLUMN = 336
    RUBY_COLUMN = 337
    DIAMOND_COLUMN = 338
    AMETHYST_STAIRS = 339
    SAPPHIRE_STAIRS = 340
    EMERALD_STAIRS = 341
    RUBY_STAIRS = 342
    DIAMOND_STAIRS = 343

    STONE = 1024
    KILN = 1025
    BRICK = 1026
    LIMESTONE = 1027
    MINED_LIMESTONE = 1028
    MARBLE = 1029
    MINED_MARBLE = 1030
    FURNACE = 1031
    WOODWORK_BENCH = 1032
    TAYLORS_BENCH = 1033
    PRESS = 1034
    SANDSTONE = 1035
    MINED_SANDSTONE = 1036
    RED_MARBLE = 1037
    MINED_RED_MARBLE = 1038
    WOVEN_FLAX_MAT = 1039
    YELLOW_FLAX_MAT = 1040
    RED_FLAX_MAT = 1041
    GLASS = 1042
    CHEST = 1043
    DEPRECATED_FOOD = 1044
    GOLD_BLOCK = 1045
    DEPRECATED_MANGO = 1046
    ROCK = 1047
    DIRT = 1048
    WOOD = 1049
    WORK_BENCH = 1050
    SAND = 1051
    TOOL_BENCH = 1052
    LAPIS_LAZULI = 1053
    MINED_LAPIS_LAZULI = 1054
    CRAFT_BENCH = 1055
    MIXING_BENCH = 1056
    REINFORCED_PLATFORM = 1057
    DEPRECATED_STONE_PICKAXE = 1058
    DEPRECATED_COPPER_INGOT = 1059
    ICE = 1060
    DYE_BENCH = 1061
    COMPOST = 1062
    BASALT = 1063  # ????
    MINED_BASALT = 1064
    SAFE = 1065
    COPPER_BLOCK = 1066
    TIN_BLOCK = 1067
    BRONZE_BLOCK = 1068
    IRON_BLOCK = 1069
    STEEL_BLOCK = 1070
    METALWORK_BENCH = 1071
    GOLDEN_CHEST = 1072
    DEPRECATED_BRONZE_MACHETE = 1073
    PORTAL_CHEST = 1074
    BLACK_SAND = 1075
    BLACK_GLASS = 1076
    STEAM_GENERATOR = 1077
    ELECTRIC_KILN = 1078
    ELECTRIC_FURNACE = 1079
    ELECTRIC_METALWORK_BENCH = 1080
    ELECTRIC_STOVE = 1081
    SOLAR_PANEL = 1082
    FLYWHEEL = 1083
    ARMOR_BENCH = 1084
    TRAIN_YARD = 1085
    BUILDERS_BENCH = 1086
    ELEVATOR_SHAFT = 1087
    ELECTRIC_ELEVATOR_MOTOR = 1088
    PLATIUM_BLOCK = 1089
    CARBON_FIBER_BLOCK = 1090
    TITANIUM_BLOCK = 1091
    DEPRECATED_IRON_SWORD = 1092
    ELECTRIC_PRESS = 1093
    GRAVEL = 1094
    COMPOST_BIN = 1095
    EGG_EXTRACTOR = 1096
    PIZZA_OVEN = 1097
    AMETHYST_BLOCK = 1098
    SAPPHIRE_BLOCK = 1099
    EMERALD_BLOCK = 1100
    RUBY_BLOCK = 1101
    DIAMOND_BLOCK = 1102
    PLASTER = 1103
    FEEDER_CHEST = 1104
    LUMINOUS_PLASTER = 1105