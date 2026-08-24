import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for enhanced complexity
        self.chaos_factors = np.sin(np.linspace(0, 2*np.pi, dim)) * 2.0 + 1.5
        self.peak_positions = np.linspace(-4.5, 4.5, 11)
        self.interaction_weights = np.random.rand(dim, dim) * 0.5 + 0.25
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal component with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.7) * self.chaos_factors[i]
            amp = 1.5 + 0.5 * np.cos(i * 0.9) * self.chaos_factors[i]
            chaotic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Fractal-like peak structure with varying heights and widths
        fractal_peaks = 0.0
        for center in self.peak_positions:
            width = 0.3 + 0.7 * np.sin(center * 0.8) ** 2
            height = 2.0 + 1.0 * np.cos(center * 0.6)
            fractal_peaks += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 4))
        
        # Saddle-point interaction with cross-dimensional coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.interaction_weights[i, j]
                saddle += coupling * np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Asymmetric exponential decay with chaotic rates
        asym_exp = 0.0
        for i in range(self.dim):
            rate = 0.1 + 0.8 * np.sin(i * 0.5) * self.chaos_factors[i]
            asym_exp += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 0.5)
        
        # Polynomial with fractional exponents and chaotic conditioning
        poly_frac = 0.0
        for i in range(self.dim):
            degree = 1.5 + 1.5 * np.sin(i * 0.6) * self.chaos_factors[i]
            poly_frac += (x[i] ** degree) * (1.0 + 0.3 * np.cos(i * 0.4))
        
        # Logarithmic spiral component for additional nonlinearity
        spiral = 0.0
        for i in range(self.dim):
            spiral += np.log(np.abs(x[i]) + 1.0) * np.sin(x[i] * 0.2) * np.cos(x[i] * 0.1)
        
        # Combine all components with adaptive weights
        weights = np.array([0.8, 0.7, 0.9, 0.6, 0.5, 0.4])
        components = np.array([chaotic, fractal_peaks, saddle, asym_exp, poly_frac, spiral])
        return np.sum(weights * components)