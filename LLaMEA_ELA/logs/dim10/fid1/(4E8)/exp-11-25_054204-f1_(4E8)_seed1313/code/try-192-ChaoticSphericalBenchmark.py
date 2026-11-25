import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.log(np.arange(1, dim + 1)) / np.log(dim + 1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic spherical harmonic component with dynamic frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 1.2 * self.chaotic_sequence[i]  # Increased frequency modulation
            f2 -= 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Spherical harmonic interactions with adaptive coupling
        f3 = 0.4 * np.sum(np.sin(x) * np.cos(2.0 * x))  # Increased coefficient
        
        # Logistic map chaotic modulation
        f4 = 0.3 * np.sum(np.sin(np.pi * np.log(1 + np.abs(x))) * np.cos(3.0 * x))
        
        # Cross-dimensional coupling with exponential weighting
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 2))  # Slightly different weighting
            cross_interaction += weight * np.sin(x[i] * x[i+1])
        f5 = 0.4 * cross_interaction  # Increased coefficient
        
        # Adaptive polynomial chaos with fractal-like behavior
        f6 = 0.2 * np.sum((x**4) * np.sin(2.0 * x))  # Slightly increased coefficient
        
        # Sigmoidal scaling with chaotic modulation
        f7 = 0.3 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x))  # Increased coefficient
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 2.0 + 0.5 * np.sin(np.sum(x**2) / 10.0)  # Slightly altered base frequency
        f8 = 0.25 * np.sum(np.sin(freq * x) * np.cos(2.0 * x))  # Increased coefficient
        
        # Nonlinear correlation with exponential weighting
        f9 = 0.2 * np.sum(np.exp(-x**2) * x**3)  # Increased coefficient
        
        # Additional higher-order terms for increased complexity (mutated)
        f10 = 0.1 * np.sum(x**6 * np.cos(x/3))  # Slightly increased coefficient
        f11 = 0.2 * np.sum(np.abs(x)**2.5)      # Increased coefficient
        
        # New term: sixth-order polynomial with cosine modulation (slightly modified)
        f12 = 0.12 * np.sum((x**6) * np.cos(1.5 * x))  # Slightly altered frequency
        
        # Additional noise modulation term
        noise = 0.1 * np.sum(np.sin(7.0 * x) * np.cos(5.0 * x))  # Increased noise level
        
        # New fractal-like coupling term (modified interaction)
        fractal_coupling = 0.0
        for i in range(self.dim - 2):
            fractal_coupling += np.sin(x[i] * x[i+1] * x[i+2] * 0.3)  # Scaled interaction
        f13 = 0.15 * fractal_coupling
        
        # Combined scaling based on dimensionality (adjusted)
        scale_factor = 1.0 + 0.6 * np.log(self.dim + 1)  # Slightly increased scaling
        
        # New term: seventh-order polynomial with modified frequency and additional cosine modulation
        f14 = 0.18 * np.sum((x**7) * np.cos(1.7 * x) * np.sin(0.6 * x))  # Added sine modulation
        
        # Additional mutation: enhanced coupling between odd/even dimensions
        odd_even_coupling = 0.0
        for i in range(0, self.dim - 1, 2):
            odd_even_coupling += np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
        f15 = 0.25 * odd_even_coupling
        
        # Modified noise interaction with dynamic scaling
        dynamic_noise = 0.08 * np.sum(np.sin(4.0 * x) * np.cos(2.0 * x) * np.exp(-x**2/10))
        
        # Additional complex coupling term: trigonometric polynomial with varying exponents
        complex_coupling = 0.0
        for i in range(self.dim - 3):
            complex_coupling += np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(x[i+3])
        f16 = 0.15 * complex_coupling
        
        # Hyperchaotic oscillation with multiple frequencies
        hyperchaos = 0.0
        for i in range(self.dim):
            hyperchaos += np.sin(2.5 * x[i]) * np.cos(1.3 * x[i]) * np.tan(0.7 * x[i])
        f17 = 0.2 * hyperchaos
        
        # Multi-scale fractal coupling with exponential decay
        multi_scale_coupling = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i**2 / (self.dim**2 + 1))
            multi_scale_coupling += weight * np.sin(x[i] * x[i+1]**2)
        f18 = 0.1 * multi_scale_coupling
        
        # High-order polynomial with chaotic modulation
        high_order_poly = 0.0
        for i in range(self.dim):
            high_order_poly += (x[i]**8) * np.sin(0.5 * x[i]) * np.cos(1.2 * x[i])
        f19 = 0.13 * high_order_poly
        
        # New coupling term: interaction with cubic roots
        cubic_coupling = 0.0
        for i in range(self.dim - 2):
            cubic_coupling += np.sin(np.cbrt(x[i]) * x[i+1] * x[i+2])
        f20 = 0.1 * cubic_coupling
        
        # Improved fitness function with better conditioning and reduced bias
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + noise + f13 + f14 + f15 + dynamic_noise + f16 + f17 + f18 + f19 + f20) + 0.01 * np.sum(np.sin(10.0 * x))