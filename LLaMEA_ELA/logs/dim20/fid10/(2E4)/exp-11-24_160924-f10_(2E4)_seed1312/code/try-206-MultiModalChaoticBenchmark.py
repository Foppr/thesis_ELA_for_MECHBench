import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for each dimension
        np.random.seed(42)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.frequencies = np.random.uniform(1.0, 6.0, dim)
        self.decay_rates = np.random.uniform(0.1, 1.5, dim)
        self.saddle_weights = np.random.uniform(-1.0, 1.0, dim)
        self.interference_strengths = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add multi-modal sinusoidal components with exponential decay
        for i in range(self.dim):
            xi = x[i]
            amp = self.amplitudes[i]
            freq = self.frequencies[i]
            decay = self.decay_rates[i]
            
            # Exponentially decaying sinusoidal term
            term1 = amp * np.exp(-decay * np.abs(xi)) * np.sin(freq * xi)
            
            # Asymmetric saddle point contribution
            saddle_contribution = self.saddle_weights[i] * xi**2 * np.cos(xi)
            
            result += term1 + saddle_contribution
            
        # Add cross-dimensional interference with asymmetric coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                interference = self.interference_strengths[i] * np.exp(-0.5 * (xi**2 + xj**2)) * np.sin(xi * xj)
                
                # Asymmetric interaction based on dimension indices
                asymmetry = 1.0 + 0.3 * np.sin(0.5 * (i - j))
                result += asymmetry * interference
                
        # Add global scaling and multi-modal complexity
        global_scaling = 1.0 + 0.2 * np.sin(0.3 * self.dim)
        result *= global_scaling
        
        # Add chaotic modulation with varying amplitudes
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = 0.5 + 0.3 * np.sin(0.7 * i)
            chaotic_component += amp * np.exp(-0.1 * xi**2) * np.cos(4.0 * xi)
            
        result += 0.05 * chaotic_component
        
        # Add ridge-like structure with varying heights
        ridge_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_height = 0.1 + 0.2 * np.sin(0.6 * i)
            ridge_penalty += ridge_height * np.sin(2.0 * xi)**2
            
        result += ridge_penalty
        
        return result