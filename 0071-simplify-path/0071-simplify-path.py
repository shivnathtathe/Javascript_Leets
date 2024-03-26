class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if path[-1] == '/':
            path = path[:-1]
        
        components = path.split('/')
        simplified_path = []
        
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if simplified_path:
                    simplified_path.pop()
            else:
                simplified_path.append(component)
        
        
        return '/' + '/'.join(simplified_path)
