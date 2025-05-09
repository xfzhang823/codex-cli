class InteractiveMode:
    def start(self):
        while True:
            command = input("Enter command: ").strip()
            if command.lower() == "exit":
                break
            elif command.startswith("generate "):
                prompt = command[len("generate "):]
                generator = CodeGenerator()
                print(generator.generate_code(prompt))
            elif command.startswith("explain "):
                code = command[len("explain "):]
                explainer = Explainer()
                print(explainer.explain(code))
            else:
                print("Unknown command.")