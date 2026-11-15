import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # High-order polynomial terms with varying exponents
        polynomial = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**6) + 0.3 * np.sum(np.abs(x_norm)**3)
        
        # Complex sinusoidal interactions with multiple frequencies and phase shifts
        sinusoidal = np.sum(np.sin(6 * np.pi * x_norm)**2) + 0.7 * np.sum(np.sin(10 * np.pi * x_norm)**2) + 0.4 * np.sum(np.cos(5 * np.pi * x_norm)**2)
        
        # Cross-terms with higher-order interactions and non-linear coupling
        cross_terms = 0.5 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm)) + \
                      0.3 * np.sum(np.sin(3 * np.pi * x_norm) * np.sin(9 * np.pi * x_norm)) + \
                      0.2 * np.sum(np.cos(6 * np.pi * x_norm) * np.sin(8 * np.pi * x_norm))
        
        # Adaptive scaling based on dimensionality to increase complexity
        adaptive_scale = 1.0 + 0.15 * self.dim
        
        # Add a complex noise term with spatial correlation
        noise = 0.1 * np.random.random() * adaptive_scale
        
        # Combine all terms to create a highly multimodal and challenging landscape
        return adaptive_scale * (polynomial + sinusoidal + cross_terms) + noise