import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive curvature
        base = 0.5 * np.sum(x**2)
        
        # Radial symmetry with multiple local minima
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.0
        for i in range(1, 6):
            radial_term += (1.0 / i) * np.sin(i * r) * np.exp(-0.1 * r**2)
        
        # Adaptive curvature based on position
        adaptive_curvature = 0.0
        for i in range(self.dim):
            # Position-dependent scaling factor
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * x[i])
            adaptive_curvature += scale_factor * x[i]**4
        
        # Saddle-point dominance with cross-dimensional interactions
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperbolic tangent interaction creating saddle points
                saddle_interaction += np.tanh(x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        # Multi-peak sinusoidal landscape with varying amplitudes
        multi_peak = 0.0
        for i in range(self.dim):
            # Varying frequencies and amplitudes
            freq = 1.0 + 0.2 * np.sin(0.5 * x[i])
            amp = 1.0 + 0.3 * np.cos(0.4 * x[i])
            multi_peak += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Condition number modulation through exponential weighting
        condition_mod = 0.0
        for i in range(self.dim):
            condition_mod += np.exp(0.2 * np.abs(x[i])) * x[i]**3
        
        return base + radial_term + adaptive_curvature + saddle_interaction + multi_peak + condition_mod