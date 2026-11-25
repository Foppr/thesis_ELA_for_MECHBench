import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with adaptive scaling
        r = np.sqrt(np.sum(x**2))
        radial_factor = 1.0 + 0.5 * np.sin(0.5 * r)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.2 * (i + 1)
            amp = 1.0 / (1.0 + 0.1 * (i + 1))
            trig_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * radial_factor
        
        # Multimodal component with multiple peaks
        multi_peak = 0.0
        for i in range(self.dim):
            multi_peak += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + 0.5 * np.sin(5.0 * x[i])
        
        # Cross-dimensional interaction with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 * (1.0 + np.sin(0.2 * (x[i] + x[j])))
                cross_term += coupling_strength * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(0.5 * x[i] * x[j])
        
        # Asymmetric scaling and polynomial terms
        asym_factor = 1.0 + 0.3 * np.sin(0.7 * r)
        poly_term = np.sum((x**2) * asym_factor) * np.cos(0.3 * r)
        
        # Final combined function
        result = trig_sum + multi_peak + cross_term + poly_term
        
        return result