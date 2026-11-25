import numpy as np

class ChaoticGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute mixture weights and centers for stability
        self.weights = np.random.rand(5) * 0.8 + 0.2
        self.weights /= np.sum(self.weights)
        self.centers = np.random.uniform(-4.0, 4.0, (5, dim))
        self.covariances = [np.eye(dim) * (0.5 + np.random.rand() * 1.5) for _ in range(5)]
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture component
        gaussian_sum = 0.0
        for i in range(5):
            diff = x - self.centers[i]
            cov_inv = np.linalg.inv(self.covariances[i])
            exp_term = np.exp(-0.5 * np.dot(diff, np.dot(cov_inv, diff)))
            gaussian_sum += self.weights[i] * exp_term
        
        # Chaotic sine modulation with varying frequencies
        chaotic_mod = 0.0
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(i * 0.7)
            chaotic_mod += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Polynomial distortion with fractional exponents
        poly_distort = np.sum((x**3.7 + 0.5 * x**2.3 + 0.2 * x**1.9) / self.dim)
        
        # Cross-dimensional interaction with logarithmic scaling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.log(1.0 + np.abs(x[i] * x[i+1])) * np.sin(x[i] + x[i+1])
        
        # Asymmetric exponential decay with sinusoidal perturbation
        exp_decay = np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(2.0 * x) * np.cos(3.0 * x))
        
        # Add a fractal-like recursive pattern using cosine series
        fractal_pattern = 0.0
        for i in range(self.dim):
            term = 0.0
            for k in range(1, 6):
                term += np.cos(k * np.pi * x[i]) / (k**2)
            fractal_pattern += term
        
        return gaussian_sum + chaotic_mod + poly_distort + cross_term + exp_decay + fractal_pattern