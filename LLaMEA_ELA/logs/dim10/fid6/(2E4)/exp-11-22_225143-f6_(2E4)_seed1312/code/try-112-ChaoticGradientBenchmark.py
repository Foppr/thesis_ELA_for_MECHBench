import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for gradient modulation
        self.chaos_params = np.random.uniform(0.1, 2.0, dim)
        self.gradient_freqs = np.random.uniform(2.0, 8.0, dim)
        # Elliptic and hyperbolic component parameters
        self.elliptic_radii = np.random.uniform(1.0, 4.0, dim)
        self.hyperbolic_params = np.random.uniform(0.5, 3.0, dim)
        # Saddle point distribution
        self.saddle_centers = np.random.uniform(-3.0, 3.0, (10, dim))
        self.saddle_strengths = np.random.uniform(0.5, 2.5, 10)
        # Noise and perturbation parameters
        self.noise_level = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic gradient modulation component
        for i in range(self.dim):
            f_val += self.chaos_params[i] * np.sin(self.gradient_freqs[i] * x_norm[i]) * \
                     np.cos(self.gradient_freqs[i] * x_norm[i]) * \
                     (1.0 + 0.2 * np.sin(13 * x_norm[i]))
        
        # Elliptic basin components
        for i in range(self.dim):
            f_val += 0.5 * (x_norm[i]**2) / (self.elliptic_radii[i]**2) * \
                     (1.0 + 0.3 * np.cos(5 * x_norm[i]))
        
        # Hyperbolic saddle point components
        for i in range(self.dim):
            f_val += self.hyperbolic_params[i] * np.tanh(x_norm[i]) * \
                     (1.0 + 0.1 * np.sin(7 * x_norm[i]))
        
        # Saddle point interactions
        for i in range(10):
            dist = 0.0
            for j in range(self.dim):
                dist += (x_norm[j] - self.saddle_centers[i, j])**2
            f_val += self.saddle_strengths[i] * np.exp(-dist / (2 * 0.5**2)) * \
                     np.sin(3 * dist) * np.cos(2 * dist)
        
        # Cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.exp(-((x_norm[i] - x_norm[j])**2 + 0.01) / (2 * 0.3**2))
                f_val += 0.2 * coupling * np.sin(5 * (x_norm[i] + x_norm[j])) * \
                         np.cos(4 * (x_norm[i] - x_norm[j]))
        
        # Noise perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_level[i] * np.sin(23 * x_norm[i]) * np.cos(19 * x_norm[i])
        f_val += 0.1 * noise
        
        # Global conditioning and non-separability
        f_val *= (1.0 + 0.4 * np.sum(np.abs(x_norm)**3))
        
        return f_val