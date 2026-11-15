import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-wave interactions with dynamic frequencies
        chaotic_terms = np.sum(np.sin(15 * np.sin(7 * x_norm)) * np.cos(11 * np.cos(5 * x_norm)))
        
        # Dynamic polynomial cross-terms with variable exponents
        poly_cross = np.sum((x_norm[0] * x_norm[1])**7) + \
                     0.5 * np.sum(x_norm**7 * np.sin(4 * np.pi * x_norm)) + \
                     0.3 * np.sum(x_norm**3 * np.cos(9 * x_norm))
        
        # Adaptive Gaussian conditioning with dimensionality-dependent variance
        gaussian_conditioning = np.sum(np.exp(-0.2 * x_norm**2) * (1 + 0.5 * np.sin(3 * x_norm)))
        
        # Enhanced trigonometric couplings with multiple frequency harmonics
        trig_coupling = np.sum(np.sin(9 * x_norm) * np.cos(12 * x_norm)) + \
                        0.7 * np.sum(np.sin(14 * x_norm) * np.cos(18 * x_norm)) + \
                        0.4 * np.sum(np.sin(20 * x_norm) * np.cos(25 * x_norm))
        
        # Non-separable high-order interactions with mixed nonlinearities
        high_order = 0.6 * np.sum((x_norm**2 + x_norm**3)**4) + \
                     0.3 * np.sum(np.sin(x_norm) * np.cos(x_norm**2) * x_norm**4)
        
        # Additional chaotic noise with dynamic amplitude
        noise = 0.02 * np.random.random() * np.sum(np.sin(23 * x_norm))
        
        # Combine all terms to create a highly complex multimodal landscape
        return chaotic_terms + poly_cross + gaussian_conditioning + trig_coupling + high_order + noise