import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like scaling
        r = np.sqrt(np.sum(x**2))
        radial_term = r * np.sin(15 * r) * np.cos(7 * r)
        
        # Multi-scale sinusoidal modulation with chaotic frequency ratios
        modulated_sum = 0.0
        frequencies = [1.0, 1.618, 2.718, 3.142, 4.236, 5.828, 6.902]  # Extended set with more transcendental constants
        for i in range(min(self.dim, len(frequencies))):
            freq = frequencies[i % len(frequencies)]
            modulated_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.sin(0.15 * x[i]**2)
        
        # Rotational symmetry breaking with polynomial weights
        rotation_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                rotation_term += (x[i]**3 + x[j]**3) * np.sin(4 * angle) * np.cos(3 * angle)
        
        # Adaptive conditioning based on dimensionality and position
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.9) + 0.4 * np.cos(r * 0.5)
        
        # Multi-scale interference pattern using wavelets with higher frequency components
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-0.3 * (x[i] - np.sin(i*0.7))**2) * np.sin(15 * x[i]) * np.cos(8 * x[i])
        
        # Nested fractal structures with recursive interaction terms
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fractal_term += np.sin(20 * dist) * np.cos(10 * dist) * (1.0 / (1.0 + dist**2))
        
        # Enhanced nonlinearity with exponential coupling
        nonlinear_coupling = 0.0
        for i in range(self.dim):
            nonlinear_coupling += np.exp(-0.1 * x[i]**2) * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Combine all terms with increased complexity and interaction
        return condition_factor * (radial_term + 0.8 * modulated_sum + 0.4 * rotation_term + 0.3 * interference + 0.2 * fractal_term + 0.15 * nonlinear_coupling)