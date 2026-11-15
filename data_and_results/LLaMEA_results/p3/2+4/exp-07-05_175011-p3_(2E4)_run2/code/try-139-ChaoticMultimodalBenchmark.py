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
        
        # New component: Fractional Brownian motion inspired chaotic structure
        fbm = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fbm += np.abs(x_norm[i] - x_norm[j])**(0.3) * np.sin(10 * (x_norm[i] + x_norm[j]))
        
        # New component: Hyperbolic tangent based multimodal structure
        tanh_multimodal = np.sum(np.tanh(5 * x_norm)**4 + np.sinh(3 * x_norm)**2)
        
        # New component: Gaussian mixture model inspired landscape
        gaussian_mixture = 0.0
        for i in range(self.dim):
            gaussian_mixture += np.exp(-0.5 * (x_norm[i] - 0.5)**2) + np.exp(-0.5 * (x_norm[i] + 0.5)**2)
        
        # Combine all components with different weights
        return 0.4 * quadratic + 2.0 * periodic + 1.5 * exp_interaction + 1.0 * nested + 0.8 * cross_term + 1.8 * high_freq + 0.6 * chaotic + 1.2 * fbm + 0.9 * tanh_multimodal + 0.7 * gaussian_mixture