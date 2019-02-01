from TestStack.White.InputDevices import Mouse
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword
from System.Windows import Point
from robot.api import logger

class MouseKeywords(LibraryComponent):

    @keyword
    def set_mouse_location(self, x, y):
        """ Sets mouse position to (x, y) Position is relative to application window.

        """
        window_location = self.state.window.Bounds.TopLeft
        point = Point(int(x) + window_location.X, int(y) + window_location.Y)
        Mouse.Instance.Location = point

    @keyword
    def move_mouse_location(self, x, y):
        """ Sets mouse position to (x, y) Position is relative to application window.

        """
        current_location = Mouse.Instance.Location
        point = Point(int(x) + current_location.X, int(y) + current_location.Y)
        Mouse.Instance.Location = point

    @keyword
    def get_mouse_location(self):
        """ Gets mouse position. Position is relative to application window.

        """
        point = Point()
        point = Mouse.Instance.Location
        return point.X, point.Y

    @keyword
    def mouse_right_button_down(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """

        if (x is None) and (y is None):
            Mouse.Instance.RightDown()
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.Location = point
            Mouse.Instance.RightDown()

    @keyword
    def mouse_left_button_down(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """
        if (x is None) and (y is None):
            Mouse.Instance.LeftDown()
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.Location = point
            Mouse.Instance.LeftDown()


    @keyword
    def mouse_right_button_up(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """

        if (x is None) and (y is None):
            Mouse.Instance.RightUp()
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.Location = point
            Mouse.Instance.RightUp()

    @keyword
    def mouse_left_button_up(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """
        if (x is None) and (y is None):
            Mouse.Instance.LefttUp(Mouse.Instance.Location)
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.Location = point
            Mouse.Instance.LeftUp()

    @keyword
    def mouse_right_click(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """
        if (x is None) and (y is None):
            Mouse.Instance.RightClick()
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.RightClick(point)

    @keyword
    def mouse_left_click(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """

        if (x is None) and (y is None):
            Mouse.Instance.Click()
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.Click(point)

    @keyword
    def mouse_right_double_click(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """

        if (x is None) and (y is None):
            Mouse.Instance.RightClick()
            Mouse.Instance.RightClick()
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.RightClick(point)
            Mouse.Instance.RightClick(point)

    @keyword
    def mouse_left_double_click(self, x=None, y=None):
        """ Right clicks mouse position. Position is relative to screen.

        """

        if (x is None) and (y is None):
            Mouse.Instance.DoubleClick()
        else:
            window_location = self.state.window.Bounds.TopLeft
            point = Point(int(x) + window_location.X, int(y) + window_location.Y)
            Mouse.Instance.DoubleClick(point)

    @keyword
    def drag_and_drop(self, locator1, locator2):
        """ Drags item under locator1 to item under locator2.

        ``locator1`` is the locator of the draggable object (TODO: check if needs to be draggable).
        ``locator2`` is the locator of the target for the draggable object.
        """

        draggable_object = self.state._get_item_by_locator(locator1)
        target_object = self.state._get_item_by_locator(locator2)
        Mouse.Instance.DragAndDrop(draggable_object, target_object)

    @keyword
    def drag_horizontally(self, locator, distance):
        """ Drags item under locator1 to distance amounts.

        ``locator`` is the locator of the draggable object (TODO: check if needs to be draggable).
        ``distance`` is ingered amount of distance to be dragged. Positive value rightwards, negative value leftwards. (TODO: verify)
        """

        draggable_object = self.state._get_item_by_locator(locator)
        Mouse.Instance.DragHorizontally(draggable_object, int(distance))
