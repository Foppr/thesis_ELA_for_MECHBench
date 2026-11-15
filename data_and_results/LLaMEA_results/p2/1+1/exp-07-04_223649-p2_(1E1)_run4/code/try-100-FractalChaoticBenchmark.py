import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.scaling_factors = np.array([1.0 / (2**i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Fractal-like self-similar sinusoidal components with varying scales
        fractal_terms = 0.0
        for i in range(1, min(6, self.dim + 1)):
            scale = self.scaling_factors[min(i, len(self.scaling_factors) - 1)]
            fractal_terms += scale * np.sum(np.sin(2**(i-1) * np.pi * x) * np.cos(2**i * np.pi * x))
        
        # Adaptive conditioning with dimension-dependent parameters
        adaptive_cond = 0.0
        for i in range(self.dim):
            adaptive_cond += (i + 1) * np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 1)**2)
        
        # Chaotic perturbation using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(np.pi * x[i] * np.sin(x[i])) * np.cos(np.pi * x[i] * np.cos(x[i]))
        
        # Multimodal peaks with varying amplitudes and frequencies
        peaks = 0.0
        for i in range(self.dim):
            peaks += np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(x[i] * x[i+1])
        
        # Resonance terms with varying phase shifts
        resonance = 0.0
        for i in range(self.dim):
            resonance += np.sin(x[i] + np.sin(x[i])) * np.cos(x[i] + np.cos(x[i]))
        
        # Asymmetric polynomial distortions with exponential weights
        poly_distortion = 0.0
        for i in range(self.dim):
            poly_distortion += (i + 1) * (x[i]**3 + 0.5 * x[i]**5) * np.exp(-0.1 * np.abs(x[i]))
        
        # Combine all terms
        result = result + fractal_terms + adaptive_cond + chaotic + peaks + coupling + resonance + poly_distortion
        
        return result