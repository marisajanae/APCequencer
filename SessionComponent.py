from _APC.SessionComponent import SessionComponent

class SessionComponent(SessionComponent):
  """ Resets matrix when assigned """

  def set_clip_launch_buttons(self, buttons):
    if buttons:
      buttons.reset()
    super(SessionComponent, self).set_clip_launch_buttons(buttons)

