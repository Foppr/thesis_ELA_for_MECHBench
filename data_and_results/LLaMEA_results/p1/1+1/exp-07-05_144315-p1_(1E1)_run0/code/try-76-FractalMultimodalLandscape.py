import numpy as np

class FractalMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like behavior
        radial = np.sum(x**2 * np.exp(-0.1 * np.abs(x)))
        
        # Nested sinusoidal waves with varying frequencies and amplitudes
        nested_sin = 0.0
        for i in range(1, 6):
            freq = i * 2.0
            amp = 1.0 / i
            nested_sin += amp * np.sum(np.sin(freq * x) * np.cos(freq * x) * np.exp(-0.05 * x**2))
        
        # Radial basis functions with varying centers and widths
        rbf = 0.0
        centers = np.linspace(-4.0, 4.0, 9)
        widths = np.logspace(-1, 1, 9)
        for i, (center, width) in enumerate(zip(centers, widths)):
            rbf += np.exp(-width * np.sum((x - center)**2)) * np.sin(2 * np.pi * (x - center))
        
        # Chaotic perturbation using logistic map-inspired terms
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.sin(x[i])) * np.cos(5 * np.sin(x[i])) * np.exp(-0.03 * x[i]**2)
        
        # Cross-dimensional interaction with fractal scaling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1 + 0.1 * np.sin(3 * (x[i] + x[j])))
        
        # High-frequency oscillatory component
        high_freq = 0.5 * np.sum(np.sin(15 * x) * np.cos(12 * x) * np.exp(-0.02 * x**2))
        
        # Fractal dimensionality scaling
        fractal_scale = 1.0 + 0.2 * np.sum(np.sin(x) * np.cos(x) * np.exp(-0.01 * x**2))
        
        # Combine all components
        return radial + 0.7 * nested_sin + 0.5 * rbf + 0.3 * chaotic + 0.4 * cross_interaction + high_freq + fractal_scale