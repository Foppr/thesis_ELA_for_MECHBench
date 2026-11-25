import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequencies and coupling coefficients
        self.frequencies = np.linspace(1.0, 18.0, min(18, dim))
        self.coupling_coeffs = np.random.rand(min(18, dim)) * 1.2 + 0.4
        self.fractal_scale = np.logspace(0, 2.5, min(12, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested trigonometric oscillation component
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i] * (1 + 0.4 * np.sin(0.6 * x[i]))
            trig_term += (np.sin(freq * x[i]) + 0.6 * np.cos(2 * freq * x[i]) + 0.3 * np.sin(3 * freq * x[i]))**2
        
        # Adaptive polynomial coupling between dimensions with enhanced nonlinearity
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = self.coupling_coeffs[i] * self.coupling_coeffs[j]
                poly_coupling += coeff * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * np.cos(0.5 * x[i] + 0.3 * x[j])
        
        # Fractal-like boundary effects with asymmetric penalties
        boundary_effect = 0.0
        for i in range(self.dim):
            if x[i] < -4.5:
                boundary_effect += 2.0 * (np.exp(-0.25 * (x[i] + 4.5)**2) + 0.4 * np.sin(12 * x[i]))
            elif x[i] > 4.5:
                boundary_effect += 2.5 * (np.exp(-0.2 * (x[i] - 4.5)**2) + 0.3 * np.cos(10 * x[i]))
        
        # Multi-scale harmonic interference with varying amplitudes and phases
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(10, self.dim+1)):
                amp = 1.2 + 0.6 * np.sin(k * x[i]) * np.cos(i * 0.5)
                phase = 0.3 * np.sin(i * 0.4) * k + 0.1 * np.cos(i * 0.2)
                interference_term += amp * np.sin(k * x[i] + phase) * np.cos(k**1.3 * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Fractal modulation of the landscape using log-scale spacing with additional sine component
        fractal_mod = 0.0
        for i in range(self.dim):
            scale = self.fractal_scale[i % len(self.fractal_scale)]
            fractal_mod += scale * np.sin(scale * x[i]) * np.cos(scale * x[i]**2) + 0.5 * np.sin(0.5 * scale * x[i]**3)
        
        # Combine all components with weighted contributions
        result = 0.8 * trig_term + 0.6 * poly_coupling + 0.5 * boundary_effect + \
                 0.7 * interference_term + 0.4 * fractal_mod
        
        return result