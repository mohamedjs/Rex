from numpy import dot

from numpy.linalg import norm

cosine = lambda v1, v2: dot(v1, v2) / (norm(v1) * norm(v2))

print(cosine([1, 1, 1, 0], [1, 1, 0, 1]))
