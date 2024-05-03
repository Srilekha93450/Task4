class TV:
    def __init__(self, brand):
        # Initialize TV with the brand name, default channel 1, volume 50, and TV off
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on = False

    def increase_volume(self):
        # Increase volume if it's less than 100
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        # Decrease volume if it's greater than 0
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        # Set channel if it's between 1 and 50
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        # Reset TV settings to default
        self.channel = 1
        self.volume = 50

    def status(self):
        # Return status of the TV: brand, channel, and volume
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


# Create an instance of TV and test its methods
tv = TV("Panasonic")
print(tv.status())  # Output: Panasonic at channel 1, volume 50
tv.increase_volume()
tv.set_channel(8)
print(tv.status())  # Output: Panasonic at channel 8, volume 51
tv.reset_tv()
print(tv.status())  # Output: Panasonic at channel 1, volume 50


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        # Initialize LedTV with additional attributes specific to LED TVs
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        # Return detailed information about the LED TV
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, " \
               f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, " \
               f"Refresh Rate: {self.refresh_rate}"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        # Initialize PlasmaTV with additional attributes specific to Plasma TVs
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def display_details(self):
        # Return detailed information about the Plasma TV
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, " \
               f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, " \
               f"Refresh Rate: {self.refresh_rate}, Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}"


# Create instances of LedTV and PlasmaTV and test their methods
led_tv = LedTV("Sony", "Slim", "Low", "10 years", "60 Hz")
print(led_tv.status())  # Output: Sony at channel 1, volume 50
print(led_tv.display_details())  # Output: Brand: Sony, Screen Thickness: Slim, Energy Usage: Low, Lifespan: 10 years, Refresh Rate: 60 Hz

plasma_tv = PlasmaTV("Samsung", "Medium", "Medium", "8 years", "120 Hz", "180 degrees", "Yes")
print(plasma_tv.status())  # Output: Samsung at channel 1, volume 50
print(plasma_tv.display_details())  # Output: Brand: Samsung, Screen Thickness: Medium, Energy Usage: Medium, Lifespan: 8 years, Refresh Rate: 120 Hz, Viewing Angle: 180 degrees, Backlight: Yes
