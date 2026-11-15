import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine waves with higher frequency modulation
        f2 = np.sum(np.sin(20 * np.pi * x_norm + np.sin(10 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms with modified exponents for complexity
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) * 1.5) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms with higher-order exponents for non-convexity
        f4 = np.sum(x_norm**6 + 0.4 * x_norm**8 + 0.2 * x_norm**10)
        
        # Stronger cross-terms with trigonometric coupling to increase dimensionality interaction
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:]) * (x_norm[:-1] - x_norm[1:])) ** 2)
        
        # Additional chaotic interference patterns with increased amplitude and frequency
        f6 = np.sum(np.sin(7 * np.pi * x_norm * np.sin(5 * np.pi * x_norm)) ** 2)
        
        # New term: highly nonlinear cross-dimensional coupling with trigonometric cubic interactions
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:]) ** 2) ** 4)
        
        # Extra term: fourth-order polynomial with chaotic modulation
        f8 = np.sum((x_norm**4 + 0.5 * x_norm**7 + 0.3 * x_norm**9) * np.sin(4 * np.pi * x_norm))
        
        # Slight modification: increased weight on chaotic interference and adjusted polynomial exponents
        return f1 + 1.0 * f2 + 0.6 * f3 + 0.12 * f4 + 0.4 * f5 + 0.25 * f6 + 0.3 * f7 + 0.15 * f8