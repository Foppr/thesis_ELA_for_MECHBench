import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate a structured rotation matrix with orthonormal basis
        self.rotation = np.random.rand(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
        # Add a structured shift to induce asymmetry
        self.shift = np.linspace(-1.0, 1.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Initialize function value
        result = 0.0
        
        # Multi-scale sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            # Base quadratic term
            result += 0.5 * (x_rot[i] ** 2)
            
            # Multi-scale sinusoidal interactions
            freq = 2 ** (i % 4)  # Varying frequencies
            amp = 1.0 + i * 0.1   # Increasing amplitude
            result += amp * np.sin(freq * x_rot[i]) * np.cos(freq * x_rot[i] / 2)
            
            # Fractal-like self-similarity using fractional powers
            result += 0.3 * (np.abs(x_rot[i]) ** (1.5 + i * 0.05)) * np.sin(x_rot[i] ** 2)
            
            # Dynamic penalty based on gradient magnitude
            grad_mag = np.abs(x_rot[i]) ** 0.5
            penalty = 0.1 * grad_mag * np.exp(-grad_mag)
            result += penalty
        
        # Cross-dimensional fractal interactions
        for i in range(1, self.dim):
            # Self-similar interaction with previous dimension
            interaction = np.sin(x_rot[i] * x_rot[i-1] * np.pi / 4) * np.exp(-0.1 * np.abs(x_rot[i] - x_rot[i-1]))
            result += interaction * (1 + i * 0.02)
        
        # Global logarithmic barrier
        log_barrier = np.sum(np.log(1 + np.abs(x_rot) ** 2))
        result += 0.2 * log_barrier
        
        # Add a strong penalty for large values to enforce boundary adherence
        result += 0.02 * np.sum(np.abs(x_rot) ** 3)
        
        return result