import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Composite sinusoidal waves with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1)
        sinusoidal = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Fractal-like self-similar structure using recursive sine components
        fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for scalability
                fractal += np.sin(3 * (x_norm[i] - x_norm[j])) * np.cos(2 * (x_norm[i] + x_norm[j])) * np.exp(-0.05 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Adaptive conditioning based on input magnitude
        adaptive = np.sum((1 + 0.5 * np.sin(10 * x_norm)) * x_norm**4)
        
        # Multi-scale multimodal structure with exponential modulation
        multi_scale = 0.0
        for k in range(1, 6):  # 5 scales
            scale = 2**k
            multi_scale += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm) * np.exp(-0.02 * np.abs(x_norm)))
        
        # Cross-dimensional interaction with chaotic perturbation
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(5 * (x_norm[i] - x_norm[j])) * np.cos(3 * (x_norm[i] + x_norm[j])) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(7 * x_norm[i] * x_norm[j])
        
        # Global optimum perturbation with chaotic modulation
        chaos = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * np.exp(-0.3 * np.abs(x_norm)) * np.sin(25 * x_norm))
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.2 * sinusoidal + 0.8 * fractal + 1.0 * adaptive + 0.9 * multi_scale + 0.7 * cross_interaction + 1.5 * chaos