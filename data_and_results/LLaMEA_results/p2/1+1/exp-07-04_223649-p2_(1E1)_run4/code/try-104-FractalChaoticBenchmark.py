import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Fractal-like chaotic component with recursive sine-cosine patterns
        fractal = 0.0
        for i in range(1, 6):
            fractal += np.sum(np.sin(2**i * np.pi * x) * np.cos(3**i * np.pi * x) * np.exp(-0.1 * i))
        
        # Hybrid exponential-polynomial coupling with dynamic exponents
        exp_poly = 0.0
        for i in range(self.dim - 1):
            exp_poly += np.exp(-0.5 * (x[i] - x[i+1])**2) * (x[i]**3 + x[i+1]**4)
        
        # Dynamic gradient modulation using hyperbolic tangent
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.tanh(x[i]) * np.sin(0.5 * x[i]**2) * np.cos(0.3 * x[i])
        
        # Multi-scale multimodal peaks with varying amplitudes and frequencies
        peaks = 0.0
        scales = [1.0, 2.0, 3.0, 4.0]
        for scale in scales:
            peaks += np.sum(np.exp(-0.5 * (x - scale)**2) * np.sin(scale * x)**2)
        
        # Cross-dimensional interaction with fractional powers
        fractional = 0.0
        for i in range(self.dim - 1):
            fractional += (x[i]**0.7 * x[i+1]**1.3) * np.sin(x[i] + x[i+1])
        
        # Asymmetric bell-shaped distortions with time-varying parameters
        asymmetric = 0.0
        for i in range(self.dim):
            asymmetric += (x[i]**2 + 0.5 * x[i]**4) * np.exp(-0.1 * x[i]**2) * np.cos(2 * x[i])
        
        # Combined result
        result = result + fractal + exp_poly + grad_mod + peaks + fractional + asymmetric
        
        return result