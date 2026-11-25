import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial component with chaotic coefficients
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.sin(i * 2.5 + x[i])
            poly_term = coeff * (x[i]**4 - 2 * x[i]**2 + 1)
            result += 0.5 * poly_term
        
        # Trigonometric modulation with varying frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.cos(x[i])
            trig_term = np.sin(freq * x[i]) * np.cos(2 * x[i])
            result += 0.3 * trig_term
        
        # Exponential decay with adaptive rate
        for i in range(self.dim):
            exp_decay = np.exp(-0.1 * (x[i] - 1.0)**2) * np.sin(5 * x[i])
            result += 0.4 * exp_decay
        
        # Cross-dimensional interference with sine coupling
        for i in range(self.dim - 1):
            coupling = np.sin(x[i] + x[i+1]) * np.exp(-0.05 * (x[i] - x[i+1])**2)
            result += 0.2 * coupling
        
        # Multi-scale oscillation with dynamic amplitude
        for i in range(self.dim):
            amp = 0.5 + 0.5 * np.sin(x[i] * 3)
            oscillation = amp * np.sin(10 * x[i]) + 0.3 * np.sin(30 * x[i])
            result += 0.6 * oscillation**2
        
        # Adaptive conditioning based on dimension
        cond_factor = 1.0 + 0.4 * np.cos(self.dim)
        for i in range(self.dim):
            conditioned_term = cond_factor * (x[i]**3 - 0.5 * x[i])
            result += 0.1 * conditioned_term
        
        # Ridge structure with varying heights
        for i in range(self.dim):
            ridge_height = 0.8 + 0.2 * np.sin(4 * x[i])
            ridge = ridge_height * np.exp(-0.5 * (x[i] - 2.0)**2)
            result += 0.3 * ridge
        
        # Stochastic perturbation with dynamic strength
        stochastic = 0.0
        for i in range(self.dim):
            noise_amp = 0.1 + 0.05 * np.sin(i * 1.5)
            noise = noise_amp * np.random.randn()
            stochastic += noise * np.cos(3 * x[i])
        result += 0.2 * stochastic
        
        # Multi-modal structure with varying peak positions
        for i in range(self.dim):
            modal_component = (np.sin(8 * x[i]) + 
                             0.6 * np.sin(24 * x[i]) + 
                             0.2 * np.sin(48 * x[i]))
            result += 0.5 * modal_component**3
        
        # Global scaling factor
        global_scale = 1.0 + 0.3 * np.cos(np.sum(x) / self.dim)
        result *= global_scale
        
        # Normalize by dimension
        result /= self.dim
        
        return result