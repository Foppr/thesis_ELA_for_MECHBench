import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay RBF centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.3, 3.0, 15)
        # Trigonometric coupling parameters
        self.coupling_freqs = np.random.uniform(2.0, 15.0, dim)
        self.coupling_ampls = np.random.uniform(0.5, 3.0, dim)
        # Adaptive conditioning exponents
        self.conditioning_exponents = np.random.uniform(1.5, 6.0, dim)
        self.conditioning_factors = np.random.uniform(0.2, 1.8, dim)
        # Multi-scale sine wave components
        self.sin_freqs = np.random.uniform(0.5, 12.0, dim)
        self.sin_ampls = np.random.uniform(0.3, 4.0, dim)
        # Exponential decay parameters
        self.exp_decay_rates = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Exponential decay RBF components
        for i in range(15):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.exp(-self.rbf_widths[i] * np.sqrt(rbf_sum)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum)
        
        # Trigonometric coupling terms
        for i in range(self.dim):
            coupling_term = 0.0
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_term += np.sin(self.coupling_freqs[i] * dist) * \
                                np.cos(self.coupling_freqs[j] * dist) * \
                                np.exp(-dist**2 / (2 * 0.5**2))
            f_val += self.coupling_ampls[i] * coupling_term
        
        # Adaptive conditioning
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.2 * np.sin(5 * x_norm[i]))
        
        # Multi-scale sine wave components
        for i in range(self.dim):
            f_val += self.sin_ampls[i] * np.sin(self.sin_freqs[i] * x_norm[i]) * \
                     np.cos(self.sin_freqs[i] * x_norm[i]) * \
                     np.exp(-self.exp_decay_rates[i] * np.abs(x_norm[i]))
        
        # Cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction = np.exp(-np.abs(x_norm[i] - x_norm[j]) / (0.5 + 0.3 * np.sin(i * 0.7)))
                f_val += 0.2 * exp_interaction * np.sin(3 * (x_norm[i] + x_norm[j]))
        
        # Global scaling and noise
        f_val *= (1.0 + 0.3 * np.sum(np.sin(x_norm)**2))
        noise = 0.1 * np.sum(np.cos(13 * x_norm) * np.sin(7 * x_norm))
        f_val += noise
        
        return f_val