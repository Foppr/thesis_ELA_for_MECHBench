import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial term with higher-order polynomial growth
        r = np.sqrt(np.sum(x_norm**2))
        
        # Enhanced radial oscillation with multiple frequencies
        radial_osc = np.sin(15 * r) * np.cos(8 * r) * np.sin(3 * r)
        
        # Coupled sine-cosine interactions between dimensions
        coupled_terms = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Complex exponential barrier with multiple peaks
        barrier = np.sum(np.exp(-5 * (1 - np.abs(x_norm))**4) + 0.5 * np.exp(-2 * (1 - np.abs(x_norm))**2))
        
        # Additional high-frequency oscillation in each dimension
        high_freq = np.sum(np.sin(20 * x_norm) ** 4)
        
        # Combine all terms with varying weights
        return r**5 + 0.7 * radial_osc + 0.4 * coupled_terms + 0.2 * barrier + 0.3 * high_freq