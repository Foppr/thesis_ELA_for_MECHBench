import numpy as np

class PolynomialFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley component with varying degrees
        poly_valley = np.sum(0.5 * x**4 - 2.0 * x**2 + 0.5 * x)
        
        # Exponential barrier component with fractal-like positioning
        exp_barrier = 0.0
        for i in range(self.dim):
            barrier_pos = 2.0 * np.sin(0.3 * i + x[i] * 0.7) + 1.0
            exp_barrier += 2.0 * np.exp(-0.5 * (x[i] - barrier_pos)**2 / (0.5 + 0.3 * np.cos(i)))
        
        # Fractal sine wave component with multi-scale frequencies
        fractal_sine = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            fractal_sine += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Mixed harmonic and cubic component
        mixed_harmonic = np.sum(0.8 * np.sin(2.0 * x) * np.cos(1.5 * x) + 0.3 * x**3)
        
        # Radial gradient with sinusoidal modulation
        radial_grad = np.sum(1.2 * np.sqrt(np.sum(x**2)) * (1.0 + 0.3 * np.cos(0.7 * np.sum(x))))
        
        # Combine all components
        result = poly_valley + exp_barrier + fractal_sine + mixed_harmonic + radial_grad
        
        return result