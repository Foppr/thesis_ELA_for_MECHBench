import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute angular frequencies for trigonometric components
        self.freqs = np.linspace(1.0, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive scaling
        rbf = np.sum(np.exp(-0.5 * (x**2)) * np.cos(self.freqs * x))
        
        # Trigonometric coupling with dynamic phase modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            phase = np.sin(x[i] * 0.5) + 0.3 * np.cos(x[i] * 1.2)
            trig_coupling += np.sin(self.freqs[i] * x[i] + phase) * np.cos(self.freqs[i] * x[i] + phase)
        
        # Polynomial chaos with adaptive exponents
        poly_chaos = np.sum((x**3) * np.sin(2.0 * x) * np.cos(1.5 * x))
        
        # Cross-dimensional harmonic interactions
        cross_harmonic = 0.0
        for i in range(self.dim - 1):
            cross_harmonic += np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        
        # Adaptive radial component with variable radius
        radial_component = np.sum(np.exp(-0.3 * (x**2)) * np.sin(3.0 * x))
        
        # Sine-cosine coupled oscillations
        osc_coupling = 0.0
        for i in range(self.dim):
            osc_coupling += np.sin(x[i]) * np.cos(1.8 * x[i]) + np.cos(x[i]) * np.sin(2.2 * x[i])
        
        # Fractal-like self-similarity through recursive scaling
        fractal_scale = 0.0
        for i in range(self.dim):
            fractal_scale += (x[i]**2) * np.sin(1.5 * x[i]) * np.cos(2.5 * x[i])
        
        # Combined weighted function with dynamic scaling factor
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        return scale_factor * (rbf + trig_coupling + poly_chaos + cross_harmonic + radial_component + osc_coupling + fractal_scale)