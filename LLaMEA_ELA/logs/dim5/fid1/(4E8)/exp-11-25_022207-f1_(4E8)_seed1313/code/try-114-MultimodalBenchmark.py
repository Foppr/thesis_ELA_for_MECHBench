import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine-cosine wave interactions with multiple frequencies and harmonics
        chaotic_wave = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                             np.sin(11 * np.pi * x_norm) * np.cos(13 * np.pi * x_norm) * 
                             np.sin(15 * np.pi * x_norm))
        
        # Asymmetric quartic potential with varying skewness, curvature and additional harmonic terms
        asymmetric_quartic = np.sum(x_norm**4 * (1 + 0.7 * np.sin(2 * x_norm) * np.cos(3 * x_norm)) * 
                                  (1 + 0.3 * np.sin(5 * x_norm) * np.cos(7 * x_norm)))
        
        # Non-separable high-order polynomial interactions with stronger coupling and additional cross-terms
        poly_interaction = np.sum((x_norm[:-1]**5 + x_norm[1:]**5) * 
                                np.exp(-0.4 * (x_norm[:-1] - x_norm[1:])**2) * 
                                (1 + 0.2 * np.sin(3 * (x_norm[:-1] + x_norm[1:]))))
        
        # Added noise term with higher variance and non-Gaussian characteristics
        noise = 0.3 * np.random.laplace(0, 1, self.dim).sum()
        
        # Exponential weighting with stronger gradient complexity and additional dimensionality
        exp_weighted = np.sum(np.exp(-0.3 * np.abs(x_norm)) * x_norm**4 * 
                            (1 + 0.2 * np.sin(4 * x_norm)))
        
        # Cross-dimensional coupling with perturbed repulsive force field using higher-order harmonics
        cross_coupling = 0.8 * np.sum((x_norm[:-1] - x_norm[1:])**5 * 
                                    np.cos(0.8 * (x_norm[:-1] + x_norm[1:])) * 
                                    np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                                    (1 + 0.1 * np.sin(2 * (x_norm[:-1] - x_norm[1:]))))
        
        # Additional perturbation term for increased multimodality with chaotic frequency modulation
        perturbation = 0.4 * np.sum(np.sin(17 * np.pi * x_norm) * np.cos(19 * np.pi * x_norm) * 
                                  np.sin(23 * np.pi * x_norm))
        
        # Additional high-frequency oscillatory component for enhanced gradient complexity
        high_freq = 0.25 * np.sum(np.sin(25 * np.pi * x_norm) * np.cos(27 * np.pi * x_norm) * 
                                np.sin(29 * np.pi * x_norm))
        
        return chaotic_wave + asymmetric_quartic + poly_interaction + noise + exp_weighted + cross_coupling + perturbation + high_freq