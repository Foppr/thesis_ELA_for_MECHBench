import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic components with enhanced conditioning
        quadratic = 0
        for i in range(self.dim):
            cond_num = 15**(0.3 * np.sin(0.4 * i) + 1.2)
            quadratic += cond_num * x[i]**2
        
        # Enhanced sine-wave coupling with frequency modulation and phase shifts
        sine_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.5 + 0.7 * np.sin(0.5 * i + 0.3)
                freq_j = 1.5 + 0.7 * np.cos(0.5 * j + 0.7)
                amp = 0.4 + 0.3 * np.sin(0.7 * (i + j) + 0.5)
                phase_shift = 0.2 * np.sin(0.6 * i + 0.8 * j)
                sine_coupling += amp * np.sin(freq_i * x[i] + phase_shift) * np.cos(freq_j * x[j] + phase_shift)
        
        # Modified Gaussian radial basis functions with dynamic centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 4.0 * np.sin(0.6 * i + 1.2)
            width = 1.0 + 0.5 * np.cos(0.8 * i + 0.4)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Enhanced cross-dimensional interaction with higher-order polynomials
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                power = 3 + int(4 * np.sin(0.6 * (i + j) + 0.5))
                cross_interaction += (x[i]**power + x[j]**power) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Enhanced dynamic conditioning with cubic terms
        conditioning = 0
        for i in range(self.dim):
            condition_factor = 1.5 + 0.4 * np.sin(0.9 * i + 0.6)
            conditioning += condition_factor * x[i]**3
        
        # Combine all components with adjusted scaling factors
        return 1.0 * quadratic + 1.5 * sine_coupling + 0.7 * rbf + 1.1 * cross_interaction + 1.8 * conditioning