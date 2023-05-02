import random
import parser

def fuzz():
    # Load constants
    constants = __import__('constants')

    # Randomly choose a method to fuzz
    methods = [parser.checkIfWeirdYAML, parser.checkIfValidK8SYaml, 
parser.checkIfValidHelm,
               parser.readYAMLAsStr, parser.loadMultiYAML]

    method = random.choice(methods)

    # Generate random input
    if method == parser.checkIfWeirdYAML or method == 
parser.checkIfValidK8SYaml or method == parser.checkIfValidHelm:
        yaml_script = '---\nfoo: ' + str(random.randint(1, 100))

        # Call the method with the random input
        try:
            result = method(yaml_script)
            print(f'{method.__name__}({yaml_script}) => {result}')
        except Exception as e:
            print(f'{method.__name__}({yaml_script}) raised 
{e.__class__.__name__}: {str(e)}')
    elif method == parser.readYAMLAsStr or method == parser.loadMultiYAML:
        path_script = 'path/to/yaml/file'

        # Call the method with the random input
        try:
            result = method(path_script)
            print(f'{method.__name__}({path_script}) => {result}')
        except Exception as e:
            print(f'{method.__name__}({path_script}) raised 
{e.__class__.__name__}: {str(e)}')

if __name__ == '__main__':
    for i in range(10):
        fuzz()
