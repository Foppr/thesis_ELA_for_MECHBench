import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base exponential-sinusoidal landscape with enhanced non-convexity
        result = 0.0
        for i in range(self.dim):
            # Enhanced exponential modulation with sinusoidal coupling
            exp_term = np.exp(0.5 * x[i]**2) - 1.0
            sin_coupling = np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            poly_term = 0.8 * x[i]**3 + 0.2 * x[i]**4
            
            # Fractional calculus-inspired smoothing with adaptive coupling
            frac_factor = (1.0 + 0.3 * np.sin(x[i] * 2.5) * np.cos(x[i] * 1.7))
            result += (exp_term + sin_coupling + poly_term) * frac_factor
        
        # Complex cross-dimensional energy interactions with dynamic frequency modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Dynamic frequency modulation with chaotic coupling
                freq_mod = 1.5 + 0.8 * np.sin(x[i] * x[j] * 0.7)
                coupling = (x[i]**2 + x[j]**2) * np.sin(freq_mod * x[i] * x[j])
                cross_term += coupling
        
        # Asymmetric energy wells with dynamic frequency modulation
        asym_term = 0.0
        for i in range(self.dim):
            # Novel asymmetric well structure with adaptive parameters
            asym_well = (x[i] - 1.5)**2 * (x[i] + 1.5)**2
            freq_shift = 2.0 + 1.2 * np.sin(x[i] * 0.8)
            asym_term += asym_well * np.cos(freq_shift * x[i])
        
        # Enhanced chaotic behavior through fractional calculus components
        frac_noise = 0.0
        for i in range(self.dim):
            # Fractional noise with dynamic scaling
            scale = 1.0 + 0.5 * np.sin(i * 0.9) * np.cos(i * 0.4)
            frac_noise += scale * np.sin(5.0 * x[i] * np.exp(-0.1 * x[i]**2))
        
        # Combined landscape with modified weights
        total = 0.35 * result + 0.30 * cross_term + 0.20 * asym_term + 0.15 * frac_noise
        
        # Dynamic global scaling based on dimensionality and chaos level
        chaos_factor = 1.0 + 0.2 * np.sin(self.dim * 0.5) + 0.15 * np.cos(self.dim * 0.3)
        scaling = 1.0 + 0.1 * self.dim + 0.05 * chaos_factor
        
        return total * scaling