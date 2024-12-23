import math

class OpticalDisk:
    def __init__(self, capacity_gb, rpm, laser_thickness_nm):
        self.capacity_gb = capacity_gb  # Емкость диска, GB
        self.rpm = rpm  # Скорость оборотов в минуту
        self.laser_thickness_nm = laser_thickness_nm  # Толщина лазера в нанометрах

    def bytes_per_20_seconds(self, radius_cm):
        circumference = 2 * math.pi * radius_cm  # Длина окружности
        bytes_per_second = (circumference * self.rpm / 60) / self.laser_thickness_nm
        return bytes_per_second * 20

class CD(OpticalDisk):
    def __init__(self, capacity_gb, rpm, laser_thickness_nm, music_minutes):
        super().__init__(capacity_gb, rpm, laser_thickness_nm)
        self.music_minutes = music_minutes  # Количество минут музыки

    def average_rotation_time(self):
        return 60 / self.rpm

class DVD(OpticalDisk):
    def __init__(self, capacity_gb, rpm, laser_thickness_nm, video_resolution):
        super().__init__(capacity_gb, rpm, laser_thickness_nm)
        self.video_resolution = video_resolution  # Разрешение видео

    def average_rotation_time(self):
        return 60 / self.rpm
