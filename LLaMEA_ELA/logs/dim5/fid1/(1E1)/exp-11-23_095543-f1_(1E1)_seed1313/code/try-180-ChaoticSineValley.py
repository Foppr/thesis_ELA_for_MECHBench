import numpy as np

class ChaoticSineValley:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with dimension-dependent scaling
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2 * (1.0 + 0.1 * np.sin(10 * x[i]))
            
        # Add chaotic sine-wave interactions with directional bias
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += 0.3 * np.sin(8 * x[i] + 2 * x[j]) * np.cos(5 * x[i] - 3 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                    
        # Add adaptive scaling based on dimension and position
        adaptive_scale = 1.0 + 0.2 * np.sin(3 * np.sum(x)) * np.cos(2 * np.sum(x**2))
        result *= adaptive_scale
        
        # Add directional bias with exponential decay
        direction_bias = 0.0
        for i in range(self.dim):
            direction_bias += 0.4 * x[i] * np.sin(7 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += direction_bias
        
        # Add multi-scale chaotic components with varying frequencies
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += 0.25 * np.sin(15 * x[i] + 3 * np.sin(8 * x[i])) * np.cos(12 * x[(i+1) % self.dim] + 2 * np.cos(7 * x[(i+1) % self.dim]))
        result += chaotic_component
        
        # Add valley-forming sinusoidal ridges
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.35 * np.sin(4 * x[i]) * np.cos(6 * x[(i+2) % self.dim]) * (1 + 0.2 * np.sin(3 * np.sum(x)))
        result += ridge_term
        
        # Add asymmetric coupling with cubic terms
        asym_coupling = 0.0
        for i in range(self.dim):
            asym_coupling += 0.2 * x[i]**3 * np.sin(5 * x[(i+1) % self.dim]) * (1 + 0.1 * np.cos(x[i]))
        result += asym_coupling
        
        # Add global modulation with multi-harmonic components
        r = np.sqrt(np.sum(x**2))
        global_mod = 1.0 + 0.15 * np.sin(4 * r) * np.cos(3 * r) * np.exp(-0.2 * r)
        result *= global_mod
        
        # Add conditioning term with fractional exponents
        conditioning_term = 0.08 * np.sum(np.abs(x)**1.7)
        result += conditioning_term
        
        return result