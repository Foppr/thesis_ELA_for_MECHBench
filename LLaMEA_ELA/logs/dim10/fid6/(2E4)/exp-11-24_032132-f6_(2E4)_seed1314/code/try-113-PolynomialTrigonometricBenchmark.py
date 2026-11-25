import numpy as np

class PolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.noise_level = 0.1
        self.time_phase = 0.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying phase for dynamic behavior
        self.time_phase = (self.time_phase + 0.02) % (2 * np.pi)
        
        # Polynomial chaos component with adaptive coefficients
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Time-varying polynomial coefficients
            a = 1.0 + 0.3 * np.sin(self.time_phase + i * 0.5)
            b = 0.5 + 0.2 * np.cos(self.time_phase + i * 0.3)
            c = 0.8 + 0.4 * np.sin(self.time_phase * 1.2 + i * 0.7)
            d = 0.3 + 0.1 * np.cos(self.time_phase * 0.8 + i * 0.9)
            poly_term += a * xi**4 + b * xi**3 + c * xi**2 + d * xi
        
        # Trigonometric coupling component
        trig_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-frequency trigonometric interactions
            trig_term += (np.sin(xi * 1.5 + self.time_phase) * np.cos(xi * 2.3 + self.time_phase * 0.6) +
                         np.sin(xi * 3.7 + self.time_phase * 1.1) * np.cos(xi * 4.2 + self.time_phase * 0.9) +
                         np.sin(xi * 5.8 + self.time_phase * 1.5) * np.cos(xi * 6.1 + self.time_phase * 1.3))
        
        # Cross-dimensional coupling with adaptive weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on time and dimension
                coupling_strength = 0.5 + 0.3 * np.sin(self.time_phase + i * 0.4 + j * 0.3)
                cross_term += coupling_strength * (np.sin(x[i] + x[j]) + np.cos(x[i] - x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Adaptive noise component
        noise_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Time-varying noise with dimension-specific scaling
            noise_scale = 0.2 + 0.1 * np.sin(self.time_phase + i * 0.6)
            noise_term += noise_scale * np.random.normal(0, 1) * np.exp(-0.05 * xi**2)
        
        # Combine all terms with dynamic weighting
        weight_poly = 0.8 + 0.2 * np.sin(self.time_phase * 0.7)
        weight_trig = 0.6 + 0.4 * np.cos(self.time_phase * 1.3)
        weight_cross = 0.7 + 0.3 * np.sin(self.time_phase * 1.1)
        weight_noise = 0.5 + 0.3 * np.cos(self.time_phase * 0.9)
        
        return (weight_poly * poly_term + 
                weight_trig * trig_term + 
                weight_cross * cross_term + 
                weight_noise * noise_term)