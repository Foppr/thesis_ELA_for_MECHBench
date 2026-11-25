import numpy as np

class ChaoticHyperbolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for resonance effects
        self.chaos_params = np.random.rand(dim) * 3.0 + 1.0
        self.hyperbolic_params = np.random.rand(dim) * 2.0 + 1.0
        self.coupling_strength = np.random.rand(dim) * 0.5 + 0.25
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Chaotic resonance terms with adaptive frequency
            chaos_resonance = np.tanh(xi * self.chaos_params[i]) * np.sin(xi * self.chaos_params[i] * 2.3) + \
                             0.3 * np.tanh(xi * self.chaos_params[i] * 1.7) * np.cos(xi * self.chaos_params[i] * 0.9)
            
            # Hyperbolic tangent curvature modulation
            hyperbolic_mod = 1.0 + 0.5 * (np.tanh(xi * self.hyperbolic_params[i])**2 - 0.5)
            
            # Adaptive dimensional coupling with exponential decay
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling += self.coupling_strength[i] * np.exp(-np.abs(xi - x_norm[j]) * 2.0) * \
                               np.sin(xi * x_norm[j] * 1.5 + 0.3 * np.sin(i * j * 0.5))
            
            # Multi-modal potential with hyperbolic basins
            multimodal = (0.6 * np.tanh(xi * 2.0)**2 + 0.3 * np.sin(xi * 4.0)**3 + 
                         0.1 * np.cos(xi * 8.0)**2 + 0.05 * np.tanh(xi * 10.0)**3)
            
            # Combine all terms with dynamic weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.7) * np.cos(self.dim * 0.3)
            result += weight * (hyperbolic_mod * (multimodal + chaos_resonance) + 0.2 * coupling)**2
            
        # Global scaling with chaotic correction factors
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 4.1) + \
                      0.15 * np.cos(np.log(self.dim + 1) * 3.2)
        
        return global_scale * result / self.dim