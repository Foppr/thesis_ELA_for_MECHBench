import numpy as np

class HybridRotatingMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for dimensionality
        self.rotation_matrix = np.random.rand(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        spherical = np.sum(x**2)
        
        # Step function component with asymmetric thresholds
        step = 0
        for i in range(self.dim):
            if x[i] > 0:
                step += np.floor(x[i] * 0.5) * (x[i] - 1)
            else:
                step += np.ceil(x[i] * 0.3) * (x[i] + 1)
        
        # Gaussian peaks with varying heights and widths
        gaussian = 0
        peaks = 5
        for i in range(peaks):
            peak_x = np.random.uniform(-5, 5, self.dim)
            height = np.random.uniform(1, 10)
            width = np.random.uniform(0.5, 2.0)
            gaussian += height * np.exp(-np.sum(((x - peak_x) / width)**2) / 2)
        
        # Rotated cross-dimensional coupling with asymmetric interaction
        rotated = np.dot(self.rotation_matrix, x)
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.1 * rotated[i] * rotated[j] * np.sin(0.5 * (rotated[i]**2 + rotated[j]**2))
        
        # Asymmetric saddle point structure
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2 * x[i]**2 + 0.5 * x[i]) * np.cos(0.3 * x[i])
        
        # Chaotic modulation with logistic map
        chaotic = 0
        r = 3.9  # Logistic map parameter
        for i in range(self.dim):
            chaotic += np.sin(x[i]) * np.cos(0.2 * x[i]) * np.tanh(x[i]**3)
        
        # Combined fitness
        return spherical + step + gaussian + cross + saddle + chaotic