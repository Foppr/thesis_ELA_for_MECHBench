import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive curvature
        base = 0.5 * np.sum(x**2)
        
        # Enhanced radial symmetry with multiple local minima
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.0
        for i in range(1, 8):
            radial_term += (1.0 / i**1.5) * np.sin(i * r) * np.exp(-0.05 * r**2)
        
        # Modified adaptive curvature based on position with enhanced nonlinearity
        adaptive_curvature = 0.0
        for i in range(self.dim):
            # Position-dependent scaling factor with higher frequency modulation
            scale_factor = 1.0 + 0.7 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            adaptive_curvature += scale_factor * x[i]**4
        
        # Augmented saddle-point dominance with cross-dimensional interactions
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling to reduce complexity
                # Enhanced hyperbolic tangent interaction creating stronger saddle points
                saddle_interaction += np.tanh(x[i] * x[j]) * (x[i]**2 + x[j]**2) * (1.0 + 0.1 * np.sin(x[i] + x[j]))
        
        # Multi-peak sinusoidal landscape with varying amplitudes and frequencies
        multi_peak = 0.0
        for i in range(self.dim):
            # Varying frequencies and amplitudes with more complex modulation
            freq = 1.5 + 0.5 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i])
            amp = 1.2 + 0.4 * np.sin(0.6 * x[i]) * np.cos(0.5 * x[i])
            multi_peak += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        
        # Condition number modulation through exponential weighting with enhanced control
        condition_mod = 0.0
        for i in range(self.dim):
            condition_mod += np.exp(0.15 * np.abs(x[i])) * x[i]**3
        
        # Additional noise component to improve robustness
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x**2)
        
        return base + radial_term + adaptive_curvature + saddle_interaction + multi_peak + condition_mod + noise