import numpy as np

class FractalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_base = 1.5
        self.harm_freq = 2.0 * np.pi
        self.coupling_strength = 0.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like radial component with self-similar structure
        r = np.sqrt(np.sum(x**2))
        fractal_component = 0
        for i in range(self.dim):
            # Self-similar harmonic terms with varying scales
            scale = self.fractal_base ** (i % 3)
            fractal_component += np.sin(scale * self.harm_freq * x[i]) * np.cos(scale * self.harm_freq * x[i] * 0.5)
        
        # Radial harmonic oscillation with fractal scaling
        radial_harmonic = 0
        if r > 1e-10:
            for k in range(1, 4):
                radial_harmonic += np.sin(k * self.harm_freq * r) * np.cos(k * self.harm_freq * r * 0.3)
        
        # Cross-dimensional coupling with fractal weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (self.fractal_base ** (i % 2)) * (self.fractal_base ** (j % 2))
                coupling += weight * np.sin(self.harm_freq * x[i] * x[j]) * np.cos(self.harm_freq * x[i] * x[j] * 0.7)
        
        # Polynomial radial term with fractal-like curvature
        poly_radial = 0
        for i in range(self.dim):
            poly_radial += (x[i] ** 3) * (self.fractal_base ** (i % 4))
        
        # Additional harmonic modulation based on all dimensions
        total_harmonic = 0
        for i in range(self.dim):
            total_harmonic += np.sin(self.harm_freq * x[i] * (1 + 0.1 * i)) * np.cos(self.harm_freq * x[i] * (1 + 0.05 * i))
        
        # Combine all components with appropriate scaling
        return (0.25 * r**2 + 
                2.1 * fractal_component + 
                0.8 * radial_harmonic + 
                0.6 * coupling + 
                0.4 * poly_radial + 
                1.3 * total_harmonic)