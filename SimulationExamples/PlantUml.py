from pylint.pyreverse.main import Run

# Generate UML diagrams in the current directory
Run(["BouncingBall_ex.py", "-o", "puml"])
