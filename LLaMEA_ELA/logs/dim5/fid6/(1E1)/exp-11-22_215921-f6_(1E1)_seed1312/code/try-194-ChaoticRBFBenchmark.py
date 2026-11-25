import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested chaotic RBF with multiple nested valleys and varying amplitudes
        rbf = 0.0
        for i in range(self.dim):
            sigma = 0.4 + 0.3 * np.sin(i * np.pi / self.dim) + 0.1 * np.cos(i * np.pi / (self.dim + 2))
            amp = 1.5 + 0.5 * np.sin(2 * i * np.pi / self.dim)
            rbf += amp * np.exp(-0.5 * (x_norm[i] / sigma)**2) * (1 + 0.3 * np.sin(5 * x_norm[i]))
        
        # Hyperchaotic tent map with 4D coupling
        tent_map = 0.0
        for i in range(self.dim - 3):
            xi, xi1, xi2, xi3 = x_norm[i], x_norm[i+1], x_norm[i+2], x_norm[i+3]
            tent_val = 2 * np.abs(xi - 0.5)
            tent_val1 = 2 * np.abs(xi1 - 0.5)
            tent_val2 = 2 * np.abs(xi2 - 0.5)
            tent_val3 = 2 * np.abs(xi3 - 0.5)
            tent_map += tent_val * tent_val1 * tent_val2 * tent_val3
        
        # Saddle structure with higher-order polynomial gradients
        saddle = 0.0
        for i in range(self.dim - 1):
            xi = x_norm[i]
            xi1 = x_norm[i + 1]
            grad_term = (xi**5 - 2*xi**3 + xi) * (xi1**5 - 2*xi1**3 + xi1)
            saddle += grad_term
        
        # Cross-dimensional coupling with logistic and sine dynamics
        logistic_coupling = 0.0
        r = 3.95
        for i in range(self.dim - 1):
            xi = x_norm[i]
            xi1 = x_norm[i + 1]
            logistic_val = r * xi * (1 - xi)
            sine_val = np.sin(3 * xi1)
            logistic_coupling += logistic_val * sine_val
        
        # High-frequency oscillatory component with dynamic phase shifts
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 30 + 5 * np.sin(i * np.pi / self.dim)
            phase = 0.5 * np.cos(i * np.pi / (self.dim + 1))
            oscillatory += np.sin(freq * x_norm[i] + phase) * np.exp(-0.2 * x_norm[i]**2)
        
        # Enhanced conditioning with fractal-like scaling
        condition_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi / 5.0) + 0.2 * np.log(self.dim + 2) + 0.1 * np.cos(self.dim * np.pi / 3.0)
        
        # Adaptive coupling with chaotic weight modulation
        coupling_factor = 1.0 + 0.2 * np.sin(0.8 * self.dim * np.pi / 6.0) + 0.15 * np.cos(0.4 * self.dim * np.pi / 7.0)
        
        # Combine all terms with enhanced interaction
        return coupling_factor * (tent_map + rbf + saddle + logistic_coupling + oscillatory) * condition_factor