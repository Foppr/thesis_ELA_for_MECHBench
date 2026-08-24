import numpy as np

class ExponentialWaveBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with varying rates and offsets
        exp_component = np.sum(1.5 * np.exp(-0.5 * (x - 1.0)**2) * np.exp(-0.3 * (x + 2.0)**2))
        
        # Trigonometric wave interference with amplitude modulation
        wave_component = 0.0
        for i in range(self.dim):
            wave_component += 2.0 * np.sin(2.0 * x[i] + 0.5 * np.cos(1.5 * x[i])) * np.cos(1.0 * x[i] + 0.3 * np.sin(2.0 * x[i]))
        
        # Logarithmic barrier functions with adaptive thresholds
        barrier = 0.0
        for i in range(self.dim):
            barrier += 1.0 / (1.0 + np.exp(-5.0 * (x[i] - 3.0))) + 1.0 / (1.0 + np.exp(5.0 * (x[i] + 3.0)))
        
        # Multi-scale harmonic oscillation with frequency coupling
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += 0.8 * np.sin(3.0 * x[i] + 0.2 * np.sin(0.5 * x[i])) * np.cos(2.0 * x[i] + 0.1 * np.cos(1.0 * x[i]))
        
        # Cross-term interaction with quadratic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.5 * (x[i] - x[j])**2 * np.sin(0.5 * (x[i] + x[j]))
        
        # Combine all components with dynamic weighting based on position
        weight_exp = 1.0 + 0.3 * np.sin(0.2 * np.sum(x))
        weight_wave = 1.0 + 0.2 * np.cos(0.1 * np.sum(x))
        weight_barrier = 1.0 + 0.25 * np.sin(0.15 * np.sum(x))
        weight_harmonic = 1.0 + 0.15 * np.cos(0.25 * np.sum(x))
        weight_cross = 1.0 + 0.1 * np.sin(0.3 * np.sum(x))
        
        result = weight_exp * exp_component + weight_wave * wave_component + weight_barrier * barrier + weight_harmonic * harmonic + weight_cross * cross_term
        
        return result