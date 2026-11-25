import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like hierarchical structure with recursive cosine modulation
        fractal_term = np.sum(np.cos(2.0 * np.pi * np.sqrt(np.sum(x**2)) * (1.0 + 0.1 * np.sin(x[0] if self.dim > 0 else 0)))) / self.dim
        
        # Quantum-inspired interference pattern with complex amplitude modulation
        quantum_term = np.sum(np.sin(x) * np.cos(2.0 * x) * np.exp(-0.5 * np.sum(x**2) / 10.0)) / self.dim
        
        # Adaptive terrain scaling with dimension-dependent multipliers
        adaptive_scale = 1.0 + 0.3 * np.mean(np.abs(x)) + 0.2 * np.std(x)
        adaptive_term = np.sum((x**3 + 0.5 * x**2) * np.sin(x / adaptive_scale)) / (self.dim * 3.0)
        
        # Multi-scale Gaussian mixture with varying sigmas and centers
        gauss_mixture = 0.0
        centers = np.linspace(-3.0, 3.0, 5)
        sigmas = np.logspace(-1, 0, 5)
        for i, (c, s) in enumerate(zip(centers, sigmas)):
            gauss_mixture += np.exp(-0.5 * np.sum((x - c)**2) / s**2)
        gauss_term = gauss_mixture / (self.dim * 5.0)
        
        # Saddle-point complexity with asymmetric polynomial interactions
        saddle_term = np.sum(x**7 * np.cos(x) - x**3 * np.sin(x)) / (self.dim * 15.0)
        
        # Logarithmic barrier with phase shift for enhanced difficulty
        barrier_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 1.5 + np.pi/4)) / self.dim
        
        # Cross-dimensional interaction with recursive scaling factors
        cross_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                cross_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        cross_term /= self.dim
        
        # Combine all terms with carefully tuned weights
        total = 0.25 * fractal_term + 0.20 * quantum_term + 0.18 * adaptive_term + 0.15 * gauss_term + 0.12 * saddle_term + 0.08 * barrier_term + 0.02 * cross_term
        
        return total