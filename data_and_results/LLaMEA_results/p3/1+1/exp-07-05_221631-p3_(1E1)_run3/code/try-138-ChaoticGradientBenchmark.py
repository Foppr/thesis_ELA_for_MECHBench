import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute random vectors for gradient direction control
        self.gradient_vectors = np.random.randn(dim, dim)
        self.gradient_vectors, _ = np.linalg.qr(self.gradient_vectors)
        # Conditioning parameters
        self.conditioning = np.logspace(0, 3, dim)
        # Chaotic modulation parameters
        self.chaos_factor = 0.5
        self.oscillation_freq = 2.0 * np.pi * np.random.rand(dim)
        # Saddle point distribution
        self.saddle_positions = np.random.uniform(-3.0, 3.0, (5, dim))
        self.saddle_strength = 0.8
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        # Apply conditioning
        x_conditioned = x * self.conditioning
        
        # Base quadratic term
        f_val = np.sum(x_conditioned**2)
        
        # Add chaotic harmonic oscillations with exponential decay
        for i in range(self.dim):
            # Exponentially decaying harmonic components
            harmonic = 0.0
            for n in range(1, 6):
                harmonic += (1.0 / (n * n)) * np.sin(n * self.oscillation_freq[i] * x_conditioned[i])
            f_val += self.chaos_factor * harmonic
            
        # Add saddle point attractors
        for saddle in self.saddle_positions:
            dist = np.sum((x - saddle)**2)
            f_val += self.saddle_strength * np.exp(-dist / 2.0)
            
        # Add cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.sin(x_conditioned[i]) * np.cos(x_conditioned[j])
                f_val += 0.3 * coupling * (1.0 + 0.2 * np.sin(3.0 * x_conditioned[i]))
                
        # Add a small constant to ensure positive fitness
        f_val += 0.1
        
        return f_val