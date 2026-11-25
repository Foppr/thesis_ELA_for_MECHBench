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
            freq = 1.0 + 4.0 * self.chaotic_sequence[i]  # Increased frequency modulation
            f2 -= 0.9 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Spherical harmonic interactions with adaptive coupling
        f3 = 0.8 * np.sum(np.sin(x) * np.cos(3.0 * x))  # Increased coefficient
        
        # Logistic map chaotic modulation
        f4 = 0.5 * np.sum(np.sin(np.pi * np.log(1 + np.abs(x))) * np.cos(4.0 * x))
        
        # Cross-dimensional coupling with exponential weighting
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 2))  # Slightly different weighting
            cross_interaction += weight * np.sin(x[i] * x[i+1])
        f5 = 0.8 * cross_interaction  # Increased coefficient
        
        # Adaptive polynomial chaos with fractal-like behavior
        f6 = 0.5 * np.sum((x**4) * np.sin(3.0 * x))  # Slightly increased coefficient
        
        # Sigmoidal scaling with chaotic modulation
        f7 = 0.6 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x))  # Increased coefficient
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 4.0 + 1.5 * np.sin(np.sum(x**2) / 15.0)  # Slightly altered base frequency
        f8 = 0.5 * np.sum(np.sin(freq * x) * np.cos(3.0 * x))  # Increased coefficient
        
        # Nonlinear correlation with exponential weighting
        f9 = 0.5 * np.sum(np.exp(-x**2) * x**3)  # Increased coefficient
        
        # Additional higher-order terms for increased complexity (mutated)
        f10 = 0.4 * np.sum(x**6 * np.cos(x/2))  # Slightly increased coefficient
        f11 = 0.5 * np.sum(np.abs(x)**3.0)      # Increased coefficient
        
        # New term: sixth-order polynomial with cosine modulation (slightly modified)
        f12 = 0.4 * np.sum((x**6) * np.cos(2.0 * x))  # Slightly altered frequency
        
        # Additional noise modulation term
        noise = 0.3 * np.sum(np.sin(10.0 * x) * np.cos(8.0 * x))
        
        # New fractal-like coupling term (modified interaction)
        fractal_coupling = 0.0
        for i in range(self.dim - 2):
            fractal_coupling += np.sin(x[i] * x[i+1] * x[i+2] * 0.8)  # Scaled interaction
        f13 = 0.4 * fractal_coupling
        
        # Combined scaling based on dimensionality (adjusted)
        scale_factor = 1.0 + 1.0 * np.log(self.dim + 1)  # Slightly increased scaling
        
        # New term: seventh-order polynomial with modified frequency
        f14 = 0.4 * np.sum((x**7) * np.cos(2.5 * x))
        
        # Mutated term: eighth-order polynomial with sine modulation
        f15 = 0.4 * np.sum((x**8) * np.sin(2.0 * x))
        
        # Additional multimodal component for enhanced conditioning
        f16 = 0.4 * np.sum(np.sin(5.0 * x) * np.cos(6.0 * x) * np.exp(-x**2 / 7.0))
        
        # Modified fractal coupling with cubic interaction
        f17 = 0.3 * np.sum(np.sin(x**3) * np.cos(x**2))  # Cubic modulation
        
        # Adjusted chaotic modulation with logarithmic scaling
        f18 = 0.4 * np.sum(np.log(1 + np.abs(x)) * np.sin(3.5 * x))
        
        # New term: ninth-order polynomial with modified frequency (mutated)
        f19 = 0.3 * np.sum((x**9) * np.cos(2.0 * x))
        
        # Mutated cross-dimensional coupling with inverse weighting
        cross_interaction_inv = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 / (1.0 + i * 0.9)  # Inverse weighting with scaling
            cross_interaction_inv += weight * np.cos(x[i] * x[i+1])
        f20 = 0.4 * cross_interaction_inv
        
        # New term: tenth-order polynomial with sine modulation
        f21 = 0.2 * np.sum((x**10) * np.sin(1.6 * x))
        
        # Additional fractal coupling with quartic interaction
        f22 = 0.2 * np.sum(np.sin(x**4) * np.cos(x**3))  # Quartic modulation
        
        # Slight modification: Adjusted coefficient for the logistic map term
        f4 = 0.5 * np.sum(np.sin(np.pi * np.log(1 + np.abs(x))) * np.cos(4.0 * x))
        
        # Additional complex fractal coupling with quintic interaction
        f23 = 0.15 * np.sum(np.sin(x**5) * np.cos(x**4))  # Quintic modulation
        
        # New term: eleventh-order polynomial with cosine modulation
        f24 = 0.15 * np.sum((x**11) * np.cos(1.8 * x))
        
        # Additional chaotic harmonic with modified exponent
        f25 = 0.25 * np.sum(np.sin(x**2.0) * np.cos(3.5 * x))
        
        # Final combined function with refined weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + noise + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20 + f21 + f22 + f23 + f24 + f25)