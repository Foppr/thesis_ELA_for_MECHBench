import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos expansion with higher order terms
        poly_term = np.sum((x_norm ** 6 - 3 * x_norm ** 4 + 3 * x_norm ** 2 - 1) * np.sin(4 * np.pi * x_norm))
        
        # Improved radial basis function components with adaptive widths
        rbf_term = 0
        for i in range(min(7, self.dim)):
            center = np.sin(i * np.pi / 4)
            width = 0.5 + 0.5 * np.cos(i * np.pi / 3)
            rbf = np.exp(-15 * (x_norm - center) ** 2 / width)
            rbf_term += np.sum(rbf)
        
        # Modified quaternion-inspired interaction terms with coupling strength
        quat_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                xi, xj = x_norm[i], x_norm[i+1]
                coupling = 0.5 * (1 + np.cos(np.pi * (xi + xj)))
                quat_term += coupling * (xi ** 2 + xj ** 2) * np.cos(3 * np.pi * (xi - xj))
        
        # Enhanced oscillatory terms with frequency modulation
        osc_term = 0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * np.pi / self.dim)
            osc_term += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Combined result with refined weighting scheme
        weight1, weight2, weight3, weight4 = 0.3, 0.25, 0.25, 0.2
        result = weight1 * poly_term + weight2 * rbf_term + weight3 * quat_term + weight4 * osc_term
        
        # Add a modified quadratic penalty term for better conditioning
        result += 0.3 * np.sum(x_norm ** 2)
        
        return result