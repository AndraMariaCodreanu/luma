import datetime


class Timer:
    """
    Useful when waiting for an event to occur in a certain time frame.

    Args:
        hours (int): How many hours until the reached property is set to True.
        minutes (int): How many minutes until the reached property is set to True.
        seconds (int): How many seconds until the reached property is set to True.

    Properties:
        reached (bool): True if the set time has elapsed, False otherwise.
        elapsed_seconds (int): Yields how many seconds have elapsed since the timer has started or has been reset.

    Methods:
        stop: Stops the timer and sets the reached attribute to the corresponding state.
        reset: Restarts the timer and sets the reached attribute to the corresponding state.
    """
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.starting_time = datetime.datetime.now()
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._reached = False
        self.stopped = False
        if self.seconds >= 60:
            self.minutes += int(self.seconds / 60)
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += int(self.minutes / 60)
            self.minutes = self.minutes % 60

    def __repr__(self):
        result = '{}H:'.format(self.hours) if self.hours else '0H:'
        result += '{}M:'.format(self.minutes) if self.minutes else '0M:'
        result += '{}S:'.format(self.seconds) if self.seconds else '0S'
        return result

    @property
    def reached(self):
        """
        Property yielding the reached state of a Timer.
        :return: True if the timeout set when the Timer object was created or reset has been reached and False
                 otherwise.
        """
        if self.stopped:
            return self._reached
        else:
            self._reached = self.starting_time < (datetime.datetime.now() - datetime.timedelta(hours=self.hours,
                                                                                               minutes=self.minutes,
                                                                                               seconds=self.seconds))
            return self._reached

    def stop(self):
        """
        Stops the Timer and sets the reached property accordingly to the time passed since it's creation or reset.
        :return: None.
        """
        if not self.stopped:
            self._reached = self.starting_time < (datetime.datetime.now() - datetime.timedelta(hours=self.hours,
                                                                                               minutes=self.minutes,
                                                                                               seconds=self.seconds))
            self.stopped = True

    @property
    def elapsed_seconds(self):
        """
        Property yielding the total seconds passed since the Timer object was created or reset.
        :return: int - The total seconds passed since the Timer object was created or reset.
        """
        return int((datetime.datetime.now() - self.starting_time).total_seconds())

    def reset(self):
        """
        Method used to reset a Timer object and set the reached property accordingly.
        :return: None.
        """
        self.starting_time = datetime.datetime.now()
        self._reached = self.starting_time < (datetime.datetime.now() - datetime.timedelta(hours=self.hours,
                                                                                           minutes=self.minutes,
                                                                                           seconds=self.seconds))
        self.stopped = False
