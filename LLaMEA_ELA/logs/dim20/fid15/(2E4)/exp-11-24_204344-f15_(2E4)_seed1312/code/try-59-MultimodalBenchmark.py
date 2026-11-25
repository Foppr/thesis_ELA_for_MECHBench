import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term for conditioning
        quadratic = 0.1 * np.sum(x**2)
        
        # Fractal-like sinusoidal structure with varying frequencies and amplitudes
        fractal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            amp = 1.0 + 0.5 * np.sin(i * 0.7)
            fractal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.05 * x[i]**2)
        
        # Polynomial cross-dimensional interactions with non-linear coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for locality
                poly_interaction += (x[i] * x[j])**3 + 0.5 * (x[i]**2 + x[j]**2) * np.sin(x[i] + x[j])
        
        # Logarithmic barrier terms to create ruggedness near boundaries
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += 1.0 / (1.0 + np.exp(-5 * (x[i] - 5.0))) + 1.0 / (1.0 + np.exp(5 * (x[i] + 5.0)))
        
        # Multi-scale oscillatory component with exponentially decaying amplitudes
        multi_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.0
            for k in range(1, 6):
                scale_factor *= 0.8
                multi_scale += scale_factor * np.sin(k * 2**k * x[i]) * np.cos(k * 3**k * x[i])
        
        # Asymmetric multimodal components with varying heights and widths
        asymmetric = 0.0
        for i in range(self.dim):
            asymmetric += 0.5 * (np.sin(10 * x[i]) + 1)**2 * np.exp(-0.5 * (x[i] - 1.5)**2) + \
                         0.3 * (np.cos(8 * x[i]) - 1)**3 * np.exp(-0.3 * (x[i] + 2.0)**2)
        
        # Coupled harmonic terms with phase shifts
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j - i <= 3:  # Local coupling only
                    harmonic += np.sin(2 * x[i] + 3 * x[j]) * np.cos(4 * x[i] - x[j])
        
        # Small random noise component to increase robustness testing
        noise = 0.05 * np.sum(np.random.randn(self.dim) * np.sin(7 * x))
        
        return quadratic + fractal + poly_interaction + log_barrier + multi_scale + asymmetric + harmonic + noise