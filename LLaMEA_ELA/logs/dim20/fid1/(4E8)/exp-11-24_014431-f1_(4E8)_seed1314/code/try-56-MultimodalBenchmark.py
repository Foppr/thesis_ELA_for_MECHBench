import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Chaotic sine-wave interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 2.0 * np.sin(10 * x[i]) * np.cos(7 * x[i]) + 1.5 * np.sin(15 * x[i])
            
        # Adaptive polynomial conditioning with dimension-dependent exponents
        for i in range(self.dim):
            exp_factor = 2 + 0.5 * np.sin(i)
            f_val += 0.8 * (x[i]**exp_factor) * np.cos(3 * x[i]) + 0.3 * (x[i]**(exp_factor + 1)) * np.sin(2 * x[i])
            
        # Cross-dimensional exponential penalties with varying decay rates
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x[i] - x[j])**2 + 0.01)
                decay_rate = 0.5 + 0.3 * np.sin(i * 0.5)
                f_val += 1.2 * np.exp(-decay_rate * distance**2) * np.sin(3 * np.pi * (x[i] + x[j]))
                
        # Multi-scale radial basis interactions with dynamic centers
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                center_i = 2 * np.sin(i * 0.3)
                center_j = 2 * np.cos(j * 0.3)
                distance = np.sqrt((x[i] - center_i)**2 + (x[j] - center_j)**2 + 0.1)
                f_val += 0.5 * np.exp(-distance**2) * np.cos(4 * np.pi * (x[i] + x[j]))
                
        # Enhanced harmonic terms with chaotic phase modulation
        for i in range(self.dim):
            phase_mod = 0.5 * np.sin(x[i] * 0.7) * np.cos(x[i] * 0.3)
            f_val += 1.0 * np.sin(12 * x[i] + phase_mod) * np.cos(5 * x[i]) + 0.8 * np.sin(18 * x[i] + phase_mod)
            
        # Global conditioning with super-quadratic terms and noise injection
        noise_term = 0.05 * np.sum(np.random.randn(self.dim) * x)
        f_val += 0.1 * np.sum(x**8) + 0.05 * np.sum(x**14) + noise_term
        
        return f_val