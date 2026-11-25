import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for gradient modulation
        self.chaos_params = np.random.uniform(0.5, 2.0, dim)
        self.gradient_freqs = np.random.uniform(2.0, 10.0, dim)
        # Polynomial exponents and exponential scaling factors
        self.poly_exponents = np.random.uniform(1.5, 4.0, dim)
        self.exp_factors = np.random.uniform(0.5, 3.0, dim)
        # Saddle-point positions and influence radii
        self.saddle_points = np.random.uniform(-4.0, 4.0, (10, dim))
        self.saddle_radii = np.random.uniform(0.5, 2.0, 10)
        # Multi-scale harmonic components for interference patterns
        self.harm_freqs = np.logspace(0, 2, 5)  # [1, 10, 100]
        self.harm_ampls = np.random.uniform(0.5, 2.0, 5)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic gradient modulation using sine and cosine products
        for i in range(self.dim):
            grad_mod = np.sin(self.gradient_freqs[i] * x_norm[i]) * \
                       np.cos(self.gradient_freqs[i] * x_norm[i])
            f_val += self.chaos_params[i] * grad_mod
        
        # Polynomial components with dynamic exponents
        for i in range(self.dim):
            f_val += (x_norm[i]**self.poly_exponents[i]) * \
                     np.exp(-x_norm[i]**2 / 2)
        
        # Exponential scaling with variable factors
        for i in range(self.dim):
            f_val += self.exp_factors[i] * np.exp(-np.abs(x_norm[i]))
        
        # Saddle-point interference terms
        for i in range(10):
            dist_sq = np.sum((x_norm - self.saddle_points[i])**2)
            influence = np.exp(-dist_sq / (2 * self.saddle_radii[i]**2))
            f_val += influence * np.sin(dist_sq)
        
        # Multi-scale harmonic interference
        for freq, ampl in zip(self.harm_freqs, self.harm_ampls):
            harm_sum = 0.0
            for j in range(self.dim):
                harm_sum += np.sin(freq * x_norm[j])
            f_val += ampl * np.sin(harm_sum)
        
        # Add chaotic perturbations to increase complexity
        chaos_perturb = 0.3 * np.sum(np.sin(17 * x_norm) * np.cos(13 * x_norm))
        f_val += chaos_perturb
        
        # Global scaling with harmonic modulation
        global_scale = 1.0 + 0.5 * np.sin(np.sum(x_norm**2))
        f_val *= global_scale
        
        return f_val