import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Center the search space at origin for easier computation
        x_centered = x - 2.5
        
        # Normalize to [-1, 1] range
        x_norm = x_centered / 5.0
        
        # Polynomial chaos expansion term with mixed monomials
        poly_term = np.sum((x_norm**2 + 0.5 * x_norm**4 + 0.1 * x_norm**6))
        
        # Radial basis function component with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, 5)
        for c in centers:
            rbfs.append(np.exp(-5 * np.sum((x_norm - c)**2)))
        rbf_term = np.sum(rbfs)
        
        # Sine-wave interaction term with varying frequencies
        sine_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Cross-dimensional coupling with interaction strength
        cross_coupling = 0.2 * np.sum(x_norm[:-1] * x_norm[1:] * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Add a chaotic component using logistic map-like behavior
        chaotic = np.sum(np.sin(10 * np.pi * x_norm) * np.tanh(x_norm))
        
        # Combine all terms with appropriate weights
        return 0.5 * poly_term + 0.3 * rbf_term + 0.2 * sine_term + cross_coupling + 0.1 * chaotic