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
        
        # Exponential decay interaction terms with enhanced coupling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.05 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(7 * (x_norm[i] - x_norm[j])) * np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Nested multimodal structure with logarithmic scaling and additional chaos
        nested = np.sum(np.log(1 + np.abs(x_norm)) * np.sin(12 * x_norm)**2 + np.cos(8 * x_norm)**2)
        
        # Cross-term with trigonometric interaction and phase shift
        cross_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:] + 0.5) * np.cos(x_norm[:-1] - x_norm[1:] - 0.3))
        
        # Global optimum at origin with high-frequency oscillation and chaotic perturbation
        high_freq = np.sum(np.sin(20 * x_norm)**2 + np.cos(20 * x_norm)**2 + 0.3 * np.sin(50 * x_norm))
        
        # Additional chaotic component with non-uniform scaling
        chaotic = np.sum(np.sin(25 * x_norm) * np.cos(15 * x_norm) * np.exp(-0.2 * np.abs(x_norm)))
        
        # Augmented chaotic dynamics with fractional Brownian motion inspired terms
        fractional = 0.0
        for i in range(self.dim):
            fractional += np.sin(30 * x_norm[i]) * np.cos(10 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2) * np.sin(15 * x_norm[i]**3)
        
        # Reshaped interaction with higher-order polynomial coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.sin(5 * (x_norm[i] - x_norm[j])) * np.cos(2 * (x_norm[i] + x_norm[j]))
        
        # Combined with a new global optimum shift and increased conditioning
        return 0.6 * quadratic + 2.5 * periodic + 1.8 * exp_interaction + 1.2 * nested + 0.9 * cross_term + 2.0 * high_freq + 0.7 * chaotic + 1.1 * fractional + 0.5 * poly_interaction