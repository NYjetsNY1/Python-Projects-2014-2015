# Ben Sklar
# A virtual TV Remote Control.
# Includes all extensions - adds some contemporary remote items.

# Necessary to define Television as a class-object.
class Television(object):
    """A virtual Television"""
    # Starts at volume 1, channel 1, TV off, TV not muted, and DVD player off.
    def __init__(self, __channel = 1, volume = 1, is_on = False, is_muted = False, is_dvd_on = False):
        self.__channel = __channel
        self.volume = volume
        self.is_on = is_on
        self.is_muted = is_muted
        self.is_dvd_on = is_dvd_on


    # Status of Television.
    def __status__(self):
        if self.is_on == True:
            print("The TV is on.")
            print("Current Channel:", self.__channel)
            if self.is_muted == False:
                print("Current Volume Level:", self.volume)
            else:
                print("Volume is currently muted.")
        else:
            print("The TV is off.")


    # Toggle the power on and off.
    def toggle_power(self):
        if self.is_on == True:
            self.is_on = False
            return self.is_on
        if self.is_on == False:
            self.is_on = True
            return self.is_on


    # Toggle the mute on and off.
    # Note, you can't adjust volume when muted. Just how it is. Unmute to adjust volume.
    def toggle_mute(self):
        if self.is_on == True:
            if self.is_muted == True:
                self.is_muted = False
                return self.is_muted
            if self.is_muted == False:
                self.is_muted = True
                return self.is_muted


    # Toggle the DVD player on and off.
    # Can adjust even if TV is off.
    def toggle_dvd_player(self):
        if self.is_dvd_on == False:
            self.is_dvd_on = True
            print("DVD player turned on.")
            return self.is_dvd_on
        if self.is_dvd_on == True:
            self.is_dvd_on = False
            print("DVD player turned off.")
            return self.is_dvd_on


    # Set the channel between 0 and 500.
    def set_channel(self, choice):
        if self.is_on == True:
            if choice >= 0 and choice <= 500:
                self.__channel = choice
            else:
                print("Channel not in range!")
        else:
            print("The TV isn't on!")

    # Raise the volume up to 10.
    def raise_volume(self, up=1):
        if self.is_on == True:
            if self.is_muted == False:
                self.volume += up
                if self.volume >= 10:
                    self.volume = 10
                    print("Max volume!")
            else:
                print("The TV is currently on the mute setting. Please unmute it to raise volume.")
        else:
            print("The TV isn't on!")


    # Lower the volume down to 0.
    def lower_volume(self, down=1):
        if self.is_on == True:
            if self.is_muted == False:
                self.volume -= down
                if self.volume <= 0:
                    self.volume = 0
                    print("Min volume!")
            else:
                print("The TV is currently on the mute setting. Please unmute it to lower the volume.")
        else:
            print("The TV isn't on!")


    # Raise the channel up to 500.
    def channel_up(self, up=1):
        if self.is_on == True:
            self.__channel += up
            if self.__channel >= 500:
                self.__channel = 500
                print("Highest possible channel!")
        else:
            print("The TV isn't on!")


    # Lower the channel down to 0.     
    def channel_down(self, down=1):
        if self.is_on == True:
            self.__channel -= down
            if self.__channel <= 0:
                self.__channel = 0
                print("Lowest possible channel!")
        else:
            print("The TV isn't on!")


    # Mute the TV.
    # Remember, when TV is muted, can't change volume till unmuted.
    def mute(self):
        if self.is_on == True:
            if self.is_muted == True:
                print("The TV has been muted.")
            elif self.is_muted == False:
                print("The TV has been unmuted.")
        else:
            print("The TV isn't on!")


    # Record a channel.
    # Just a print statement to tell you that the channel will be recorded.
    def record(self):
        if self.is_on == True:
            print("Channel", self.__channel, "will be recorded.")
        else:
            print("The TV isn't on!")

# Main function.
def main():

    tv = Television()
    choice= None
    while choice != "0":
        print( \
        """
        TV Remote Control

        0 - Exit
        1 - Toggle Power ON/OFF
        2 - Change Channel
        3 - Raise Volume
        4 - Lower Volume
        5 - Channel Up
        6 - Channel Down
        7 - Mute/Unmute
        8 - Turn DVD player on
        9 - TV status
        10 - Record this channel
        """)


        # Asks user for choice.
        choice = input("Choice: ")
        print()


        # Quit the program.
        if choice == "0":
            print("Good-bye.")


        # Turn TV on/off.
        elif choice == "1":
            tv.toggle_power()
            tv.__status__()


        # Change to any channel between 0-500.
        elif choice == "2":
            change = int(input("What channel number (0-500) would you like?: "))
            tv.set_channel(change)
            tv.__status__()


        # Change volume up one unit.
        elif choice == "3":
            tv.raise_volume()
            tv.__status__()


        # Change volume down one unit.
        elif choice == "4":
            tv.lower_volume()
            tv.__status__()


        # Change channel up one unit.
        elif choice == "5":
            tv.channel_up()
            tv.__status__()


        # Change channel down one unit.
        elif choice == "6":
            tv.channel_down()
            tv.__status__()


        # Mute TV. TV cannot change volume until Unmuted.
        # Must actually toggle Unmute to change volume.
        elif choice == "7":
            tv.toggle_mute()
            tv.mute()
            tv.__status__()


        # Turns on or off the DVD player.
        # You can turn DVD player on even if TV is off.
        elif choice == "8":
            tv.toggle_dvd_player()
            tv.__status__()


        # TV status. Somewhat irrelevant as can find it out any other way.
        elif choice == "9":
            tv.__status__()


        # Record the channel.
        # Doesn't actually do anything, just tells you that it will record the channel.
        # If you ever wanted to build a DVR program, you could add more.
        elif choice == "10":
            tv.record()
            tv.__status__()


        # Any unknown choice.
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
("\n\nPress the enter key to exit.") 
