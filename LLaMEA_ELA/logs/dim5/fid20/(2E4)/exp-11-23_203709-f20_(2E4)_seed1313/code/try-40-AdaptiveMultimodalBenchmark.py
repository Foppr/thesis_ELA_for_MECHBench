import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for conditioning
        self.conditioning = np.linspace(1.0, 10.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with adaptive conditioning
        polynomial = np.sum(self.conditioning * (x ** 4) + 0.5 * (x ** 3) - 2.0 * (x ** 2))
        
        # Trigonometric components with varying frequencies and amplitudes
        trigonometric = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.5 + 0.5 * np.cos(i * 0.3)
            trigonometric += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Radial basis function components with dynamic centers and widths
        radial = 0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i]
            width = 1.0 + 0.2 * np.sin(i * 0.8)
            radial += np.exp(-0.5 * ((x - center) / width) ** 2)
        
        # Cross-dimensional interaction terms with variable coupling strengths
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.7 * np.sin((i + j) * 0.2)
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                interaction += coupling * np.sin(3.0 * dist) / (dist + 0.01)
        
        # Adaptive noise modulation based on position
        noise_modulation = np.sum(np.sin(x) * np.cos(2 * x) * (x**2))
        
        # Combine all components with appropriate scaling
        return 2.5 * polynomial + 3.0 * trigonometric + 1.8 * radial + 0.25 * interaction + 0.1 * noise_modulation + 15.0 * self.dim