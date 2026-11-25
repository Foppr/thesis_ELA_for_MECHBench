import numpy as np

class FractalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Initialize fractal parameters for each dimension
        self.hurst_exponents = 0.3 + 0.4 * np.random.rand(dim)
        self.fractal_amplitudes = 1.0 + 2.0 * np.random.rand(dim)
        self.polynomial_degrees = 3 + np.random.randint(0, 3, dim)
        # Chaos parameters for Brownian motion
        self.chaos_params = 0.5 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion term
        poly_term = 0.0
        for i in range(self.dim):
            degree = self.polynomial_degrees[i]
            poly_term += np.sum((x[i] ** degree) * np.sin(i * x[i] + self.chaos_params[i]))
        
        # Fractal Brownian motion component
        fbm_term = 0.0
        for i in range(self.dim):
            # Generate fractal noise using Hurst exponent
            hurst = self.hurst_exponents[i]
            amplitude = self.fractal_amplitudes[i]
            
            # Simple fractal noise approximation using multiple sine waves
            noise = 0.0
            for k in range(1, 6):
                freq = k * (1 + 0.1 * np.sin(i * 0.5))
                phase = k * np.cos(i * 0.3)
                noise += amplitude * (1/k) ** hurst * np.sin(freq * x[i] + phase)
            
            fbm_term += noise
        
        # Multi-scale interaction term
        scale_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-dependent interaction with fractal characteristics
                scale_factor = (i + 1) * (j + 1)
                dist = np.abs(x[i] - x[j])
                interaction = np.exp(-dist**2 / (0.5 * scale_factor)) * np.sin(scale_factor * (x[i] + x[j]))
                scale_term += interaction
        
        # Add a global scaling factor and noise
        global_scaling = 1.0 + 0.1 * np.sum(np.sin(x)**2)
        
        # Combine all terms with different weights
        return 0.5 * poly_term + 0.3 * fbm_term + 0.2 * scale_term * global_scaling