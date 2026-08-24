import numpy as np

class FractalGaussianMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal structure
        self.fractal_scale = 2.0
        self.gaussian_amplitude = 1.0
        self.conditioning_factor = 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2) * self.conditioning_factor
        
        # Composite Gaussian peaks with varying scales and positions
        gaussian_sum = 0.0
        peak_positions = np.linspace(-1, 1, min(10, self.dim))
        for i in range(min(10, self.dim)):
            pos = peak_positions[i]
            scale = 0.5 + 0.5 * np.sin(i * 0.5)
            gaussian_sum += self.gaussian_amplitude * np.exp(-0.5 * ((x_norm - pos) / scale)**2)
        
        # Fractal-like self-similarity with recursive scaling
        fractal = 0.0
        for i in range(1, min(5, self.dim + 1)):
            fractal += np.sum(np.sin(self.fractal_scale**i * x_norm)**2)
        
        # Adaptive conditioning based on input magnitude
        adaptive_cond = np.sum(np.abs(x_norm)**1.5)
        
        # Cross-term with sinusoidal coupling and phase modulation
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.sin(x_norm[i] + x_norm[i+1]) * np.cos(2 * x_norm[i] - x_norm[i+1])
        
        # Multi-scale oscillation with chaotic perturbation
        chaotic_osc = 0.0
        for i in range(self.dim):
            chaotic_osc += np.sin(10 * x_norm[i]) * np.cos(15 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Combine all components with appropriate weights
        return 0.3 * quadratic + 1.5 * gaussian_sum + 0.8 * fractal + 0.6 * adaptive_cond + 0.7 * cross_term + 1.2 * chaotic_osc