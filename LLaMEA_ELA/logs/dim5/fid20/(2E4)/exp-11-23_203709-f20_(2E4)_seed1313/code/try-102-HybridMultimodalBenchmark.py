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
            cond_num = 15**(0.3 * np.sin(0.7 * i) + 1.2)
            quadratic += cond_num * x[i]**2
        
        # Chaotic sine-wave coupling with non-linear modulation
        sine_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.5 + 0.8 * np.sin(0.6 * i + 0.3)
                freq_j = 1.5 + 0.8 * np.cos(0.6 * j + 0.3)
                amp = 0.4 + 0.3 * np.sin(0.5 * (i - j) + 1.0)
                sine_coupling += amp * np.sin(freq_i * x[i] + 0.2 * np.cos(freq_j * x[j])) * np.cos(freq_j * x[j] + 0.2 * np.sin(freq_i * x[i]))
        
        # Adaptive Gaussian radial basis functions with time-varying centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 4.0 * np.sin(0.6 * i + 1.5)
            width = 1.0 + 0.5 * np.cos(0.8 * i + 0.5)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Modified cross-dimensional interaction with exponential weighting and altered exponents
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                power = 4 + int(3 * np.sin(0.4 * (i + j)) + 2)  # Increased exponent variability
                weight = np.exp(-0.07 * (x[i]**2 + x[j]**2))   # Slightly stronger weighting
                cross_interaction += (x[i]**power + x[j]**power) * weight
        
        # Enhanced dynamic conditioning with polynomial scaling
        conditioning = 0
        for i in range(self.dim):
            condition_factor = 1.5 + 0.4 * np.sin(1.0 * i + 0.7)
            conditioning += condition_factor * x[i]**3
        
        # Combine all components with adjusted scaling factors
        return 1.2 * quadratic + 1.7 * sine_coupling + 0.9 * rbf + 1.2 * cross_interaction + 1.4 * conditioning