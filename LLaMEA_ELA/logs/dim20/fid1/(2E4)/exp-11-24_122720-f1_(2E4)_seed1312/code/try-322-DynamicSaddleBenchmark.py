import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic gradient parameters
        self.chaos_params = np.random.uniform(0.1, 2.0, dim)
        # Fractal coupling coefficients
        self.fractal_coeffs = np.random.uniform(0.5, 1.5, dim)
        # Hyperbolic saddle point configurations
        self.hyper_saddles = np.random.uniform(-4.0, 4.0, (dim, 3))
        self.saddle_strengths = np.random.uniform(1.0, 3.0, dim)
        # Chaotic modulation frequencies
        self.freqs = np.random.uniform(2.0, 8.0, dim)
        # Non-smoothness parameters
        self.nonsmooth_params = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient interaction component
        chaotic = 0.0
        for i in range(self.dim):
            # Apply chaotic modulation with fractal coupling
            chaotic += self.fractal_coeffs[i] * np.sin(self.chaos_params[i] * x[i]) * np.cos(self.freqs[i] * x[i])
            
        # Fractal coupling component with hyperbolic saddle dynamics
        fractal = 0.0
        for i in range(self.dim):
            # Hyperbolic attraction to multiple saddle points
            saddle_sum = 0.0
            for j in range(3):
                s = self.hyper_saddles[i, j]
                strength = self.saddle_strengths[i]
                # Hyperbolic term with non-smoothness
                saddle_sum += strength * np.tanh((x[i] - s)**2) / (1.0 + np.exp(-self.nonsmooth_params[i] * (x[i] - s)))
            fractal += saddle_sum
            
        # Sinusoidal modulation with exponential decay
        sin_mod = 0.0
        for i in range(self.dim):
            # Multi-frequency sinusoidal with chaotic envelope
            envelope = np.exp(-0.1 * x[i]**2)
            sin_mod += envelope * (np.sin(self.freqs[i] * x[i]) + 0.5 * np.sin(2.0 * self.freqs[i] * x[i]))
            
        # Cross-dimension hyperbolic interaction
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-interaction
                # Hyperbolic coupling with chaotic weights
                weight = np.tanh(self.chaos_params[i] * self.chaos_params[j]) * np.exp(-0.05 * (i + j))
                cross += weight * np.sinh(x[i] * x[j]) * np.cosh(0.3 * (x[i] + x[j]))
                
        # Polynomial with chaotic exponents
        poly = 0.0
        for i in range(self.dim):
            # Chaotic degree selection
            degree = 2 + int(np.abs(np.sin(self.chaos_params[i])) * 4) % 5
            poly += np.sign(x[i]) * np.abs(x[i])**degree
            
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(self.freqs[i] * x[i] * np.cos(x[i])) * np.exp(-0.01 * x[i]**2)
            
        # Combine all components with dynamic scaling
        result = 1.8 * chaotic + 1.2 * fractal + 1.0 * sin_mod + 0.9 * cross + 0.7 * poly + 0.5 * noise
        
        # Add dimensionality-dependent normalization and chaotic bias
        norm_factor = np.sqrt(self.dim) * (1.0 + 0.1 * np.sin(self.dim))
        result /= norm_factor
        
        return result