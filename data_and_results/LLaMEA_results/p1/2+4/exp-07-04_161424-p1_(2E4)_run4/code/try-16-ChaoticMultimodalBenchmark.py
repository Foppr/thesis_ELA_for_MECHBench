import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sine waves with logistic map dynamics
        logistic_map = 4.0 * np.abs(x_norm) * (1 - np.abs(x_norm))
        chaotic_sine = np.sum(np.sin(20 * np.pi * x_norm * logistic_map)**2)
        
        # Radial basis functions with varying widths
        rbf = np.sum(np.exp(-5 * (x_norm**2)) * np.cos(5 * np.pi * x_norm))
        
        # Asymmetric noise component
        noise = np.sum(np.abs(x_norm)**3 * np.sin(7 * np.pi * x_norm) * np.random.uniform(0.8, 1.2, self.dim))
        
        # Polynomial interaction terms with exponential scaling
        polynomial = np.sum(np.exp(np.abs(x_norm)) * (x_norm**3 + 0.3 * x_norm**2 + 0.05 * x_norm))
        
        # Cross-dimensional interaction with chaotic decay
        cross_term = np.exp(-np.sum(np.abs(x_norm)**1.5)) * np.prod(np.sin(3 * np.pi * x_norm))
        
        # Global minimum perturbation with chaotic modulation
        perturbation = 0.02 * np.sum(np.sin(25 * x_norm)**3 * np.cos(5 * x_norm))
        
        # Combine all terms with varying weights
        return 1.5 * quadratic + 0.8 * chaotic_sine + 0.3 * rbf + 0.1 * noise + 0.25 * polynomial + 0.08 * cross_term + perturbation