import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial chaos expansion with trigonometric modulations
        poly_term = np.sum((x_norm ** 8 - 4 * x_norm ** 6 + 6 * x_norm ** 4 - 4 * x_norm ** 2 + 1) * 
                          np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Modified radial basis functions with adaptive widths and multiple centers
        rbf_term = 0
        for i in range(min(5, self.dim)):
            center = np.sin(i * np.pi / 4)
            width = 10 + 5 * np.sin(i * np.pi / 3)
            rbf_term += np.exp(-width * (x_norm - center) ** 2)
        
        # Novel quaternion-inspired coupling with phase shifts and amplitude modulation
        quat_term = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                xi, xj = x_norm[i], x_norm[i+1]
                phase = np.sin(2 * np.pi * (xi + xj))
                amplitude = 1 + 0.5 * np.cos(3 * np.pi * xi)
                quat_term += amplitude * (xi ** 2 * xj ** 2) * np.sin(4 * np.pi * (xi - xj) + phase)
        
        # Combined oscillatory components with varying frequencies and damping
        osc_term = np.sum(np.sin(6 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                         np.exp(-0.5 * x_norm ** 2))
        
        # Dynamic weighting based on dimensionality
        weight1, weight2, weight3, weight4 = 0.25, 0.3, 0.2, 0.25
        result = weight1 * poly_term + weight2 * rbf_term + weight3 * quat_term + weight4 * osc_term
        
        # Add a global quadratic penalty to encourage convergence to the global minimum
        result += 0.2 * np.sum(x_norm ** 2) + 0.1 * np.sum(np.abs(x_norm) ** 3)
        
        return result