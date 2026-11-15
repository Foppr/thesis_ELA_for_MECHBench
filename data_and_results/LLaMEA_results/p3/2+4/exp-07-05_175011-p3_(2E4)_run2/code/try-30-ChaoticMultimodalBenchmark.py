import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Enhanced periodic sinusoidal components with chaotic behavior
        freqs = np.arange(1, self.dim + 1)
        periodic = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Stronger exponential decay interaction terms with chaotic coupling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                exp_interaction += np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(3 * dist) * np.cos(2 * dist)
        
        # Nested multimodal structure with enhanced logarithmic scaling
        nested = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(15 * x_norm)**2 + np.cos(10 * x_norm)**2)
        
        # Cross-term with enhanced trigonometric interaction and chaotic coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.sin(x_norm[i] + x_norm[i+1]) * np.cos(x_norm[i] - x_norm[i+1]) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Global optimum at origin with enhanced high-frequency oscillation
        high_freq = np.sum(np.sin(20 * x_norm)**2 + np.cos(20 * x_norm)**2 + np.sin(25 * x_norm)**2)
        
        # Additional chaotic attractor-like component
        chaotic = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * np.exp(-0.05 * np.abs(x_norm)))
        
        # Combine all components with optimized weights
        return 0.2 * quadratic + 2.0 * periodic + 1.5 * exp_interaction + 1.0 * nested + 0.8 * cross_term + 1.8 * high_freq + 0.5 * chaotic