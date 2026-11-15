import numpy as np

class FractalSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute fractal-like frequency patterns
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Precompute polynomial chaos coefficients
        self.poly_coeffs = np.random.randn(dim, 5) * 0.1
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Apply polynomial chaos expansion
        poly_result = 0.0
        for i in range(self.dim):
            x_i = x[i]
            # Evaluate polynomial chaos expansion up to 4th order
            poly_val = (self.poly_coeffs[i, 0] + 
                       self.poly_coeffs[i, 1] * x_i + 
                       self.poly_coeffs[i, 2] * x_i**2 + 
                       self.poly_coeffs[i, 3] * x_i**3 + 
                       self.poly_coeffs[i, 4] * x_i**4)
            poly_result += poly_val
        
        # Fractal-like sine-wave interactions
        sine_result = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            phase = self.phases[i]
            # Add fractal-like interaction with multiple scales
            sine_result += amp * np.sin(freq * x[i] + phase) * \
                          (1.0 + 0.3 * np.sin(2.0 * freq * x[i] + phase) + 
                           0.2 * np.sin(3.0 * freq * x[i] + phase))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.1 * np.sin(0.1 * self.dim) + 0.05 * np.cos(0.05 * self.dim)
        
        # Cross-dimension coupling with fractal scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with exponentially decaying interaction
                coupling_strength = 0.1 * np.exp(-0.1 * np.abs(i-j))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Boundary penalty with fractal-like scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x[i])
            if dist_from_bound < 0:
                boundary_penalty += 5.0 * np.exp(-dist_from_bound**2) * (1.0 + 0.2 * np.sin(3.0 * x[i]))
        
        # Combine all components
        result = condition_factor * (poly_result + sine_result + cross_coupling) + boundary_penalty
        
        # Add a global scaling factor
        global_scale = 1.0 + 0.05 * np.sin(0.02 * self.dim)
        result *= global_scale
        
        return result