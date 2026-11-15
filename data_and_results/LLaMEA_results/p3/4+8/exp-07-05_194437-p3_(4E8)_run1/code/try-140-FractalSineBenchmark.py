import numpy as np

class FractalSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute fractal-like interaction coefficients with chaotic scaling
        self.fractal_coeffs = np.random.randn(dim, dim) * 0.5
        self.fractal_coeffs = np.abs(self.fractal_coeffs) + 0.1
        # Add chaotic modulation to coefficients
        for i in range(dim):
            for j in range(dim):
                self.fractal_coeffs[i, j] *= (1.0 + 0.2 * np.sin(0.5 * i + 0.3 * j))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Apply chaotic fractal sine-wave interactions with polynomial chaos components
        result = 0.0
        for i in range(self.dim):
            # Base polynomial chaos component with chaotic sine modulation
            poly_term = x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i]
            sine_mod = np.sin(3.0 * x[i] + 0.5 * np.sin(2.0 * x[i])) + 0.5 * np.cos(2.0 * x[i] + 0.3 * np.cos(x[i]))
            result += poly_term * sine_mod
            
            # Add chaotic fractal coupling with other dimensions
            for j in range(self.dim):
                if i != j:
                    # Introduce chaotic interaction with exponential decay
                    decay = np.exp(-0.1 * np.abs(i - j))
                    coupling = self.fractal_coeffs[i, j] * np.sin(2.0 * x[i] * x[j]) * decay
                    result += coupling
                    
        # Add multi-scale chaotic fractal sine-wave components
        for i in range(self.dim):
            # Chaotic frequency modulation with fractal scaling
            freq = 1.0 + 0.5 * np.sin(0.3 * i + 0.2 * np.sin(0.1 * i)) + 0.2 * np.cos(0.4 * i + 0.1 * np.cos(0.2 * i))
            amp = 1.0 + 0.3 * np.sin(0.5 * i + 0.1 * np.sin(0.3 * i)) + 0.1 * np.cos(0.6 * i + 0.05 * np.cos(0.4 * i))
            phase = 0.2 * np.sin(0.4 * i + 0.1 * np.sin(0.2 * i)) + 0.1 * np.cos(0.3 * i + 0.05 * np.cos(0.1 * i))
            result += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase)
            
        # Adaptive conditioning based on dimensionality with chaotic component
        condition_factor = 1.0 + 0.2 * np.sin(0.1 * self.dim + 0.1 * np.sin(0.05 * self.dim)) + 0.1 * np.cos(0.05 * self.dim + 0.05 * np.cos(0.02 * self.dim))
        result *= condition_factor
        
        # Add boundary penalty with chaotic scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x[i])
            if dist_from_bound < 0:
                # Chaotic fractal scaling for boundary penalty
                fractal_scale = 1.0 + 0.1 * np.sin(0.2 * i + 0.05 * np.sin(0.1 * i)) + 0.05 * np.cos(0.1 * i + 0.02 * np.cos(0.05 * i))
                boundary_penalty += 5.0 * np.exp(-dist_from_bound**2 * fractal_scale)
        result += boundary_penalty
        
        # Add a chaotic noise component with fractal structure
        noise = 0.0
        for i in range(self.dim):
            # Chaotic noise with fractal modulation
            noise += 0.05 * np.sin(5.0 * x[i] + 0.3 * i + 0.1 * np.sin(0.2 * i)) * np.cos(3.0 * x[i]**2 + 0.2 * i + 0.05 * np.cos(0.1 * i))
        result += noise
        
        # Add a global scaling factor with chaotic modulation
        global_scale = 1.0 + 0.1 * np.sin(0.05 * self.dim + 0.05 * np.sin(0.02 * self.dim)) + 0.05 * np.cos(0.02 * self.dim + 0.02 * np.cos(0.01 * self.dim))
        result *= global_scale
        
        # Add chaotic harmonic perturbations
        harmonic_pert = 0.0
        for i in range(self.dim):
            harmonic_pert += 0.02 * np.sin(7.0 * x[i] + 0.1 * np.sin(3.0 * x[i])) * np.cos(4.0 * x[i]**2 + 0.05 * np.cos(2.0 * x[i]))
        result += harmonic_pert
        
        return result