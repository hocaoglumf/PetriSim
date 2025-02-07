from pylint.pyreverse.main import Run

# Generate UML diagrams in the current directory
Run(["BouncingBall.py", "-o", "puml"])
