import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine wave component with varying frequencies
        chaotic_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) + 
                             0.2 * np.sin(11 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Asymmetric quartic potential with adaptive scaling
        quartic_term = np.sum(0.8 * x_norm**4 + 0.3 * x_norm**3 - 0.5 * x_norm**2 + 
                             0.1 * x_norm * np.sin(2 * x_norm) * np.cos(x_norm))
        
        # Non-separable high-order polynomial interactions with cross-dimensional coupling
        poly_term = 0.5 * np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Enhanced saddle point structure with variable curvature and noise modulation
        saddle_term = np.sum(x_norm**6 * np.exp(-0.5 * x_norm**2) + 0.4 * x_norm**3 * np.sin(3 * x_norm))
        
        # Cross-dimensional interaction with dynamic weights based on position and frequency modulation
        cross_term = 0.2 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**(2.1 + 0.4 * np.sin(x_norm[:-1] * np.pi)))
        
        # Add gradient regularization to avoid flat regions and improve conditioning
        grad_reg = 0.05 * np.sum(np.gradient(x_norm)**2)
        
        # Add noise with adaptive amplitude based on dimensionality
        noise_amp = 0.03 * (1 + self.dim / 10.0)
        noise_term = noise_amp * np.random.randn(*x_norm.shape)
        
        return chaotic_term + quartic_term + poly_term + saddle_term + cross_term + grad_reg + noise_term