import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified polynomial chaos expansion with higher degree terms
        poly_term = np.sum((x_norm ** 6 - 3 * x_norm ** 4 + 3 * x_norm ** 2 - 1) * np.cos(4 * np.pi * x_norm))
        
        # Enhanced radial basis function components with variable widths and shifted centers
        rbfs = []
        centers = np.linspace(-0.8, 0.8, min(7, self.dim))
        for c in centers:
            rbf = np.exp(-15 * (x_norm - c) ** 2)
            rbfs.append(np.sum(rbf))
        rbf_term = np.sum(rbfs)
        
        # Modified quaternion-inspired interaction terms with different coupling
        quat_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                xi, xj = x_norm[i], x_norm[i+1]
                quat_term += (xi ** 2 * xj ** 2) * np.sin(3 * np.pi * (xi - xj))
        
        # Adjusted sine-cosine coupled oscillations with different frequencies
        osc_term = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Combined result with updated dynamic weighting
        weight1, weight2, weight3, weight4 = 0.3, 0.25, 0.25, 0.2
        result = weight1 * poly_term + weight2 * rbf_term + weight3 * quat_term + weight4 * osc_term
        
        # Add a global scaling and offset to ensure positive fitness values
        result += 0.3 * np.sum(x_norm ** 2)
        
        return result