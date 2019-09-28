def package_dependency(dependencies):

    result = []
    visiting = set([])
    visited = set([])

    def dfs(node):
        if node in visited:
            return
        visiting.add(node)
        for neighbors in dependencies[node]:
            if neighbors in visiting:
                raise Exception("have cycle")
            if neighbors not in visited:
                dfs(neighbors)

        visiting.remove(node)
        visited.add(node)
        result.append(node)

    for node in dependencies.keys():
        dfs(node)

    return result

dict = {0: [], 1: [0], 2:[0], 3:[1,2], 4:[3]}
dict[0] = []
dict[1] = [0]
dict[2] = [0]
dict[3] = [1,2]
dict[4] = [3]

print(package_dependency(dict))