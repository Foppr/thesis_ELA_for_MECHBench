import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Self-adaptive polynomial potentials with dimension-dependent exponents
        poly_potential = 0.0
        for i in range(self.dim):
            # Exponent adapts based on dimension and position
            exp_val = 2 + 0.5 * np.sin(i * np.pi / self.dim) + 0.3 * x_norm[i]**2
            poly_potential += np.abs(x_norm[i])**exp_val
        
        # Fractal-like gradient field with recursive scaling
        fractal_gradient = 0.0
        scale = 1.0
        for i in range(self.dim):
            # Recursive fractal component with diminishing scale
            fractal_val = np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i])
            fractal_gradient += fractal_val
            scale *= 0.7  # Decreasing scale for recursive effect
        
        # Quantum-inspired interference patterns
        quantum_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Pairwise interference terms with phase modulation
                phase = np.pi * (x_norm[i] + x_norm[j]) / 2.0
                interference = np.sin(phase) * np.cos(phase)
                quantum_interference += interference
        
        # Dimension-dependent conditioning with logarithmic scaling
        condition_number = 1.0 + 0.5 * np.log(self.dim + 1) + 0.2 * np.sin(self.dim * np.pi / 3.0)
        
        # Add noise component for additional complexity
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x_norm)
        
        # Combine all components with adaptive weights
        total = condition_number * (poly_potential + 0.5 * fractal_gradient + 0.3 * quantum_interference + noise)
        
        return total