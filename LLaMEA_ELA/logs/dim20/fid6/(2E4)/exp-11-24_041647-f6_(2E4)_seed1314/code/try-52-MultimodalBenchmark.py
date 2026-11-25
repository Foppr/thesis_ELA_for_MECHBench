import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin with dimension-dependent scaling
        quadratic_term = 0.1 * np.sum(x_normalized**2)
        
        # Periodic oscillations with varying frequencies and amplitudes
        periodic_term = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi
            amplitude = 1.0 / (1.0 + 0.1 * i)
            periodic_term += amplitude * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
        
        # Asymmetric saddle points with exponential decay
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.05 * (x_normalized[i]**3 - 3*x_normalized[i]**2) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Cross-dimensional interaction with trigonometric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.02 * np.sin(3 * x_normalized[i]) * np.cos(5 * x_normalized[j])
        
        # Dimension-dependent conditioning factor
        condition_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Add a chaotic component with recursive feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 0.03 * np.sin(7 * x_normalized[i]) * np.cos(11 * x_normalized[i]) * (1 + 0.1 * np.sin(x_normalized[i]))
        
        # Hyperbolic tangent modulation for enhanced nonlinearity
        tanh_modulation = 0.0
        for i in range(self.dim):
            tanh_modulation += 0.04 * np.tanh(2.0 * x_normalized[i]) * np.sin(9 * x_normalized[i])
        
        # Logarithmic barrier near boundaries to enforce constraints
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += 0.025 * (1 / (1 - x_normalized[i]**2 + 1e-8) - 1)
        
        return condition_factor * (quadratic_term + periodic_term + saddle_term + cross_term + chaotic_term + tanh_modulation + barrier_term)