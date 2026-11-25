import numpy as np

class ChaoticFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = 3.9 + 0.1 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map chaos component with modified dynamics
        chaos_sum = 0.0
        for i in range(self.dim):
            # Initialize chaotic sequence with different initial conditions
            x_chaos = 0.5 + 0.1 * np.random.rand()
            for _ in range(15):  # Increased transient discard
                x_chaos = self.chaos_params[i] * x_chaos * (1 - x_chaos)
            chaos_sum += x_chaos * np.sin(x_norm[i] * np.pi) * np.cos(x_norm[i] * 0.5)
        
        # Fractal noise component with improved scaling
        fractal_sum = 0.0
        for i in range(self.dim):
            # Generate fractal-like pattern with varying roughness and phase
            roughness = 0.4 + 0.4 * np.sin(i * np.pi / max(1, self.dim - 1))
            phase = 0.5 * np.cos(i * np.pi / max(1, self.dim - 1))
            noise_val = np.random.normal(0, 1) * (1 + roughness * x_norm[i]**3)
            fractal_sum += noise_val * np.cos(x_norm[i] * 7.0 + phase)
        
        # Multi-scale harmonic component with frequency modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            scale = 1.5 + 1.5 * np.sin(i * np.pi / max(1, self.dim - 1))
            freq = 3.0**(i % 4) if i % 4 != 0 else 1.0
            amp = 1.2 + 0.8 * np.cos(i * np.pi / max(1, self.dim - 1))
            harmonic_sum += amp * np.sin(freq * x_norm[i] * scale) * np.exp(-0.1 * i)
        
        # Enhanced cross-dimension coupling with sine-based interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sin_interaction = np.sin(np.abs(x_norm[i] - x_norm[j]) * np.pi)
                cross_sum += sin_interaction * (x_norm[i]**2 + x_norm[j]**2) * 0.5
        
        # Combine all components with updated weighting
        result = 0.3 * chaos_sum + 0.25 * fractal_sum + 0.25 * harmonic_sum + 0.2 * cross_sum
        
        # Improved conditioning factor based on dimensionality and input distribution
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.std(x_norm)
        
        # Apply global transformation to increase non-convexity and add plateau control
        tanh_term = np.tanh(result)
        plateau_control = 1.0 + 0.2 * np.sum(np.abs(x_norm)**3)
        result = tanh_term * plateau_control
        
        return result * condition_factor