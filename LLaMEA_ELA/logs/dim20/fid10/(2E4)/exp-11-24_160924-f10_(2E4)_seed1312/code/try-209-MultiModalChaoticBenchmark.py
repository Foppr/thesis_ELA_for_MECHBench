import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random parameters for each dimension
        np.random.seed(42)
        self.amplitudes = np.random.uniform(0.3, 1.8, dim)
        self.frequencies = np.random.uniform(0.8, 5.5, dim)
        self.decay_rates = np.random.uniform(0.05, 1.2, dim)
        self.saddle_weights = np.random.uniform(-0.8, 0.8, dim)
        self.interference_strengths = np.random.uniform(0.05, 0.7, dim)
        
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
            
            # Exponentially decaying sinusoidal term with modified phase
            term1 = amp * np.exp(-decay * np.abs(xi)) * np.sin(freq * xi + 0.5 * i)
            
            # Enhanced asymmetric saddle point contribution with variable dominance
            saddle_contribution = self.saddle_weights[i] * xi**2 * np.cos(0.7 * xi + 0.3 * i)
            
            result += term1 + saddle_contribution
            
        # Add cross-dimensional interference with enhanced asymmetry and coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                interference = self.interference_strengths[i] * np.exp(-0.3 * (xi**2 + xj**2)) * np.sin(xi * xj + 0.2 * (i - j))
                
                # Enhanced asymmetric interaction based on dimension indices
                asymmetry = 1.0 + 0.4 * np.sin(0.6 * (i - j) + 0.1 * i)
                result += asymmetry * interference
                
        # Add global scaling with modified harmonic components
        global_scaling = 1.0 + 0.15 * np.sin(0.2 * self.dim + 0.3 * np.sum(x))
        result *= global_scaling
        
        # Add enhanced chaotic modulation with dynamic amplitudes
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = 0.4 + 0.25 * np.sin(0.8 * i + 0.1 * np.sum(x))
            chaotic_component += amp * np.exp(-0.12 * xi**2) * np.cos(3.5 * xi + 0.2 * i)
            
        result += 0.06 * chaotic_component
        
        # Add refined ridge-like structure with variable heights and widths
        ridge_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_height = 0.12 + 0.18 * np.sin(0.5 * i + 0.2 * np.sum(x))
            ridge_width = 0.8 + 0.4 * np.cos(0.3 * i)
            ridge_penalty += ridge_height * np.sin(ridge_width * xi)**2
            
        result += ridge_penalty
        
        # Add noise-like perturbations to increase landscape complexity
        noise_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            noise_term += 0.02 * np.sin(7.0 * xi + 0.1 * i) * np.cos(3.0 * xi + 0.05 * np.sum(x))
            
        result += noise_term
        
        return result