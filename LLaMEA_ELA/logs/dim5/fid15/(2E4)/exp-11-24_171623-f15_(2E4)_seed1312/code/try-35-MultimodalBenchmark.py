import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion terms with varying degrees
        poly_term = np.sum((x_norm ** 4 - 2 * x_norm ** 2 + 1) * np.cos(3 * np.pi * x_norm))
        
        # Radial basis function components with different centers and widths
        rbfs = []
        centers = np.linspace(-1, 1, min(5, self.dim))
        for c in centers:
            rbf = np.exp(-10 * (x_norm - c) ** 2)
            rbfs.append(np.sum(rbf))
        rbf_term = np.sum(rbfs)
        
        # Quaternion-inspired interaction terms
        quat_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                xi, xj = x_norm[i], x_norm[i+1]
                quat_term += (xi ** 2 + xj ** 2) * np.sin(2 * np.pi * (xi + xj))
        
        # Sine-cosine coupled oscillations with phase shifts
        osc_term = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Combined result with dynamic weighting based on dimensionality
        weight1, weight2, weight3, weight4 = 0.25, 0.35, 0.2, 0.2
        result = weight1 * poly_term + weight2 * rbf_term + weight3 * quat_term + weight4 * osc_term
        
        # Add a global scaling and offset to ensure positive fitness values
        result += 0.5 * np.sum(x_norm ** 2)
        
        return result