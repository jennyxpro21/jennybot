from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),

    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✘ 𝘽𝙇𝘼𝘾𝙆𝙇𝙄𝙎𝙏 ✘",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✘ 𝘼𝙐𝙏𝙃 ✘",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="✘ 𝘼𝘿𝙈𝙄𝙉 ✘",
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✘ 𝘽𝙍𝙊𝘼𝘿𝘾𝘼𝙎𝙏 ✘",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✘ 𝙂-𝘽𝘼𝙉 ✘",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="✘ 𝙇𝙔𝙍𝙄𝘾𝙎 ✘",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✘ 𝙋𝙇𝘼𝙔𝙇𝙄𝙎𝙏 ✘",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✘ 𝙋𝙇𝘼𝙔 ✘",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="✘ 𝙋𝙄𝙉𝙂 ✘",
                    callback_data="help_callback hb7",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✘ 𝙑𝙄𝘿𝙀𝙊𝘾𝙃𝘼𝙏𝙎 ✘",
                    callback_data="help_callback hb10",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✘ 𝙎𝙏𝘼𝙍𝙏 ✘",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="✘ 𝙎𝙐𝘿𝙊 ✘",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✘ 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 ✘",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
