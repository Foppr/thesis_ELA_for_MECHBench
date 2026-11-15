import numpy as np

class ExponentialWaveBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with varying rates and directional bias
        exp_component = np.sum(0.8 * np.exp(-0.5 * np.sum((x - 2.0 * np.sin(x))**2)) * 
                             np.exp(-0.3 * np.sum((x + 1.5 * np.cos(x))**2)))
        
        # Trigonometric wave interference with frequency modulation and phase shifts
        wave_component = 0.0
        for i in range(self.dim):
            wave_component += np.sin(2.0 * x[i] + 0.5 * np.sin(1.2 * x[i])) * \
                            np.cos(1.5 * x[i] + 0.3 * np.cos(0.8 * x[i])) * \
                            np.sin(0.7 * x[i] + 0.4 * np.sin(1.0 * x[i]))
        
        # Logarithmic barrier functions with adaptive thresholds and scaling
        barrier_component = 0.0
        for i in range(self.dim):
            barrier = np.log(1.0 + 0.5 * (x[i]**2) + 0.3 * np.abs(x[i]) + 0.1 * np.sin(2.0 * x[i]))
            barrier_component += barrier * (1.0 + 0.2 * np.cos(0.5 * x[i]))
        
        # Multi-scale harmonic oscillation with amplitude and frequency modulation
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_component += 0.6 * np.sin(3.0 * x[i] + 0.2 * np.sin(2.0 * x[i])) * \
                               np.cos(2.5 * x[i] + 0.3 * np.cos(1.5 * x[i])) * \
                               (1.0 + 0.1 * np.sin(0.8 * x[i]))
        
        # Adaptive weighting based on coordinate sum and dimensionality
        weight_exp = 1.0 + 0.15 * np.sin(0.2 * np.sum(x))
        weight_wave = 1.0 + 0.1 * np.cos(0.3 * np.sum(x))
        weight_barrier = 1.0 + 0.2 * np.sin(0.1 * np.sum(x))
        weight_harmonic = 1.0 + 0.05 * np.cos(0.4 * np.sum(x))
        
        # Combine all components with adaptive scaling
        result = weight_exp * exp_component + weight_wave * wave_component + \
                weight_barrier * barrier_component + weight_harmonic * harmonic_component
        
        return result