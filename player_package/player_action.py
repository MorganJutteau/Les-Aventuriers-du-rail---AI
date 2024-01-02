DRAW_DESTINATION = "draw_destination"
DRAW_TRANSPORT = "draw_transport"
BUILD = "build"


class PlayerAction:
    def __init__(self, action_type, args):
        if action_type not in [DRAW_DESTINATION, DRAW_TRANSPORT, BUILD]:
            raise ValueError(
                f"action_type should be one of {DRAW_DESTINATION}, {DRAW_TRANSPORT} or {BUILD}"
            )

        if action_type == DRAW_DESTINATION:
            if len(args) != 0:
                raise ValueError(f"{DRAW_DESTINATION} should have no arguments")
        elif action_type == DRAW_TRANSPORT:
            if len(args) not in [1, 2]:
                raise ValueError(
                    f"{DRAW_TRANSPORT} should have 1 or 2 arguments, not {len(args)}"
                )
        elif action_type == BUILD:
            if len(args) != 2:
                raise ValueError(f"{BUILD} should have 2 arguments, not {len(args)}")

        self.action_type = action_type
        self.args = args

    def __str__(self):
        return f"{self.action_type} {self.args}"

    def __repr__(self):
        return f"{self.action_type} {self.args}"
