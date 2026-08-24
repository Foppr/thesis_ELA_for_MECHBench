import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add time-varying harmonic potentials with chaotic modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation using sine-Gordon-like dynamics
            freq = 10 + 5 * np.sin(3 * x[i]) + 2 * np.cos(7 * x[i])
            harmonic_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-i / self.dim)
        
        # Multi-scale saddle point structure with varying curvature
        saddle_term = 0.0
        for i in range(self.dim):
            # Create saddle points with varying depth and position
            depth = 0.5 * (1 + np.sin(i * np.pi / 4.0))
            pos = 0.3 * np.cos(i * np.pi / 3.0)
            saddle_term += depth * (x[i] - pos)**2 * (x[i] + pos)**2
        
        # Adaptive noise component that changes with input
        noise_term = 0.0
        for i in range(self.dim):
            # Noise amplitude varies with position and dimension
            amp = 0.1 * (1 + np.sin(x[i] * 2)) * (1 + 0.1 * i / self.dim)
            noise_term += amp * np.sin(50 * x[i] + i) * np.cos(30 * x[i] + i)
        
        # Dynamic coupling between dimensions with phase shift
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(x[i] + x[j] + i * j * 0.1) * np.cos(x[i] - x[j] + i + j)
        
        # Add all components to the result
        result += 0.3 * harmonic_term + 0.2 * saddle_term + 0.1 * noise_term + 0.4 * coupling_term
        
        return result