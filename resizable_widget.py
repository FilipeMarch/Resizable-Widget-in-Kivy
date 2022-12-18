from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ColorProperty
from kivy.metrics import dp
from kivy.core.window import Window


kv = """
<ResizeSelect>:
    canvas.before:
        # TOP LINE
        Color:
            rgba: root.top_color
        Line:
            width: dp(1)
            points: (self.x + dp(7), self.top, self.right - dp(7), self.top)  # Top line
            cap: 'round'
            joint: 'round'
            dash_offset: 2
            dash_length: 10
            close: False

        # BOTTOM LINE
        Color:
            rgba: root.bottom_color
        Line:
            width: dp(1)
            points: (self.x + dp(7), self.y, self.right - dp(7), self.y)  # Bottom
            cap: 'round'
            joint: 'round'
            dash_offset: 2
            dash_length: 10
            close: False

        # LEFT LINE
        Color:
            rgba: root.left_color
        Line:
            width: dp(1)
            points: (self.x, self.y+dp(7), self.x, self.top - dp(7))  # Left
            cap: 'round'
            joint: 'round'
            dash_offset: 2
            dash_length: 10
            close: False

        # RIGHT LINE
        Color:
            rgba: root.right_color
        Line:
            width: dp(1)
            points: (self.right, self.y + dp(7), self.right, self.top - dp(7))  # Right
            cap: 'round'
            joint: 'round'
            dash_offset: 2
            dash_length: 10
            close: False

        # Upper left rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.x, self.top - dp(7)
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.x, self.top - dp(7), \
                self.x + dp(7), self.top - dp(7),  self.x + dp(7), self.top, \
                self.x, self.top, \
                self.x, self.top - dp(7))  # Horizontal
            cap: 'round'
            joint: 'round'
            close: False

        # Bottom left rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.x, self.y
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.x, self.y, \
                self.x + dp(7), self.y,  self.x + dp(7), self.y + dp(7), \
                self.x, self.y + dp(7), \
                self.x, self.y)  # Vertical
            cap: 'round'
            joint: 'round'
            close: True

        # Bottom right rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.right - dp(7), self.y
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.right - dp(7), self.y, \
                self.right - dp(7), self.y + dp(7),  self.right, self.y + dp(7), \
                self.right, self.y, \
                self.right - dp(7), self.y)  # Vertical
            cap: 'round'
            joint: 'round'
            close: True
            
        # Upper right rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.right - dp(7), self.top - dp(7)
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.right - dp(7), self.top - dp(7), \
                self.right - dp(7), self.top,  self.right, self.top, \
                self.right, self.top - dp(7), \
                self.right - dp(7), self.top - dp(7))  # Horizontal
            cap: 'round'
            joint: 'round'
            close: True

        # Upper edge rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.x + self.width/2 - dp(3.5), self.top - dp(7)
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.x + self.width/2 - dp(3.5), self.top - dp(7), \
                self.x + self.width/2 + dp(3.5), self.top - dp(7),  self.x + self.width/2 + dp(3.5), self.top, \
                self.x + self.width/2 - dp(3.5), self.top, \
                self.x + self.width/2 - dp(3.5), self.top - dp(7))  # Horizontal
            cap: 'round'
            joint: 'round'
            close: True

        # Left edge rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.x, self.y + self.height/2 - dp(3.5)
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.x, self.y + self.height/2 - dp(3.5), \
                self.x + dp(7), self.y + self.height/2 - dp(3.5), \
                self.x + dp(7), self.y + self.height/2 + dp(3.5), \
                self.x, self.y + self.height/2 + dp(3.5), \
                self.x, self.y + self.height/2 - dp(3.5))  # Vertical
            cap: 'round'
            joint: 'round'
            close: True

        # Right edge rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.right - dp(7), self.y + self.height/2 - dp(3.5)
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.right - dp(7), self.y + self.height/2 - dp(3.5), \
                self.right, self.y + self.height/2 - dp(3.5), \
                self.right, self.y + self.height/2 + dp(3.5), \
                self.right - dp(7), self.y + self.height/2 + dp(3.5), \
                self.right - dp(7), self.y + self.height/2 - dp(3.5))  # Vertical
            cap: 'round'
            joint: 'round'
            close: True

        # Bottom edge rectangle
        Color:
            rgba: 62/255, 254/255, 1, 1
        Rectangle:
            pos: self.x + self.width/2 - dp(3.5), self.y
            size: dp(7), dp(7)
        Color:
            rgba: 1,1,1,1
        Line:
            width: dp(1)
            points: ( \
                self.x + self.width/2 - dp(3.5), self.y, \
                self.x + self.width/2 + dp(3.5), self.y, \
                self.x + self.width/2 + dp(3.5), self.y + dp(7), \
                self.x + self.width/2 - dp(3.5), self.y + dp(7), \
                self.x + self.width/2 - dp(3.5), self.y)  # Horizontal
            cap: 'round'
            joint: 'round'
            close: True
    

RelativeLayout:
    ResizeSelect:
        size_hint: None, None
        size: dp(300),dp(300)
        pos: 20, 40

<DashedLabel@Label>:
    canvas:
        Color:
            rgb: 1, 1, 1
        Line:
            dash_offset: 2
            dash_length: 10
            rectangle: (*self.pos, *self.size)
"""


class AbstractClass:
    pos = (0, 0)


class ResizeSelect(FloatLayout):
    top_color = ColorProperty("red")
    bottom_color = ColorProperty("red")
    left_color = ColorProperty("red")
    right_color = ColorProperty("red")
    highlight_color = ColorProperty("red")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_side = None
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, something, touch):
        """
        When the mouse moves, we check the position of the mouse
        and update the cursor accordingly.
        """
        if self.collide_point(touch[0], touch[1]):
            collision = self.collides_with_control_points(something, touch)
            if collision in ["top left", "bottom right"]:
                Window.set_system_cursor("size_nwse")
            elif collision in ["top right", "bottom left"]:
                Window.set_system_cursor("size_nesw")
            elif collision in ["top", "bottom"]:
                Window.set_system_cursor("size_ns")
            elif collision in ["left", "right"]:
                Window.set_system_cursor("size_we")
            else:
                Window.set_system_cursor("size_all")
        else:
            Window.set_system_cursor("arrow")

    def collides_with_control_points(self, _, touch):
        """
        Returns True if the mouse is over a control point.
        """
        x, y = touch[0], touch[1]

        # Checking mouse is on left edge
        if self.x <= x <= self.x + dp(7):
            if self.y <= y <= self.y + dp(7):
                return "bottom left"
            elif self.y + dp(7) <= y <= self.y + self.height - dp(7):
                return "left"
            else:
                return "top left"

        # Checking mouse is on top edge
        elif self.x + dp(7) <= x <= self.x + self.width - dp(7):
            if self.y <= y <= self.y + dp(7):
                return "bottom"
            elif self.y + self.height - dp(7) <= y <= self.y + self.height:
                return "top"
            else:
                return False

        # Checking mouse is on right edge
        elif self.x + self.width - dp(7) <= x <= self.x + self.width:
            if self.y <= y <= self.y + dp(7):
                return "bottom right"
            elif self.y + dp(7) <= y <= self.y + self.height - dp(7):
                return "right"
            else:
                return "top right"

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            x, y = touch.pos[0], touch.pos[1]

            collision = self.collides_with_control_points("", touch.pos)

            if collision == "top":
                self.top_color = self.highlight_color
                self.selected_side = "top"
            elif collision == "bottom":
                self.bottom_color = self.highlight_color
                self.selected_side = "bottom"
            elif collision == "left":
                self.left_color = self.highlight_color
                self.selected_side = "left"
            elif collision == "right":
                self.right_color = self.highlight_color
                self.selected_side = "right"
            else:
                if collision == "top left":
                    self.selected_side = "top left"
                    self.top_color = self.highlight_color
                    self.left_color = self.highlight_color
                elif collision == "bottom right":
                    self.selected_side = "bottom right"
                    self.bottom_color = self.highlight_color
                    self.right_color = self.highlight_color
                elif collision == "top right":
                    self.selected_side = "top right"
                    self.top_color = self.highlight_color
                    self.right_color = self.highlight_color
                elif collision == "bottom left":
                    self.selected_side = "bottom left"
                    self.bottom_color = self.highlight_color
                    self.left_color = self.highlight_color
                else:
                    self.selected_side = None
                    self.top_color = self.highlight_color
                    self.bottom_color = self.highlight_color
                    self.left_color = self.highlight_color
                    self.right_color = self.highlight_color
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        MINIMUM_HEIGHT = 50.0
        MINIMUM_WIDTH = 50.0

        if touch.grab_current is self:
            x, y = self.to_window(*self.pos)

            top = y + self.height  # top of our widget
            right = x + self.width  # right of our widget

            if x < self.parent.x or right > self.parent.right:
                print("X out of bounds")
            if y < self.parent.y or top > self.parent.top:
                print("y out of bounds")

            if self.selected_side == "top":
                if self.height + touch.dy <= MINIMUM_HEIGHT:
                    return False
                self.height += touch.dy

            elif self.selected_side == "bottom":
                if self.height - touch.dy <= MINIMUM_HEIGHT:
                    return False
                self.height -= touch.dy
                self.y += touch.dy

            elif self.selected_side == "left":
                if self.width - touch.dx <= MINIMUM_WIDTH:
                    return False
                self.width -= touch.dx
                self.x += touch.dx

            elif self.selected_side == "right":
                if self.width + touch.dx <= MINIMUM_WIDTH:
                    return False
                self.width += touch.dx

            elif self.selected_side == "top left":
                if touch.dx > 0:
                    if self.width - touch.dx <= MINIMUM_WIDTH:
                        return False
                if touch.dy < 0:
                    if self.height + touch.dy <= MINIMUM_HEIGHT:
                        return False

                self.width -= touch.dx
                self.x += touch.dx  # OK
                self.height += touch.dy

            elif self.selected_side == "top right":
                if touch.dx < 0:
                    if self.width + touch.dx <= MINIMUM_WIDTH:
                        return False
                if touch.dy < 0:
                    if self.height + touch.dy <= MINIMUM_HEIGHT:
                        return False

                self.width += touch.dx
                self.height += touch.dy

            elif self.selected_side == "bottom left":
                if touch.dx > 0:
                    if self.width - touch.dx <= MINIMUM_WIDTH:
                        return False
                if touch.dy > 0:
                    if self.height - touch.dy <= MINIMUM_HEIGHT:
                        return False

                self.width -= touch.dx  # OK
                self.x += touch.dx
                self.height -= touch.dy
                self.y += touch.dy

            elif self.selected_side == "bottom right":
                if touch.dx < 0:
                    if self.width + touch.dx <= MINIMUM_WIDTH:
                        return False
                if touch.dy > 0:
                    if self.height - touch.dy <= MINIMUM_HEIGHT:
                        return False

                self.width += touch.dx
                self.height -= touch.dy
                self.y += touch.dy

            elif not self.selected_side:
                print("No side selected: ")
                self.x += touch.dx
                self.y += touch.dy

        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.bottom_color = (
                self.top_color
            ) = self.left_color = self.right_color = "white"

            return True
        return super().on_touch_up(touch)


Builder.load_string(kv)


class ResizeWidgetApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    ResizeWidgetApp().run()
