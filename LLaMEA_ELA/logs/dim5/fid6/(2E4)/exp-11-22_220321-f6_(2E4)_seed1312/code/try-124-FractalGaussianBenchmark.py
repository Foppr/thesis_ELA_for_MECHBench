import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.n_components = 5
        self.fractal_dim = 1.3
        self.gaussian_means = np.random.uniform(-3.0, 3.0, (self.n_components, dim))
        self.gaussian_vars = np.random.uniform(0.5, 2.0, (self.n_components, dim))
        self.component_weights = np.random.dirichlet(np.ones(self.n_components))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture component evaluation
        gaussian_term = 0.0
        for i in range(self.n_components):
            exponent = -0.5 * np.sum(((x - self.gaussian_means[i]) ** 2) / self.gaussian_vars[i])
            gaussian_term += self.component_weights[i] * np.exp(exponent)
        
        # Fractal Brownian motion component with varying roughness
        fbm_term = 0.0
        for i in range(self.dim):
            # Generate fractal noise with different frequencies
            freq = 2 ** (i % 4)
            scale = 1.0 / (freq ** self.fractal_dim)
            fbm_term += scale * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Multi-scale quadratic interaction terms
        scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                dist = (x[i] - x[j]) ** 2
                scale_term += dist * np.exp(-0.1 * dist)
        
        # Sine-wave modulation with dynamic frequency
        mod_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.6) + 0.3 * np.cos(i * 0.4)
            mod_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Asymmetric penalty for boundary violations
        penalty = 0.0
        for i in range(self.dim):
            if x[i] <= -4.5 or x[i] >= 4.5:
                penalty += 10.0 * (abs(x[i]) - 4.5) ** 2
        
        # Combine all terms with dynamic scaling
        return 0.3 * gaussian_term + 0.25 * fbm_term + 0.2 * scale_term + 0.15 * mod_term + penalty