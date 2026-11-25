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
            freq = 1.0 + 1.0 * self.chaotic_sequence[i]  # Reduced frequency modulation
            f2 -= 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Spherical harmonic interactions with adaptive coupling
        f3 = 0.3 * np.sum(np.sin(x) * np.cos(2.0 * x))  # Reduced coefficient
        
        # Logistic map chaotic modulation
        f4 = 0.25 * np.sum(np.sin(np.pi * np.log(1 + np.abs(x))) * np.cos(3.0 * x))
        
        # Cross-dimensional coupling with exponential weighting
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 1))  # Slightly different weighting
            cross_interaction += weight * np.sin(x[i] * x[i+1])
        f5 = 0.3 * cross_interaction  # Reduced coefficient
        
        # Adaptive polynomial chaos with fractal-like behavior
        f6 = 0.15 * np.sum((x**4) * np.sin(2.0 * x))  # Reduced coefficient
        
        # Sigmoidal scaling with chaotic modulation
        f7 = 0.25 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x))  # Reduced coefficient
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 1.8 + 0.4 * np.sin(np.sum(x**2) / 10.0)  # Altered base frequency
        f8 = 0.2 * np.sum(np.sin(freq * x) * np.cos(2.0 * x))  # Reduced coefficient
        
        # Nonlinear correlation with exponential weighting
        f9 = 0.15 * np.sum(np.exp(-x**2) * x**3)  # Reduced coefficient
        
        # Additional higher-order terms for increased complexity (mutated)
        f10 = 0.08 * np.sum(x**6 * np.cos(x/3))  # Reduced coefficient
        f11 = 0.15 * np.sum(np.abs(x)**2.5)      # Reduced coefficient
        
        # New term: sixth-order polynomial with cosine modulation (slightly modified)
        f12 = 0.1 * np.sum((x**6) * np.cos(1.3 * x))  # Altered frequency
        
        # Additional noise modulation term
        noise = 0.08 * np.sum(np.sin(7.0 * x) * np.cos(5.0 * x))  # Reduced noise level
        
        # New fractal-like coupling term (modified interaction)
        fractal_coupling = 0.0
        for i in range(self.dim - 2):
            fractal_coupling += np.sin(x[i] * x[i+1] * x[i+2] * 0.25)  # Scaled interaction
        f13 = 0.12 * fractal_coupling  # Reduced coefficient
        
        # Combined scaling based on dimensionality (adjusted)
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)  # Reduced scaling
        
        # New term: seventh-order polynomial with modified frequency and additional cosine modulation
        f14 = 0.15 * np.sum((x**7) * np.cos(1.5 * x) * np.sin(0.5 * x))  # Added sine modulation
        
        # Additional mutation: enhanced coupling between odd/even dimensions
        odd_even_coupling = 0.0
        for i in range(0, self.dim - 1, 2):
            odd_even_coupling += np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
        f15 = 0.2 * odd_even_coupling  # Reduced coefficient
        
        # Modified noise interaction with dynamic scaling
        dynamic_noise = 0.06 * np.sum(np.sin(4.0 * x) * np.cos(2.0 * x) * np.exp(-x**2/10))
        
        # Additional complex coupling term: trigonometric polynomial with varying exponents
        complex_coupling = 0.0
        for i in range(self.dim - 3):
            complex_coupling += np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(x[i+3])
        f16 = 0.12 * complex_coupling  # Reduced coefficient
        
        # Hyperchaotic oscillation with multiple frequencies
        hyperchaos = 0.0
        for i in range(self.dim):
            hyperchaos += np.sin(2.3 * x[i]) * np.cos(1.1 * x[i]) * np.tan(0.6 * x[i])
        f17 = 0.18 * hyperchaos  # Reduced coefficient
        
        # Multi-scale fractal coupling with exponential decay
        multi_scale_coupling = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i**2 / (self.dim**2 + 1))
            multi_scale_coupling += weight * np.sin(x[i] * x[i+1]**2)
        f18 = 0.08 * multi_scale_coupling  # Reduced coefficient
        
        # High-order polynomial with chaotic modulation
        high_order_poly = 0.0
        for i in range(self.dim):
            high_order_poly += (x[i]**8) * np.sin(0.4 * x[i]) * np.cos(1.0 * x[i])
        f19 = 0.1 * high_order_poly  # Reduced coefficient
        
        # New coupling term: interaction with cubic roots
        cubic_coupling = 0.0
        for i in range(self.dim - 2):
            cubic_coupling += np.sin(np.cbrt(x[i]) * x[i+1] * x[i+2])
        f20 = 0.08 * cubic_coupling  # Reduced coefficient
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + noise + f13 + f14 + f15 + dynamic_noise + f16 + f17 + f18 + f19 + f20)