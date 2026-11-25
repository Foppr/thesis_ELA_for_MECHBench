import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive frequencies and coupling coefficients
        self.frequencies = np.linspace(1.0, 25.0, min(25, dim))
        self.coupling_coeffs = np.random.rand(min(25, dim)) * 0.8 + 0.2
        self.fractal_scale = np.logspace(0, 3.0, min(15, dim))
        # Add chaotic logistic map parameters for enhanced complexity
        self.logistic_r = 3.9 + np.random.rand(min(15, dim)) * 0.2
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested trigonometric oscillation component with chaotic modulation
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i] * (1 + 0.5 * np.sin(0.7 * x[i]))
            # Introduce chaotic modulation using logistic map
            chaotic_factor = 1.0 + 0.3 * (self.logistic_r[i % len(self.logistic_r)] * 
                                          x[i] * (1 - x[i]**2) if abs(x[i]) < 1 else 0)
            trig_term += (np.sin(freq * x[i]) + 0.7 * np.cos(2 * freq * x[i]))**2 * chaotic_factor
        
        # Adaptive polynomial coupling between dimensions with cross-interference
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = self.coupling_coeffs[i] * self.coupling_coeffs[j]
                # Add cross-dimensional interference term
                interference = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                poly_coupling += coeff * (x[i]**3 + x[j]**3) * interference
        
        # Fractal-like boundary effects with asymmetric penalties and additional noise
        boundary_effect = 0.0
        for i in range(self.dim):
            if x[i] < -4.8:
                boundary_effect += 2.5 * (np.exp(-0.2 * (x[i] + 4.8)**2) + 0.5 * np.sin(15 * x[i]))
            elif x[i] > 4.8:
                boundary_effect += 3.0 * (np.exp(-0.15 * (x[i] - 4.8)**2) + 0.4 * np.cos(12 * x[i]))
        
        # Multi-scale harmonic interference with varying amplitudes and phase shifts
        interference_term = 0.0
        for i in range(self.dim):
            for k in range(1, min(12, self.dim+1)):
                amp = 1.5 + 0.4 * np.sin(k * x[i]) * np.cos(i * 0.6)
                phase = 0.4 * np.sin(i * 0.5) * k + 0.2 * np.random.rand()
                interference_term += amp * np.sin(k * x[i] + phase) * np.cos(k**1.4 * x[i])
        
        # Fractal modulation of the landscape using log-scale spacing and additional nonlinear terms
        fractal_mod = 0.0
        for i in range(self.dim):
            scale = self.fractal_scale[i % len(self.fractal_scale)]
            fractal_mod += scale * np.sin(scale * x[i]) * np.cos(scale * x[i]**2) + \
                           0.4 * np.sin(scale**1.6 * x[i]**3)
        
        # Add a new chaotic component based on sine-cosine products
        chaotic_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                chaotic_component += np.sin(x[i]) * np.cos(x[j]) * (x[i]**3 + x[j]**3)
        
        # Combine all components with weighted contributions
        result = 0.9 * trig_term + 0.7 * poly_coupling + 0.6 * boundary_effect + \
                 0.8 * interference_term + 0.5 * fractal_mod + 0.4 * chaotic_component
        
        return result