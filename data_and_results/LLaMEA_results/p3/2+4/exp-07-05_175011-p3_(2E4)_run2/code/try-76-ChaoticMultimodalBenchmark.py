import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Composite sinusoidal waves with varying amplitudes and frequencies
        waves = 0.0
        for i in range(self.dim):
            waves += np.sin(2 * np.pi * (i + 1) * x_norm[i]) * np.cos(3 * np.pi * (i + 1) * x_norm[i])
        
        # Radial basis function components with varying centers and widths
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            for j in range(self.dim):
                rbf += np.exp(-5 * (x_norm[j] - centers[i])**2) * np.sin(4 * np.pi * (x_norm[j] - centers[i]))
        
        # Asymmetric penalty terms to create non-symmetric landscape
        asym_penalty = 0.0
        for i in range(self.dim):
            if x_norm[i] > 0:
                asym_penalty += 2 * x_norm[i]**3
            else:
                asym_penalty += 0.5 * x_norm[i]**3
        
        # Cross-term interactions with trigonometric coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(2 * (x_norm[i] + x_norm[j])) * np.cos(3 * (x_norm[i] - x_norm[j]))
        
        # Nested multimodal structure with exponential scaling
        nested = 0.0
        for i in range(self.dim):
            nested += np.exp(-0.5 * x_norm[i]**2) * np.sin(10 * x_norm[i])**2 + np.cos(5 * x_norm[i])**2
        
        # Chaotic perturbation using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x_norm[i]) * np.cos(7 * x_norm[i]) * np.exp(-0.1 * np.abs(x_norm[i]))
        
        # Shifted global optimum with additional harmonic components
        shift = 0.0
        for i in range(self.dim):
            shift += 0.2 * (x_norm[i] - 0.2)**2 + 0.1 * np.sin(10 * (x_norm[i] - 0.2))
        
        # Combine all components with different weights
        return 0.5 * quadratic + 1.5 * waves + 1.2 * rbf + 0.8 * asym_penalty + 0.6 * cross_interaction + 1.0 * nested + 0.7 * chaotic + 0.4 * shift