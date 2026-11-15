import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine interactions with dynamic frequencies
        chaotic_terms = np.sum(np.sin(13 * x_norm) * np.cos(17 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Dynamic polynomial cross-terms with varying exponents
        poly_cross = np.sum((x_norm[0] * x_norm[1])**9) + \
                     0.4 * np.sum(x_norm**8 * np.sin(5 * np.pi * x_norm)) + \
                     0.2 * np.sum(x_norm**5 * np.cos(8 * np.pi * x_norm))
        
        # Adaptive Gaussian conditioning with dimensionality-dependent variance
        gaussian_conditioning = np.sum(np.exp(-0.1 * x_norm**2) * (x_norm**2 + 0.5 * np.abs(x_norm)))
        
        # Multi-scale trigonometric couplings with varying amplitudes
        multi_trig = 1.5 * np.sum(np.sin(10 * x_norm) * np.cos(12 * x_norm)) + \
                     0.7 * np.sum(np.sin(15 * x_norm) * np.cos(18 * x_norm)) + \
                     0.3 * np.sum(np.sin(20 * x_norm) * np.cos(25 * x_norm))
        
        # Mixed nonlinear coupling with exponential and logarithmic interactions
        mixed_nonlinear = 0.3 * np.sum(np.exp(0.5 * x_norm) * np.sin(3 * x_norm)) + \
                          0.2 * np.sum(np.log(1 + np.abs(x_norm)) * np.cos(4 * x_norm))
        
        # Add a complex noise term with chaotic behavior
        noise = 0.05 * np.random.random() * np.sum(np.sin(23 * x_norm) * np.cos(27 * x_norm))
        
        # Combine all terms to create a highly multimodal and complex landscape
        return chaotic_terms + poly_cross + gaussian_conditioning + multi_trig + mixed_nonlinear + noise