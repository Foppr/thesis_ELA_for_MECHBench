import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial basis function component
        rbfs = 0.0
        for i in range(self.dim):
            rbfs += np.exp(-0.5 * (x[i] - self.chaotic_sequence[i])**2) * np.sin(2.0 * x[i])
        
        # Sinusoidal oscillation with dynamic frequency modulation
        sin_component = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.abs(self.chaotic_sequence[i])
            sin_component += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Chaotic cross-dimensional coupling with exponential weighting
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-np.abs(x[i] - x[i+1]) / (self.dim + 1))
            cross_coupling += weight * np.sin(x[i] * x[i+1])
        
        # Spherical harmonic with modified polynomial exponents
        spherical_harmonic = np.sum((x**3) * np.cos(2.0 * x)) + 0.5 * np.sum((x**4) * np.sin(x))
        
        # Multi-modal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (x[i]**6) * np.cos(3.0 * x[i]) + 0.5 * (x[i]**8) * np.sin(x[i])
        
        # Fractal-like interaction terms with scaling factors
        fractal_interaction = 0.0
        for i in range(self.dim):
            fractal_interaction += np.sin(x[i] * np.sqrt(i + 1)) * np.cos(x[i] / (i + 1))
        
        # Logarithmic chaotic modulation
        log_modulation = 0.0
        for i in range(self.dim):
            log_modulation += np.log(1.0 + np.abs(x[i])) * np.sin(4.0 * x[i])
        
        # Combined function with dynamic scaling based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Additional noise term for increased complexity
        noise = 0.2 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x))
        
        return scale_factor * (rbfs + sin_component + cross_coupling + spherical_harmonic + 
                              multimodal + fractal_interaction + log_modulation + noise)