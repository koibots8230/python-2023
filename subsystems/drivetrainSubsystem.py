import commands2
import rev
import wpilib
import wpilib.drive
import constants


class TankDriveSubsystem(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        self.leftLeadMotor = rev.CANSparkMax(constants.leftLeadMotor, rev.CANSparkMax.MotorType.kBrushless)
        self.rightLeadMotor = rev.CANSparkMax(constants.rightLeadMotor, rev.CANSparkMax.MotorType.kBrushless)
        self.leftFollowMotor = rev.CANSparkMax(constants.leftFollowMotor, rev.CANSparkMax.MotorType.kBrushless)
        self.rightFollowMotor = rev.CANSparkMax(constants.rightFollowMotor, rev.CANSparkMax.MotorType.kBrushless)

        self.leftMotors = wpilib.MotorControllerGroup(self.leftLeadMotor, self.leftFollowMotor)
        self.rightMotors = wpilib.MotorControllerGroup(self.rightLeadMotor, self.rightFollowMotor)

        self.differentialDrive = wpilib.drive.DifferentialDrive(self.leftMotors, self.rightMotors)

    def tankDrive(self, left, right):
        self.differentialDrive.tankDrive(left * constants.tankLeftDriveSpeed, right * constants.tankRightDriveSpeed,
                                         constants.squareInput)

    def arcadeDrive(self, movement, turn):
        self.differentialDrive.arcadeDrive(movement * constants.arcadeDriveSpeed, turn * constants.arcadeTurnSpeed,
                                           constants.squareInput)

    def setBrakeMode(self, brake = True):
        if brake:
            self.leftLeadMotor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
            self.rightLeadMotor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
            self.leftFollowMotor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
            self.rightFollowMotor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        else:
            if brake:
                self.leftLeadMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
                self.rightLeadMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
                self.leftFollowMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
                self.rightFollowMotor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)

    def setCoastMode(self, coast=True):
        self.setBrakeMode(not coast)

