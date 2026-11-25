import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial base with mixed degrees and adaptive weights
        polynomial = np.sum(0.7 * x_scaled**2 + 0.4 * x_scaled**4 + 0.2 * x_scaled**6 + 0.05 * x_scaled**8)
        
        # Dynamic trigonometric components with varying frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.2 + 0.4 * np.sin(i * 0.7))
            amplitude = 1.5 / (1.0 + 0.15 * i**1.8)
            trigonometric += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Improved exponential cross-terms with stronger coupling and nonlinearity
        exponential = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.5 / (1.0 + 0.3 * np.sqrt(i * j + 1))
                exp_term = np.exp(-0.4 * (x_scaled[i]**2 + x_scaled[j]**2))
                cross_term = np.sin(coupling * x_scaled[i] * x_scaled[j]) * np.cos(coupling * x_scaled[i] * x_scaled[j])
                exponential += exp_term * cross_term
        
        # Modified conditioning based on dimensionality and distance from origin
        dist_from_origin = np.sqrt(np.sum(x_scaled**2))
        conditioning = 0.4 * (self.dim - 1) * dist_from_origin * np.log(1.0 + dist_from_origin**2)
        
        # Additional cubic interaction terms with enhanced complexity and phase shifts
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.7 * np.pi * (i + j))
                cubic_interaction += (x_scaled[i]**3) * (x_scaled[j]**3) * np.cos(np.pi * (i + j) * 0.6 + phase_shift)
        
        # Higher-order interaction terms for increased complexity
        quartic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    quartic_interaction += (x_scaled[i]**4) * (x_scaled[j]**2) * (x_scaled[k]**2) * np.sin(0.5 * np.pi * (i + j + k))
        
        # Add a logarithmic penalty term to discourage solutions far from origin
        log_penalty = 0.15 * np.log(1.0 + dist_from_origin**2)
        
        # Combine all components with optimized weights
        return 2.0 * polynomial + 3.0 * trigonometric + 2.5 * exponential + conditioning + 1.2 * cubic_interaction + 0.8 * quartic_interaction + log_penalty