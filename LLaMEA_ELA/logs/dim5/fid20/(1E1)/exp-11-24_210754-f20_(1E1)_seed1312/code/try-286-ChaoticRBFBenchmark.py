import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic center placement
        rb_f = 0.0
        for i in range(self.dim):
            # Chaotic offset using sine-based positioning
            center = 3.0 * np.sin(i * 0.7) + 1.5 * np.cos(i * 0.4)
            rb_f += np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.2 * np.sin(i * 0.9)))**2)
        
        # Sinusoidal oscillation with varying frequency and amplitude
        sin_f = 0.0
        for i in range(self.dim):
            freq = 20.0 * (1.0 + 0.5 * np.sin(i * 0.6))
            amp = 1.5 + 0.8 * np.cos(i * 0.3)
            sin_f += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Asymmetric saddle point structure with exponential modulation
        saddle_f = 0.0
        for i in range(self.dim):
            # Exponential decay with asymmetric curvature
            saddle_f += (x[i]**3 + 0.5 * x[i]**2 - 0.3 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Multi-scale interference pattern using fractional powers and modulations
        frac_f = 0.0
        for i in range(self.dim):
            frac_f += (np.abs(x[i])**1.7 + 0.8 * np.sin(15.0 * x[i])) * np.cos(10.0 * x[i])
        
        # Cross-dimensional interaction with chaotic coupling weights
        cross_f = 0.0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.3 * np.sin(i * 0.8)
            cross_f += weight * np.sin(x[i] + 0.7 * x[i+1]) * np.cos(0.9 * x[i] - x[i+1])
        
        # Combined objective with dynamic scaling
        return 0.5 * (rb_f + sin_f + saddle_f + frac_f + cross_f) / self.dim