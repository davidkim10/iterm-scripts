#!/usr/bin/env python3.7

import iterm2
# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    if window is not None:
        # If you want to launch in seperate tab uncomment
        # tab = await window.async_create_tab()
        # await tab.async_activate()
        # session = tab.current_session

        tab = window.current_tab
        session = window.current_tab.current_session

        await tab.async_set_title('ENTER TAB TITLE HERE')

        # Left Pane (main)
        await session.async_send_text('cd /your-path-here\n')
        await session.async_send_text('enter command here\n')
        await session.async_send_text('enter command here\n')

        # Right Pane
        paneRight = await session.async_split_pane(vertical=True)
        await session.async_send_text('cd /your-path-here\n')
        await session.async_send_text('enter command here\n')
        await session.async_send_text('enter command here\n')

        paneRight2 = await paneRight.async_split_pane(vertical=False)
        await session.async_send_text('cd /your-path-here\n')
        await session.async_send_text('command here\n')

        paneRight3 = await paneRight2.async_split_pane(vertical=False)
        await session.async_send_text('cd /your-path-here\n')
        await session.async_send_text('command here\n')
        
    else:
        # You can view this message in the script console.
        print("No current window")
        exit();

iterm2.run_until_complete(main)
