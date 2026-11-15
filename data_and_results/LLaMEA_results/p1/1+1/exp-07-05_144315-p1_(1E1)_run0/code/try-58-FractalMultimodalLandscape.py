import numpy as np

class FractalMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_factors = np.array([0.5**i for i in range(1, min(11, dim+1))])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Fractal sinusoidal component with multiple scales
        fractal_sin = 0.0
        for i in range(min(10, self.dim)):
            scale = self.fractal_factors[min(i, len(self.fractal_factors)-1)]
            fractal_sin += scale * np.sin(scale * x[i]) * np.cos(scale * x[i])
        
        # Multi-scale Gaussian peaks with varying widths
        gaussian_peaks = 0.0
        peak_centers = np.linspace(-4.0, 4.0, 9)
        for center in peak_centers:
            gaussian_peaks += np.exp(-0.5 * np.sum((x - center)**2) / 0.5**2)
        
        # Adaptive cross-term interactions based on dimension
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for computational efficiency
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Polynomial chaos component with increasing degree
        chaos_poly = 0.0
        for i in range(1, min(6, self.dim+1)):
            chaos_poly += (0.1 * i) * np.sin(i * x[i-1]) * np.cos(i * x[i-1]) if i < self.dim else 0.0
        
        # Distance-based difficulty modulation
        distance = np.sqrt(np.sum(x**2))
        difficulty_mod = 1.0 + 0.3 * np.sin(0.5 * distance)
        
        # Combine all components
        result = quadratic + 0.5 * fractal_sin + 0.3 * gaussian_peaks + 0.2 * cross_interaction + 0.1 * chaos_poly
        return result * difficulty_mod