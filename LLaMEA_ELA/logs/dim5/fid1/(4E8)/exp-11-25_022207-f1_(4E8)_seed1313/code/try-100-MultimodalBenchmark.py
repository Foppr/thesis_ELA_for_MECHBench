import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-cosine wave interactions with multiple frequencies
        chaotic_wave = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                             np.sin(9 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm))
        
        # Asymmetric quartic potential with varying skewness and curvature
        asymmetric_quartic = np.sum(x_norm**4 * (1 + 0.5 * np.sin(2 * x_norm) * np.cos(3 * x_norm)))
        
        # Non-separable high-order polynomial interactions with stronger coupling
        poly_interaction = np.sum((x_norm[:-1]**4 + x_norm[1:]**4) * 
                                np.exp(-0.3 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Added noise term with higher variance for robustness testing
        noise = 0.2 * np.random.normal(0, 1, self.dim).sum()
        
        # Exponential weighting with stronger gradient complexity
        exp_weighted = np.sum(np.exp(-0.2 * np.abs(x_norm)) * x_norm**3)
        
        # Cross-dimensional coupling with perturbed repulsive force field
        cross_coupling = 0.7 * np.sum((x_norm[:-1] - x_norm[1:])**4 * 
                                    np.cos(0.7 * (x_norm[:-1] + x_norm[1:])) * 
                                    np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Additional perturbation term for increased multimodality
        perturbation = 0.3 * np.sum(np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm))
        
        return chaotic_wave + asymmetric_quartic + poly_interaction + noise + exp_weighted + cross_coupling + perturbation