import commands2
import wpilib
import rev
from wpilib.drive import DifferentialDrive

import robotContainer
import subsystems.drivetrainSubsystem


class MyRobot(commands2.TimedCommandRobot):

    # robot
    def robotInit(self):
        self.container = robotContainer.RobotContainer()

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    # auto
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def autonomousExit(self):
        pass

    # teleop
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.container.drivetrain.tankDrive(self.leftJoystick.getY(), self.rightJoystick.getY())

    def teleopExit(self):
        pass

    # test
    def testInit(self):
        self.container.drivetrain.setCoastMode()

    def testPeriodic(self):
        pass

    def testExit(self):
        pass
