import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic components with chaotic condition numbers
        quadratic = 0
        for i in range(self.dim):
            cond_num = 10**(0.3 * np.sin(0.9 * i) + 1.1)
            quadratic += cond_num * x[i]**2
        
        # Chaotic sine-wave coupling with non-linear modulation
        sine_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.3 + 0.8 * np.sin(0.6 * i + 0.5)
                freq_j = 1.3 + 0.8 * np.cos(0.6 * j + 0.5)
                amp = 0.6 + 0.1 * np.sin(0.7 * (i - j) + 1.1)
                sine_coupling += amp * np.sin(freq_i * x[i] + 0.2 * np.cos(freq_j * x[j])) * np.cos(freq_j * x[j] + 0.2 * np.sin(freq_i * x[i]))
        
        # Adaptive Gaussian radial basis functions with time-varying centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 3.0 * np.sin(0.8 * i + 1.1)
            width = 1.3 + 0.3 * np.cos(0.8 * i + 0.5)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Modified cross-dimensional interaction with exponential weighting
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                power = 3 + int(2.0 * np.sin(0.4 * (i + j)) + 1)
                weight = np.exp(-0.02 * (x[i]**2 + x[j]**2))
                cross_interaction += (x[i]**power + x[j]**power) * weight
        
        # Enhanced dynamic conditioning with polynomial scaling
        conditioning = 0
        for i in range(self.dim):
            condition_factor = 1.9 + 0.2 * np.sin(1.1 * i + 0.7)
            conditioning += condition_factor * x[i]**3
        
        # Combine all components with adjusted scaling factors for better fitness
        return 1.1 * quadratic + 1.4 * sine_coupling + 0.8 * rbf + 1.1 * cross_interaction + 1.3 * conditioning