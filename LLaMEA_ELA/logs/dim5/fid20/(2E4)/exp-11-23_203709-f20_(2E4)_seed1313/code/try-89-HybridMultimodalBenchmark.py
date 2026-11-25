import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic components with dimensionally varying condition numbers
        quadratic = 0
        for i in range(self.dim):
            cond_num = 10**(0.5 * np.sin(0.3 * i) + 1.0)
            quadratic += cond_num * x[i]**2
        
        # Sine-wave coupling between dimensions with varying frequencies and amplitudes
        sine_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.5 * np.sin(0.4 * i)
                freq_j = 1.0 + 0.5 * np.cos(0.4 * j)
                amp = 0.3 + 0.2 * np.sin(0.6 * (i + j))
                sine_coupling += amp * np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Gaussian radial basis functions with dynamic centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 3.0 * np.sin(0.5 * i + 1.0)
            width = 0.8 + 0.4 * np.cos(0.7 * i)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional interaction with polynomial weighting
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                power = 2 + int(3 * np.sin(0.5 * (i + j)))
                cross_interaction += (x[i]**power + x[j]**power) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Dynamic conditioning based on dimension index
        conditioning = 0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.3 * np.sin(0.8 * i + 0.5)
            conditioning += condition_factor * x[i]**4
        
        # Combine all components with appropriate scaling
        return 0.8 * quadratic + 1.2 * sine_coupling + 0.6 * rbf + 0.9 * cross_interaction + 1.5 * conditioning