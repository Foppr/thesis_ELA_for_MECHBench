import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.r = 3.8
        self.noise_scale = 0.1
        # Generate random noise terms for each dimension
        np.random.seed(42)  # For reproducibility
        self.noise_terms = np.random.randn(dim)
        
    def f(self, x):
        # Clip input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        if r < 1e-10:
            r = 1e-10
        chaotic_factor = 1.0 + 0.5 * np.sin(self.r * np.log(r)) * np.cos(self.r * np.log(r))
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        wave_sum = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * 2.0
            amp = 1.0 + 0.3 * np.sin(i * 0.5)
            wave_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Add chaotic modulation to wave components
        wave_sum *= chaotic_factor
        
        # Add noise perturbations
        noise = np.sum(self.noise_terms * np.exp(-0.5 * (x - self.noise_terms)**2))
        
        # Radial polynomial term with chaotic influence
        poly_term = 0.2 * r**3 + 0.1 * r**4
        
        # Combine all components
        return wave_sum + noise + poly_term