import numpy as np

class GaussianTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Define multiple Gaussian components with random positions and variances
        self.n_components = 5
        self.means = 3.0 * np.random.rand(self.n_components, dim) - 1.5
        self.vars = 0.5 + 1.5 * np.random.rand(self.n_components, dim)
        # Trigonometric modulation parameters
        self.freq_mod = 2.0 + 3.0 * np.random.rand(dim)
        self.phase_shift = np.pi * np.random.rand(dim)
        # Conditioning and scaling factors
        self.conditioning = 1.0 + 2.0 * np.random.rand(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture term
        gaussian_term = 0.0
        for i in range(self.n_components):
            diff = x - self.means[i]
            exponent = -0.5 * np.sum((diff**2) / self.vars[i])
            weight = 1.0 / (np.sqrt(2.0 * np.pi * np.prod(self.vars[i])))
            gaussian_term += weight * np.exp(exponent)
        
        # Trigonometric modulation term
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += self.conditioning[i] * np.sin(self.freq_mod[i] * x[i] + self.phase_shift[i])**2
        
        # Cross-dimensional interaction term
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.cos(x[i] - x[j]) * (i + j) * 0.1
        
        # Add a global scaling and offset to control function range
        return 2.0 * gaussian_term + 1.5 * trig_term + 0.8 * cross_term + 0.5 * np.sum(x**4)