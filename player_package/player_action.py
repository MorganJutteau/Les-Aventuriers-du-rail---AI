class PlayerAction:
    DRAW_DESTINATION = "draw_destination"
    DRAW_TRANSPORT = "draw_transport"
    BUILD = "build"

    def __init__(self, action_type, args):
        if action_type not in [
            PlayerAction.DRAW_DESTINATION,
            PlayerAction.DRAW_TRANSPORT,
            PlayerAction.BUILD,
        ]:
            raise ValueError(
                f"action_type should be one of {PlayerAction.DRAW_DESTINATION}, {PlayerAction.DRAW_TRANSPORT} or {PlayerAction.BUILD}"
            )

        if action_type == PlayerAction.DRAW_DESTINATION:
            if len(args) != 0:
                raise ValueError(
                    f"{PlayerAction.DRAW_DESTINATION} should have no arguments"
                )
        elif action_type == PlayerAction.DRAW_TRANSPORT:
            if len(args) not in [1, 2]:
                raise ValueError(
                    f"{PlayerAction.DRAW_TRANSPORT} should have 1 or 2 arguments, not {len(args)}"
                )
        elif action_type == PlayerAction.BUILD:
            if len(args) != 2:
                raise ValueError(
                    f"{PlayerAction.BUILD} should have 2 arguments, not {len(args)}"
                )

        self.action_type = action_type
        self.args = [int(arg) for arg in args]

    def __str__(self):
        return f"{self.action_type} {self.args}"

    def __repr__(self):
        return f"{self.action_type} {self.args}"
