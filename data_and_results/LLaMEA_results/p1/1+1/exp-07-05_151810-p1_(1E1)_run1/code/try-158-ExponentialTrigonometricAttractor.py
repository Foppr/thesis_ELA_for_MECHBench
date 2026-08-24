import numpy as np

class ExponentialTrigonometricAttractor:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with multi-scale modulation
        exp_component = np.sum(2.0 * np.exp(-0.5 * np.sum((x - 1.0)**2)) * np.exp(-0.3 * np.sum((x + 1.0)**2)))
        
        # Trigonometric coupling with phase-shifted harmonics and adaptive amplitude
        trig_coupling = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.7 * i) + 0.3 * np.cos(0.4 * i)
            amplitude = 1.0 + 0.2 * np.sin(0.6 * i)
            trig_coupling += amplitude * np.sin(2.0 * x[i] + phase) * np.cos(1.5 * x[i] + phase)
        
        # Gradient-based attraction fields with repulsion zones
        attraction = 0.0
        for i in range(self.dim):
            # Attraction towards multiple local optima
            attraction += np.sum(0.8 * np.exp(-0.2 * (x[i] - np.sin(i * 0.5))**2) * 
                               np.exp(-0.1 * (x[i] - np.cos(i * 0.3))**2))
        
        # Multi-scale sinusoidal modulation with adaptive frequency
        multi_scale = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.5 * i)
            multi_scale += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive noise injection with fitness-dependent intensity
        noise_intensity = 0.1 * (1.0 + 0.5 * np.sin(np.sum(x)))
        noise = np.random.normal(0, noise_intensity, self.dim)
        noise_component = np.sum(noise**2)
        
        # Combine all components with dynamic weighting
        weight_exp = 1.0 + 0.1 * np.sin(0.2 * np.sum(x))
        weight_trig = 1.0 + 0.15 * np.cos(0.3 * np.sum(x))
        weight_attraction = 1.0 + 0.2 * np.sin(0.1 * np.sum(x))
        weight_multi = 1.0 + 0.05 * np.cos(0.4 * np.sum(x))
        
        result = weight_exp * exp_component + weight_trig * trig_coupling + weight_attraction * attraction + weight_multi * multi_scale + noise_component
        
        return result