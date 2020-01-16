"""
Calculate properties of Virtual address
"""
import toga
import math
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class VirtualAddress(toga.App):

    def button_handler(self, button):
        main_box = self.main_window.content

        if 0 <= self.textEntry.value.find('0x'):
            value = int(self.textEntry.value, 0)
            virtual_address = bin(value)[2:]
            address_len = len(virtual_address)

            # Check length of bit string
            if address_len < int(self.textEntry1.value) or int(self.textEntry1.value) < address_len:
                n = 13 - address_len
                virtual_address = ('0' * n) + virtual_address

            # Calculate VPN, TLB index, TLB tag
            
            # Firstly get offset (Where VPN starts)
            vpn_offset = int(math.log2(int(self.textEntry3.value)))
            vpn_bits = virtual_address[:-vpn_offset]
            vpn_value = hex(int(vpn_bits, 2))

            TLB_index_length    = int(math.log2(int(self.textEntry2.value)))
            TLB_index_bits      = virtual_address[-(vpn_offset+TLB_index_length):-vpn_offset]
            TLB_index_value     = hex(int(TLB_index_bits, 2))

            TLB_tag_offset      = vpn_offset+TLB_index_length
            TLB_tag_bits        = virtual_address[:-TLB_tag_offset]
            TLB_tag_value     = hex(int(TLB_tag_bits, 2))

            # Add the results to window

            # Labels
            label = toga.Label('Bits of virtual address', style=Pack(flex=1, text_align='center'))
            label.style.font_size = 18
            label.style.font_family = 'monospace'
            label.style.font_weight = 'bold'

            address_label = toga.Label(virtual_address, style=Pack(flex=1, text_align='center'))
            address_label.style.font_size = 15
            address_label.style.font_family = 'monospace'
            address_label.style.font_weight = 'bold'

            headings = ['VPN', 'TLB index', 'TLB tag', 'VPO/PPO bits']
            table = toga.Table(
                headings=headings,
                data=[(vpn_value, TLB_index_value, TLB_tag_value, vpn_offset)],
                style=Pack(flex=1, height=50, padding=(10,10,10,10))
            )

            main_box.add(label)
            main_box.add(address_label)
            main_box.add(table)
        
        self.main_window.content = main_box

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        self.main_window = toga.MainWindow(title=self.formal_name, size=(350, 400))

        # Label
        label = toga.Label('Virtual address properties', style=Pack(flex=1, text_align='center', padding=(10,0)))
        label.style.font_family = 'monospace'
        label.style.font_size = 20
        label.style.font_weight = 'bold'

        # Text entry
        self.textEntry = toga.TextInput(style=Pack(flex=1, padding=(0, 10, 10)), placeholder='The address eg. 0x0000')

        # Button
        button = toga.Button('Calculate', style=Pack(padding=(0, 15, 15)), on_press=self.button_handler)
        #button.style.padding = 10
        button.style.flex = 1

        # Container box
        inner_box = toga.Box(
            style=Pack(direction=ROW, padding=(10, 0, 0, 10)),
            children=[
                self.textEntry,
                button
            ]
        )

        # Text entry
        self.textEntry1 = toga.TextInput(style=Pack(flex=1, padding=(0, 10, 10)), placeholder='In bits, eg. 13')

        # Label n variable
        label1 = toga.Label('Length of virtual address', style=Pack(flex=1, padding=(0, 5, 0)))

        # Container box
        inner_box1 = toga.Box(
            style=Pack(direction=ROW, padding=(10, 0, 0, 10)),
            children=[
                self.textEntry1,
                label1
            ]
        )

        # Text entry
        self.textEntry2 = toga.TextInput(style=Pack(flex=1, padding=(0, 10, 10)), placeholder='Eg. 4')

        # Label m variable
        label2 = toga.Label('Number of sets', style=Pack(flex=1, padding=(0, 5, 0)))

        # Container box
        inner_box2 = toga.Box(
            style=Pack(direction=ROW, padding=(10, 0, 0, 10)),
            children=[
                self.textEntry2,
                label2
            ]
        )

        # Text entry
        self.textEntry3 = toga.TextInput(style=Pack(flex=1, padding=(0, 10, 10)), placeholder='Eg. 32')

        # Label m variable
        label3 = toga.Label('Page size in bytes', style=Pack(flex=1, padding=(0, 5, 0)))

        # Container box
        inner_box3 = toga.Box(
            style=Pack(direction=ROW, padding=(10, 0, 0, 10)),
            children=[
                self.textEntry3,
                label3
            ]
        )

        outer_box = toga.Box(
            children=[label, inner_box1, inner_box2, inner_box3, inner_box],
            style=Pack(direction=COLUMN)
        )

        # Add elements

        self.main_window.content = outer_box
        self.main_window.show()


def main():
    return VirtualAddress()
