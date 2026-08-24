import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base with adaptive scaling
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic += np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[j]) * np.sin(7 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Radial polynomial distortion with high-degree terms
        radial = np.sum((x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2) ** 2)
        
        # Cross-terms with exponential decay interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(2 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[j])
        
        # Add a complex noise pattern based on the input structure
        noise = 0.1 * np.sum(np.sin(13 * x_norm) * np.cos(11 * x_norm))
        
        # Combine all terms with varying weights to create a highly complex landscape
        return 2.0 * quadratic + 1.5 * chaotic + 0.8 * radial + 0.6 * cross_terms + noise