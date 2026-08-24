import numpy as np

class FractalSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute fractal-like interaction coefficients
        self.fractal_coeffs = np.random.randn(dim, dim) * 0.5
        self.fractal_coeffs = np.abs(self.fractal_coeffs) + 0.1
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Apply fractal-like sine-wave interactions with polynomial chaos components
        result = 0.0
        for i in range(self.dim):
            # Base polynomial chaos component with sine modulation
            poly_term = x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i]
            sine_mod = np.sin(3.0 * x[i]) + 0.5 * np.cos(2.0 * x[i])
            result += poly_term * sine_mod
            
            # Add fractal-like coupling with other dimensions
            for j in range(self.dim):
                if i != j:
                    coupling = self.fractal_coeffs[i, j] * np.sin(2.0 * x[i] * x[j])
                    result += coupling
                    
        # Add multi-scale fractal sine-wave components with chaotic modulation
        for i in range(self.dim):
            # Fractal-like frequency modulation with chaotic component
            freq = 1.0 + 0.5 * np.sin(0.3 * i) + 0.2 * np.cos(0.4 * i) + 0.1 * np.sin(0.7 * i**1.5)
            amp = 1.0 + 0.3 * np.sin(0.5 * i) + 0.1 * np.cos(0.6 * i) + 0.05 * np.sin(0.9 * i**1.2)
            phase = 0.2 * np.sin(0.4 * i) + 0.1 * np.cos(0.3 * i) + 0.05 * np.sin(0.6 * i**0.8)
            result += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase)
            
        # Adaptive conditioning based on dimensionality with chaotic scaling
        condition_factor = 1.0 + 0.2 * np.sin(0.1 * self.dim) + 0.1 * np.cos(0.05 * self.dim) + 0.05 * np.sin(0.15 * self.dim**1.3)
        result *= condition_factor
        
        # Add boundary penalty with fractal scaling and chaotic component
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x[i])
            if dist_from_bound < 0:
                fractal_scale = 1.0 + 0.1 * np.sin(0.2 * i) + 0.05 * np.cos(0.1 * i) + 0.02 * np.sin(0.3 * i**1.1)
                boundary_penalty += 5.0 * np.exp(-dist_from_bound**2 * fractal_scale)
        result += boundary_penalty
        
        # Add a chaotic noise component with fractal structure and exponential decay
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(5.0 * x[i] + 0.3 * i) * np.cos(3.0 * x[i]**2 + 0.2 * i) * np.exp(-0.1 * i)
        result += noise
        
        # Add a global scaling factor with fractal modulation and chaotic component
        global_scale = 1.0 + 0.1 * np.sin(0.05 * self.dim) + 0.05 * np.cos(0.02 * self.dim) + 0.03 * np.sin(0.08 * self.dim**1.4)
        result *= global_scale
        
        # Add exponential decay harmonic perturbations for increased multimodality
        decay_perturbation = 0.0
        for i in range(self.dim):
            decay_perturbation += 0.2 * np.exp(-0.5 * i) * np.sin(4.0 * x[i] + 0.1 * i**1.5)
        result += decay_perturbation
        
        return result