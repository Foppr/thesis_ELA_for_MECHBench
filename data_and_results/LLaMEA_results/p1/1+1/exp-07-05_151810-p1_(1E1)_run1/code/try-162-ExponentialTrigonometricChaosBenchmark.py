import numpy as np

class ExponentialTrigonometricChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with dimensionally adaptive rates
        exp_component = np.sum(0.8 * np.exp(-0.5 * np.abs(x)) * np.cos(1.2 * x) * np.sin(0.7 * x))
        
        # Trigonometric coupling with adaptive phase shifts and amplitude modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.4 * i + 0.2 * np.sum(x))
            amplitude_mod = 1.0 + 0.2 * np.cos(0.5 * i + 0.1 * np.sum(x))
            trig_coupling += amplitude_mod * np.sin(x[i] + phase_shift) * np.cos(x[i] * 0.8 + phase_shift)
        
        # Polynomial chaos component with Hermite-like basis functions and cross-dimensional interactions
        chaos_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term = (x[i] * x[j]) / (1.0 + 0.1 * np.abs(x[i] - x[j]))
                chaos_component += cross_term * np.exp(-0.3 * (x[i]**2 + x[j]**2))
        
        # Adaptive conditioning with dynamic scaling based on coordinate positions
        conditioning = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.6 * x[i] + 0.2 * np.cos(0.4 * x[i]))
            conditioning += scale_factor * x[i]**3
        
        # Multi-scale harmonic oscillation with frequency modulation and amplitude variation
        harmonic = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.2 * np.sin(0.3 * i + 0.1 * np.sum(x))
            amp_var = 0.8 + 0.4 * np.cos(0.5 * i + 0.2 * np.sum(x))
            harmonic += amp_var * np.sin(freq_mod * x[i] + 0.3 * np.cos(0.4 * x[i]))
        
        # Combine all components with dynamic weights based on input characteristics
        total_weight = 1.0 + 0.1 * np.sin(0.2 * np.sum(x))
        result = total_weight * (exp_component + trig_coupling + chaos_component + conditioning + harmonic)
        
        return result