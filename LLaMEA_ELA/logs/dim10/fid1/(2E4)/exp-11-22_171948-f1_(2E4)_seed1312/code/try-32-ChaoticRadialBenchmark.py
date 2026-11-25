import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Radial basis function component with chaotic modulation
        for i in range(self.dim):
            # Radial distance from origin with chaotic scaling
            r = np.sqrt(np.sum(x**2))
            radial_basis = np.exp(-0.1 * (r - 2.5)**2) * np.sin(3 * r)
            result += radial_basis
        
        # Sinusoidal modulation with adaptive frequency
        for i in range(self.dim):
            # Adaptive frequency based on position
            freq = 2 + 0.5 * np.sin(x[i])
            sin_mod = np.sin(freq * x[i]) * np.cos(0.5 * x[i]**2)
            result += 0.7 * sin_mod
        
        # Multi-scale chaotic oscillation
        for i in range(self.dim):
            # Nested chaotic oscillations with varying amplitudes
            chaotic_osc = (np.sin(10 * x[i]) + 
                          0.5 * np.sin(30 * x[i]) + 
                          0.2 * np.sin(90 * x[i]))
            result += 0.4 * chaotic_osc**2
        
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim - 1):
            coupling = np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(5 * (x[i] + x[i+1]))
            result += 0.3 * coupling
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.3 * np.sin(self.dim)
        for i in range(self.dim):
            # Conditioned polynomial with chaotic behavior
            poly_term = condition_factor * (0.01 * x[i]**6 - 0.1 * x[i]**4 + 0.3 * x[i]**2)
            result += poly_term
        
        # Fractal-like ridge structure
        for i in range(self.dim):
            ridge = 0.5 * np.sin(20 * x[i]) * np.exp(-0.05 * x[i]**2) + \
                   0.3 * np.cos(15 * x[i]) * np.exp(-0.02 * x[i]**2)
            result += ridge
        
        # Stochastic perturbation with adaptive strength
        stochastic = 0.0
        for i in range(self.dim):
            # Random phase modulation
            phase = np.random.rand() * np.pi
            stochastic += np.sin(8 * x[i] + phase) * np.cos(4 * x[i] + phase)
        result += 0.2 * stochastic
        
        # Multi-modal component with varying peak locations
        for i in range(self.dim):
            multimodal = (np.sin(15 * x[i]) + 
                         0.7 * np.sin(45 * x[i]) + 
                         0.3 * np.sin(75 * x[i]))
            result += 0.6 * multimodal**3
        
        # Global scaling with dynamic adjustment
        global_scaling = 1.0 + 0.2 * np.sin(np.sum(x) / self.dim)
        result *= global_scaling
        
        # Normalize by dimension
        result /= self.dim
        
        return result