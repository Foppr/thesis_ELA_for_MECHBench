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
            cond_num = 20**(0.4 * np.sin(0.8 * i) + 1.3)
            quadratic += cond_num * x[i]**2
        
        # Chaotic sine-wave coupling with non-linear modulation and dynamic phase shifts
        sine_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2.0 + 0.9 * np.sin(0.7 * i + 0.4)
                freq_j = 2.0 + 0.9 * np.cos(0.7 * j + 0.4)
                amp = 0.5 + 0.4 * np.sin(0.6 * (i - j) + 1.2)
                phase_i = 0.3 * np.sin(0.5 * i + 0.8)
                phase_j = 0.3 * np.cos(0.5 * j + 0.8)
                sine_coupling += amp * np.sin(freq_i * x[i] + phase_i) * np.cos(freq_j * x[j] + phase_j)
        
        # Adaptive Gaussian radial basis functions with time-varying centers, widths, and amplitudes
        rbf = 0
        for i in range(self.dim):
            center = 4.5 * np.sin(0.7 * i + 1.8)
            width = 1.2 + 0.6 * np.cos(0.9 * i + 0.6)
            amplitude = 0.8 + 0.3 * np.sin(0.6 * i + 1.1)
            rbf += amplitude * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Modified cross-dimensional interaction with exponential weighting and dynamic powers
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                power = 4 + int(3 * np.sin(0.5 * (i + j)) + 2)
                weight = np.exp(-0.07 * (x[i]**2 + x[j]**2))
                cross_interaction += (x[i]**power + x[j]**power) * weight
        
        # Enhanced dynamic conditioning with polynomial scaling and chaotic modulation
        conditioning = 0
        for i in range(self.dim):
            condition_factor = 2.0 + 0.5 * np.sin(1.2 * i + 0.8)
            conditioning += condition_factor * x[i]**4
        
        # Additional chaotic harmonic coupling with multi-scale frequency components
        harmonic_coupling = 0
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(0.9 * i + 0.3)
            freq2 = 1.5 + 0.6 * np.cos(0.9 * i + 0.3)
            harmonic_coupling += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
        
        # Combine all components with adjusted scaling factors
        return 1.2 * quadratic + 1.8 * sine_coupling + 0.9 * rbf + 1.3 * cross_interaction + 1.5 * conditioning + 0.7 * harmonic_coupling