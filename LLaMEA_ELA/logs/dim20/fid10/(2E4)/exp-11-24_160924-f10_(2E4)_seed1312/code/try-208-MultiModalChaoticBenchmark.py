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
        self.ridge_heights = np.random.uniform(0.05, 0.3, dim)
        self.chaotic_amplitudes = np.random.uniform(0.3, 0.7, dim)
        
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
            
            # Enhanced asymmetric saddle point contribution with variable weight
            saddle_contribution = self.saddle_weights[i] * xi**2 * np.cos(xi) * (1.0 + 0.2 * np.sin(0.5 * i))
            
            result += term1 + saddle_contribution
            
        # Add cross-dimensional interference with enhanced asymmetry and coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                interference = self.interference_strengths[i] * np.exp(-0.5 * (xi**2 + xj**2)) * np.sin(xi * xj)
                
                # Enhanced asymmetric interaction based on dimension indices
                asymmetry = 1.0 + 0.4 * np.sin(0.7 * (i - j)) * np.cos(0.3 * (i + j))
                result += asymmetry * interference
                
        # Add enhanced global scaling and multi-modal complexity
        global_scaling = 1.0 + 0.3 * np.sin(0.4 * self.dim)
        result *= global_scaling
        
        # Add enhanced chaotic modulation with varying amplitudes and phase shifts
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = self.chaotic_amplitudes[i]
            phase_shift = 0.2 * np.cos(0.5 * i)
            chaotic_component += amp * np.exp(-0.1 * xi**2) * np.cos(4.0 * xi + phase_shift)
            
        result += 0.08 * chaotic_component
        
        # Add enhanced ridge-like structure with varying heights and widths
        ridge_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_height = self.ridge_heights[i]
            ridge_width = 0.5 + 0.3 * np.sin(0.4 * i)
            ridge_penalty += ridge_height * np.sin(2.0 * xi / ridge_width)**2
            
        result += ridge_penalty
        
        # Add noise component to increase robustness
        noise = 0.01 * np.sum(np.random.uniform(-1, 1, self.dim) * x**2)
        result += noise
        
        return result