import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic conditioning term
        quadratic = np.sum(x_scaled**2)
        
        # Logarithmic barrier terms to create narrow valleys
        barrier = np.sum(np.log(1.0 + 10.0 * x_scaled**2))
        
        # Chaotic sine waves with varying frequencies and amplitudes
        chaotic = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Cross-dimensional coupling with interaction weights
        coupling = 0.5 * np.sum((x_scaled[:-1] + x_scaled[1:])**2 * np.sin(10 * np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Time-varying harmonic components (static in this case but with dynamic structure)
        harmonic = np.sum(np.sin(8 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Add a global scaling factor to balance contributions
        return 0.3 * quadratic + 0.4 * barrier + 0.2 * chaotic + 0.1 * coupling + 0.05 * harmonic