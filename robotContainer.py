import commands2.cmd
import commands2
import wpilib

import constants
import subsystems.drivetrainSubsystem


class RobotContainer:
    def __init__(self):
        self.drivetrain = subsystems.drivetrainSubsystem.TankDriveSubsystem()

    def configureControllers(self):
        self.leftJoystick = wpilib.Joystick(constants.leftJoystick)
        self.rightJoystick = wpilib.Joystick(constants.rightJoystick)

        if constants.driveMode.lower() == "tank":
            self.drivetrain.setDefaultCommand(
                commands2.cmd.run(self.drivetrain.tankDrive(self.leftJoystick.getY(), self.rightJoystick.getY()))
            )
        elif constants.driveMode.lower() == "arcade":
            self.drivetrain.setDefaultCommand(
                commands2.cmd.run(self.drivetrain.arcadeDrive(self.leftJoystick.getY(), self.leftJoystick.getX()))
            )
        else:
            self.drivetrain.setDefaultCommand(
                commands2.cmd.run(self.drivetrain.tankDrive(self.leftJoystick.getY(), self.rightJoystick.getY()))
            )
