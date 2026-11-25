import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like sequence for dynamic scaling
        self.fractal_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base spherical term with fractal modulation
        f1 = np.sum(x**2)
        
        # Chaotic coupling with dynamic scaling
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.5 * self.fractal_sequence[i]
            f2 += 0.6 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial fractal interaction with dynamic scaling
        radial = np.sum(x**2)
        f3 = 0.5 * np.sin(np.sqrt(radial) * 4.5) * np.cos(np.sqrt(radial) * 3.5)
        
        # Cross-dimensional coupling with polynomial weights
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = (i + 1) / (self.dim + 2)
            cross_interaction += weight * np.sin(x[i] + x[i+1])
        f4 = 0.4 * cross_interaction
        
        # Polynomial chaos with fractal-like behavior
        f5 = 0.3 * np.sum((x**3) * np.sin(1.8 * x))
        
        # Sigmoidal scaling with trigonometric modulation
        f6 = 0.25 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x))
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 2.5 + 1.2 * np.sin(np.sum(x**2) / 8.0)
        f7 = 0.35 * np.sum(np.sin(freq * x) * np.cos(2.5 * x))
        
        # Nonlinear correlation with exponential weighting
        f8 = 0.25 * np.sum(np.exp(-x**2) * x**2)
        
        # Additional higher-order terms for increased complexity
        f9 = 0.2 * np.sum(x**5 * np.cos(x/1.5))
        f10 = 0.25 * np.sum(np.abs(x)**3.2)
        
        # Fractal-like coupling with cubic interaction
        fractal_coupling = 0.0
        for i in range(self.dim - 2):
            fractal_coupling += np.sin(x[i] * x[i+1] * x[i+2])
        f11 = 0.3 * fractal_coupling
        
        # Combined scaling based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Additional multimodal component for enhanced conditioning
        f12 = 0.2 * np.sum(np.sin(4.5 * x) * np.cos(3.5 * x) * np.exp(-x**2 / 5.0))
        
        # Modified fractal coupling with quartic interaction
        f13 = 0.2 * np.sum(np.sin(x**4) * np.cos(x**2.5))
        
        # New term: ninth-order polynomial with modified frequency
        f14 = 0.15 * np.sum((x**9) * np.cos(1.3 * x))
        
        # Mutated cross-dimensional coupling with inverse weighting
        cross_interaction_inv = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 / (1.0 + i * 0.5)
            cross_interaction_inv += weight * np.cos(x[i] * x[i+1])
        f15 = 0.25 * cross_interaction_inv
        
        # Additional chaotic harmonic with modified exponent
        f16 = 0.2 * np.sum(np.sin(x**1.7) * np.cos(2.3 * x))
        
        # Intensified chaotic coupling term
        f17 = 0.3 * np.sum(np.sin(x**2) * np.cos(x**2.5) * np.exp(-x**2 / 7.0))
        
        # Enhanced radial basis function modulation
        f18 = 0.25 * np.sum(np.exp(-np.sqrt(radial)) * np.sin(radial))
        
        # Cross-dimensional fractal coupling with higher-order terms
        f19 = 0.15 * np.sum(np.sin(x**2 + x**3) * np.cos(x**3.5))
        
        # Additional harmonic term with exponential scaling
        f20 = 0.15 * np.sum(np.exp(-x**2 / 4.0) * np.sin(6.5 * x))
        
        # New: Enhanced chaotic coupling with modified exponent and additional trigonometric modulation
        f21 = 0.25 * np.sum(np.sin(x**2.3) * np.cos(x**3.1) * np.exp(-x**2 / 6.0) * np.sin(2.7 * x))
        
        # New: Multi-scale fractal coupling with varying interaction strengths
        f22 = 0.2 * np.sum(np.sin(x**1.5) * np.cos(x**2.8) * np.tanh(x**3.2))
        
        # New: Complex polynomial with dynamic exponents and exponential weighting
        f23 = 0.18 * np.sum((x**4.7) * np.exp(-x**2 / 3.0) * np.cos(1.9 * x))
        
        # New: Coupling with inverse distance scaling and sinusoidal modulation
        f24 = 0.22 * np.sum(np.sin(x) * np.cos(x**2) / (1.0 + np.abs(x)) * np.exp(-x**2 / 8.0))
        
        # Final combined function with refined weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20 + f21 + f22 + f23 + f24)