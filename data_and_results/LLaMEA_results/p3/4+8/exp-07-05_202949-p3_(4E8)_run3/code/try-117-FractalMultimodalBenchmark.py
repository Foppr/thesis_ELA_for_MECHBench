import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like scaling factors
        self.scales = np.power(2.0, np.arange(dim) % 5)
        self.fractal_exponents = 0.5 + 0.5 * np.sin(np.arange(dim) * np.pi / 4.0)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Fractal-like multimodal components with varying scales and exponents
        for i in range(self.dim):
            scale = self.scales[i]
            exponent = self.fractal_exponents[i]
            # Multi-scale sinusoidal modulations
            result += 0.1 * scale * np.sin(scale * x[i]) * np.cos(2.0 * scale * x[i]) + \
                      0.05 * scale * np.sin(3.0 * scale * x[i]) * np.cos(4.0 * scale * x[i]) + \
                      0.02 * scale * np.sin(5.0 * scale * x[i])
        
        # Self-similar interaction terms with multiple fractal dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for scalability
                # Fractal interaction with scale-dependent coupling
                coupling = 0.3 * self.scales[i] * self.scales[j] / (self.scales[i] + self.scales[j])
                result += coupling * np.sin(2.0 * (x[i] + x[j])) * np.cos(3.0 * (x[i] - x[j]))
        
        # Scale-invariant ruggedness through adaptive conditioning
        adaptive_conditioning = np.array([1.0 + 0.5 * np.sin(0.5 * i * np.pi) for i in range(self.dim)])
        result += 0.2 * np.sum(adaptive_conditioning * x**4)
        
        # Multi-fractal polynomial terms
        for i in range(self.dim):
            result += 0.01 * (x[i]**(2 + int(self.fractal_exponents[i] * 4))) * np.cos(5.0 * x[i])
        
        # Add basin-like regions with varying depths
        basin_depths = 0.5 + 0.5 * np.cos(np.arange(self.dim) * np.pi / 3.0)
        for i in range(self.dim):
            result += basin_depths[i] * np.exp(-0.5 * (x[i] - 1.0)**2) + \
                      0.3 * np.exp(-0.5 * (x[i] + 2.0)**2)
        
        # Add noise with fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(10.0 * x[i] * self.scales[i]) * np.cos(8.0 * x[i] * self.scales[i])
        result += noise
        
        return result