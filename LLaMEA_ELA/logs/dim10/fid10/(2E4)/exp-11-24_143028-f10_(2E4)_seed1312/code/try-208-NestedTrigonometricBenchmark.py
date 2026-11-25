import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequencies and coupling coefficients
        self.frequencies = np.linspace(1.0, 15.0, min(15, dim))
        self.coupling_coeffs = np.random.rand(min(15, dim)) * 0.8 + 0.2
        self.fractal_scale = np.logspace(0, 2, min(10, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested trigonometric oscillation component
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i] * (1 + 0.3 * np.sin(0.5 * x[i]))
            trig_term += (np.sin(freq * x[i]) + 0.5 * np.cos(2 * freq * x[i]))**2
        
        # Adaptive polynomial coupling between dimensions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = self.coupling_coeffs[i] * self.coupling_coeffs[j]
                poly_coupling += coeff * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
        
        # Fractal-like boundary effects with asymmetric penalties
        boundary_effect = 0.0
        for i in range(self.dim):
            if x[i] < -4.5:
                boundary_effect += 1.5 * (np.exp(-0.2 * (x[i] + 4.5)**2) + 0.3 * np.sin(10 * x[i]))
            elif x[i] > 4.5:
                boundary_effect += 2.0 * (np.exp(-0.15 * (x[i] - 4.5)**2) + 0.2 * np.cos(8 * x[i]))
        
        # Multi-scale harmonic interference with varying amplitudes
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(8, self.dim+1)):
                amp = 1.0 + 0.5 * np.sin(k * x[i]) * np.cos(i * 0.4)
                phase = 0.2 * np.sin(i * 0.3) * k
                interference_term += amp * np.sin(k * x[i] + phase) * np.cos(k**1.2 * x[i])
        
        # Fractal modulation of the landscape using log-scale spacing
        fractal_mod = 0.0
        for i in range(self.dim):
            scale = self.fractal_scale[i % len(self.fractal_scale)]
            fractal_mod += scale * np.sin(scale * x[i]) * np.cos(scale * x[i]**2)
        
        # Combine all components with weighted contributions
        result = 0.7 * trig_term + 0.5 * poly_coupling + 0.4 * boundary_effect + \
                 0.6 * interference_term + 0.3 * fractal_mod
        
        return result