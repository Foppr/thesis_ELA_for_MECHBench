import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees and adaptive coefficients
        poly_term = np.sum(0.5 * x**6 + 0.3 * x**4 + 0.7 * x**2 + 0.1 * x)
        
        # Trigonometric components with frequency modulation based on dimension
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            trig_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Radial basis function with dynamic center placement and adaptive width
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, min(20, self.dim * 2))
        for i, center in enumerate(centers):
            if i < self.dim:
                width = 1.0 + 0.3 * np.sin(i * 0.8)
                rbf_term += np.exp(-0.5 * (x[i] - center)**2 / width**2)
        
        # Cross-dimensional interaction terms with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Chaotic component using logistic map with dimension-dependent parameter
        chaotic_term = 0.0
        r = 3.8 + 0.1 * np.cos(self.dim * 0.3)
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Gaussian noise modulation with amplitude scaling
        noise_term = np.sum(0.2 * np.exp(-0.5 * (x**2)) * np.sin(3.0 * x))
        
        # Asymmetric distortion to create non-symmetric landscape features
        asym_term = np.sum(0.4 * (x**3 + 0.5 * x**2 - 0.3 * x) * np.cos(x))
        
        # Global scaling and offset to balance term contributions
        return 0.15 * poly_term + 0.20 * trig_term + 0.18 * rbf_term + 0.12 * cross_term + 0.15 * chaotic_term + 0.10 * noise_term + 0.08 * asym_term + 1.5