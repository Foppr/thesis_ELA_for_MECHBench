import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic mapping with multiple nested sine-cosine cycles
        chaotic_term = np.sum(np.sin(25 * np.sin(np.cos(x))) * np.cos(12 * np.cos(np.sin(x))) * np.sin(8 * np.sin(x))) / self.dim
        
        # Modified polynomial with fractional powers and dynamic coefficients
        poly_term = np.sum(1.8 * x**6.5 - 1.1 * x**5.7 + 1.4 * x**4.9 - 0.8 * x**4.1 + 0.4 * x**3.3 - 0.2 * x**2.5 + 0.9 * x) / self.dim
        
        # Improved quantum-inspired barrier with multi-frequency modulation
        barrier_term = np.sum(np.exp(-x**2 / 2.5) * np.sin(6 * x) * np.cos(3 * x) * np.sin(x/2.5) * np.cos(x/4.0)) / self.dim
        
        # Refined multi-scale chaotic attractor with logarithmic scaling
        attractor_term = np.sum(np.sin(np.log(np.abs(x) + 1.0)) * np.cos(np.log(np.abs(x) + 2.0)) * np.sin(x/3.5) * np.cos(x/6.0)) / self.dim
        
        # Enhanced cross-dimensional coupling with dynamic phase shifts
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                phase_shift = 0.5 * np.sin(i * np.pi / self.dim)
                cross_term += np.abs(x[i] - x[i+1])**(1.7 + 0.3 * np.cos(i * np.pi / self.dim) + phase_shift)
        cross_term /= (self.dim - 1)
        
        # Advanced noise component with fractal-like structure
        noise = 0.012 * np.random.rand() + 0.006 * np.sin(np.sum(x**2)) + 0.004 * np.cos(np.sum(x**3)) + 0.002 * np.sin(np.sum(x**4))
        
        # Dynamic weighting with improved balance
        result = 0.35 * chaotic_term + 0.28 * poly_term + 0.22 * barrier_term + 0.12 * attractor_term + 0.03 * cross_term
        
        return result + noise