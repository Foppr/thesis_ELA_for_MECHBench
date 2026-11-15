import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Periodic sinusoidal components with increasing frequency
        freqs = np.arange(1, self.dim + 1)
        periodic = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Exponential decay interaction terms with modified decay rate
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.15 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(5 * (x_norm[i] - x_norm[j]))
        
        # Nested multimodal structure with logarithmic scaling
        nested = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(10 * x_norm)**2)
        
        # Cross-term with trigonometric interaction
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Global optimum at origin with high-frequency oscillation
        high_freq = np.sum(np.sin(18 * x_norm)**2 + np.cos(18 * x_norm)**2)
        
        # Additional chaotic component with shifted optimum
        shift = 0.1
        chaotic = np.sum(np.sin(20 * (x_norm + shift)) * np.cos(20 * (x_norm + shift)))
        
        # New enhanced chaotic component with stronger nonlinearity
        enhanced_chaotic = np.sum(np.sin(30 * x_norm**3) * np.cos(30 * x_norm**3))
        
        # New multimodal component with saddle point structure
        saddle = np.sum(np.sin(7 * x_norm) * np.cos(7 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # New interaction term with cubic coupling
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.sin(3 * (x_norm[i] - x_norm[j]))
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.8 * periodic + 1.5 * exp_interaction + 0.9 * nested + 0.7 * cross_term + 1.8 * high_freq + 0.5 * chaotic + 1.2 * enhanced_chaotic + 0.8 * saddle + 1.1 * cubic_interaction