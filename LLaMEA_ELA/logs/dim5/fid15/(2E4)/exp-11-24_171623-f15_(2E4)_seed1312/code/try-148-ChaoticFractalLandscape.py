import numpy as np

class ChaoticFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = 3.9 + 0.1 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map chaos component with dynamic coupling
        chaos_sum = 0.0
        for i in range(self.dim):
            # Initialize chaotic sequence
            x_chaos = 0.5
            for _ in range(15):  # Discard initial transient
                x_chaos = self.chaos_params[i] * x_chaos * (1 - x_chaos)
            # Add coupling between dimensions
            coupling = np.sum([np.sin(x_norm[j] * x_chaos) for j in range(self.dim) if j != i])
            chaos_sum += x_chaos * np.sin(x_norm[i] * np.pi + coupling)
        
        # Fractal noise component using midpoint displacement with periodicity
        fractal_sum = 0.0
        for i in range(self.dim):
            # Generate fractal-like pattern with varying roughness and periodicity
            roughness = 0.3 + 0.4 * np.sin(i * np.pi / max(1, self.dim - 1))
            period = 2.0 + 3.0 * np.cos(i * np.pi / max(1, self.dim - 1))
            noise_val = np.random.normal(0, 1) * (1 + roughness * x_norm[i]**2)
            fractal_sum += noise_val * np.cos(x_norm[i] * period)
        
        # Multi-scale harmonic component with variable phase shifts
        harmonic_sum = 0.0
        for i in range(self.dim):
            scale = 1.0 + 1.5 * np.sin(i * np.pi / max(1, self.dim - 1))
            freq = 2.0**(i % 4)  # Limited frequency range for better conditioning
            amp = 1.0 + 0.8 * np.cos(i * np.pi / max(1, self.dim - 1))
            phase_shift = 0.5 * np.sin(i * np.pi / max(1, self.dim - 1))
            harmonic_sum += amp * np.sin(freq * x_norm[i] * scale + phase_shift)
        
        # Cross-dimension coupling with hyperbolic interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic coupling mechanism
                hyperbolic_interaction = 1.0 / (1.0 + np.exp(-10 * (x_norm[i] - x_norm[j])**2))
                cross_sum += hyperbolic_interaction * (x_norm[i]**2 + x_norm[j]**2)
        
        # Combine all components with dynamic weighting
        result = 0.3 * chaos_sum + 0.25 * fractal_sum + 0.25 * harmonic_sum + 0.2 * cross_sum
        
        # Add dimensionality-dependent conditioning
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Apply global transformation to increase non-convexity and create sharp valleys
        result = np.tanh(result) * (1 + 0.2 * np.sum(np.abs(x_norm)**4))
        
        return result * condition_factor