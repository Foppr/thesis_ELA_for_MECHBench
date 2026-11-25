import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.1, 1.0, dim)
        self.frequency_params = np.random.uniform(2.0, 8.0, dim)
        self.curvature_params = np.random.uniform(0.5, 3.0, dim)
        # Saddle point configuration
        self.saddle_centers = np.random.uniform(-3.0, 3.0, (5, dim))
        self.saddle_strengths = np.random.uniform(0.5, 2.0, 5)
        # Multi-scale harmonic components
        self.harmonic_freqs = np.random.uniform(1.0, 6.0, dim)
        self.harmonic_amps = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic gradient terms with exponential modulation
        for i in range(self.dim):
            chaos_term = self.chaos_params[i] * np.exp(-x_norm[i]**2) * \
                         np.sin(self.frequency_params[i] * x_norm[i]) * \
                         np.cos(self.frequency_params[i] * x_norm[i])
            f_val += chaos_term
        
        # Dynamic curvature components with varying exponents
        for i in range(self.dim):
            curv_term = self.curvature_params[i] * (x_norm[i]**2) * \
                        np.exp(-0.5 * x_norm[i]**2) * \
                        np.sin(3 * x_norm[i])
            f_val += curv_term
        
        # Saddle point attractions and repulsions
        for i in range(5):
            dist = np.sum((x_norm - self.saddle_centers[i])**2)
            saddle_term = self.saddle_strengths[i] * np.exp(-dist / 2.0) * \
                          np.sin(dist) * np.cos(dist)
            f_val += saddle_term
        
        # Multi-scale harmonic interference
        for i in range(self.dim):
            harmonic_sum = 0.0
            for j in range(1, 6):  # Up to 5 harmonics
                harmonic_sum += self.harmonic_amps[i] * np.sin(j * self.harmonic_freqs[i] * x_norm[i])
            f_val += harmonic_sum**2
        
        # Add global noise with fractal-like structure
        noise = 0.0
        for i in range(1, 8):
            noise += np.sin(i * np.pi * x_norm[0]) * np.cos(i * np.pi * x_norm[-1])
        f_val += 0.2 * noise
        
        # Normalize and return final value
        return f_val / (1.0 + 0.1 * np.abs(np.sum(x_norm**3)))