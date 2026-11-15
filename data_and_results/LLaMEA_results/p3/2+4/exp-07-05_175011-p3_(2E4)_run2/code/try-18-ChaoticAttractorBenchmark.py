import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Periodic attractor-like components with varying periods and amplitudes
        periods = np.arange(1, self.dim + 1)
        attractor = np.sum(np.sin(periods * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Asymmetric multimodal structure using sigmoidal transformations
        asymmetric = np.sum(1.0 / (1.0 + np.exp(-x_norm)) * np.sin(2 * np.pi * x_norm)**2)
        
        # Gradient complexity via higher-order polynomial interactions
        grad_complexity = np.sum((x_norm[:-1]**3) * (x_norm[1:]**2) * np.cos(5 * np.pi * x_norm[:-1] + 3 * np.pi * x_norm[1:]))
        
        # Non-separable cross-terms with chaotic scaling
        cross_terms = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(2 * x_norm[:-1] - x_norm[1:]))
        
        # High-frequency chaotic noise component
        noise = np.sum(np.sin(15 * x_norm) * np.cos(7 * x_norm) * np.sin(11 * x_norm))
        
        # Combine all components with carefully tuned weights
        return 0.3 * quadratic + 1.8 * attractor + 1.2 * asymmetric + 0.9 * grad_complexity + 1.1 * cross_terms + 0.7 * noise