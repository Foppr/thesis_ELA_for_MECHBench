import numpy as np

class ExponentialWavePerturbationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with dimension-dependent scaling
        exp_component = np.sum(2.0 * np.exp(-0.5 * np.abs(x)) * np.cos(1.0 * x) * np.sin(0.5 * x))
        
        # Trigonometric wave interference with varying frequencies and amplitudes
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.2 * i)
            amp = 1.0 + 0.2 * np.cos(0.1 * i)
            wave_interference += amp * np.sin(freq * x[i] + 0.5 * np.cos(0.3 * x[i]))
        
        # Stochastic perturbation component with adaptive noise scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.random.normal(0, 0.1 * (1.0 + 0.1 * np.sin(0.4 * i))) * np.sin(0.7 * x[i])
        
        # Adaptive scaling based on dimensionality and position
        scale_factor = 1.0 + 0.1 * np.sin(0.3 * np.sum(x)) + 0.05 * np.cos(0.2 * self.dim)
        
        # Multi-scale radial component with exponential modulation
        radial = np.sum(1.5 * np.exp(-0.2 * np.sum(x**2)) * (1.0 + 0.3 * np.sin(2.0 * np.sum(x))))
        
        # Cross-term interaction with exponential decay
        cross_term = np.sum(0.8 * np.exp(-0.1 * np.abs(x[:-1] - x[1:])) * np.cos(1.5 * (x[:-1] + x[1:])))
        
        # Combine all components with dimensionally adaptive weights
        weight_exp = 1.0 + 0.1 * np.sin(0.2 * np.sum(x))
        weight_wave = 1.0 + 0.15 * np.cos(0.1 * np.sum(x))
        weight_noise = 1.0 + 0.05 * np.sin(0.3 * np.sum(x))
        weight_radial = 1.0 + 0.2 * np.cos(0.25 * np.sum(x))
        weight_cross = 1.0 + 0.1 * np.sin(0.4 * np.sum(x))
        
        result = (weight_exp * exp_component + 
                 weight_wave * wave_interference + 
                 weight_noise * noise + 
                 weight_radial * radial + 
                 weight_cross * cross_term) * scale_factor
        
        return result