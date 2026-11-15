import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute rotation matrix for added complexity
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        # Adaptive conditioning parameters
        self.conditioning = np.random.uniform(0.1, 10.0, dim)
        # Resonance frequencies for cross-dimensional interactions
        self.resonance_freqs = np.random.uniform(1.0, 5.0, dim)
        # Exponential modulation parameters
        self.exp_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.exp_rates = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and conditioning
        x_transformed = self.rotation_matrix @ x * self.conditioning
        
        # Base quadratic term
        f_val = np.sum(x_transformed**2)
        
        # Add exponential modulated periodic terms
        for i in range(self.dim):
            f_val += self.exp_amplitudes[i] * np.exp(self.exp_rates[i] * np.abs(x_transformed[i])) * \
                     np.sin(self.resonance_freqs[i] * x_transformed[i])
        
        # Cross-dimensional resonance interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                f_val += 0.5 * np.sin(x_transformed[i] * x_transformed[j]) * \
                         np.cos(0.5 * x_transformed[i] + 0.3 * x_transformed[j])
        
        # Add a perturbed quartic term with exponential modulation
        f_val += 0.1 * np.sum((x_transformed**4) * np.exp(0.2 * np.abs(x_transformed)))
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.01
        
        return f_val